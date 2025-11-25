# ===============================================================
# Smart Playlist Analyzer: Step 1 - Feature Extraction
# Description:
#   This script analyzes a folder of MP3 files and extracts
#   key musical features for each song:
#       - Tempo (beats per minute)
#       - Energy (normalized loudness)
#       - Mood (interpretable combination of tempo + energy)
#       - Duration (in seconds)
#   The results are saved into a CSV file for later algorithmic use.
# ===============================================================

import sys, glob, librosa, numpy as np, pandas as pd, os

# ========================
#   CONFIGURABLE PARAMS
# ========================
SR = 22050           # Sampling rate (Hz) – resample all songs for consistency
HOP = 512            # Hop length for analysis – smaller = more precise but slower
SEG = 25             # Analyze only the middle 25 seconds of each song

# ---------------------------------------------------------------
# Helper: load_mid()
# ---------------------------------------------------------------
def load_mid(y, sr, seg=SEG):
    """
    Extract a centered segment of 'seg' seconds from an audio track.

    Why:
      - Speeds up analysis (no need to analyze full songs)
      - Avoids noisy intros/outros or silence
    Returns:
      (trimmed_audio, total_duration)
    """
    d = librosa.get_duration(y=y, sr=sr)
    if d <= seg:
        # If the song is short, use the full audio
        return y, d
    # Find the midpoint and slice around it
    mid = len(y) // 2
    half = int(seg * sr // 2)
    return y[mid - half : mid + half], d


# ---------------------------------------------------------------
# Core: score()
# ---------------------------------------------------------------
def score(mp3):
    """
    Analyze one MP3 file and return its musical feature scores.

    Returns:
        tempo   – beats per minute (BPM)
        energy  – normalized RMS loudness (0–1)
        mood    – interpretable mood score (0–1)
        dur     – duration (seconds)
    """
    # Load audio (mono) and resample to SR
    y, sr = librosa.load(mp3, sr=SR, mono=True)

    # Take only the middle SEG seconds for consistent analysis
    y, dur = load_mid(y, sr)

    # ---- TEMPO (BPM) ----
    # Use librosa's beat detection to estimate global tempo
    tempo = float(librosa.beat.tempo(y=y, sr=sr, hop_length=HOP, aggregate=np.median))

    # ---- ENERGY ----
    # Compute frame-wise RMS (Root Mean Square) amplitude = loudness
    rms_frames = librosa.feature.rms(y=y, frame_length=2048, hop_length=HOP).flatten()
    rms_mean = float(rms_frames.mean())

    # Dynamic normalization to [0,1]:
    # use the 95th percentile RMS of this track as reference loudness.
    # This avoids saturation for modern loudly mastered tracks.
    ref = float(np.percentile(rms_frames, 95))
    if ref <= 1e-8:
        energy = 0.0
    else:
        energy = float(np.clip(rms_mean / ref, 0.0, 1.0))

    # ---- MOOD SCORE ----
    # Combine tempo and loudness into an interpretable mood indicator.
    # Higher tempo + higher loudness = more energetic or "happier".
    # Lower tempo + softer sound = calmer or "sadder".
    tempo_mean, tempo_std = 120.0, 30.0   # Empirical stats for pop music
    energy_mean, energy_std = 0.05, 0.03  # Typical RMS range (for z-score scaling)

    zt = (tempo - tempo_mean) / max(tempo_std, 1e-6)
    ze = (rms_mean - energy_mean) / max(energy_std, 1e-6)

    # Sigmoid function maps values smoothly into [0,1]
    sig = lambda x: 1 / (1 + np.exp(-x))
    # Weighted combination: tempo contributes more than energy
    mood = float(np.clip(0.6 * sig(zt) + 0.4 * sig(ze), 0.0, 1.0))

    return tempo, energy, mood, dur


# ---------------------------------------------------------------
# Main: process entire folder
# ---------------------------------------------------------------
def main(indir, outcsv):
    """
    Walk through all MP3 files under 'indir',
    analyze each one with score(), and write a summary CSV.
    """
    rows = []

    # Recursively find all .mp3 files in the directory
    for mp3 in sorted(glob.glob(os.path.join(indir, "**/*.mp3"), recursive=True)):
        try:
            tempo, energy, mood, dur = score(mp3)
            rows.append({
                "file": mp3,
                "tempo": tempo,
                "energy": energy,
                "mood": mood,
                "duration": dur
            })
        except Exception as e:
            # Log any decoding or analysis error but continue
            print(f"[WARN] Failed on {mp3}: {e}")
            rows.append({
                "file": mp3,
                "tempo": np.nan,
                "energy": np.nan,
                "mood": np.nan,
                "duration": np.nan,
                "error": str(e)
            })

    # Build a DataFrame from all results
    df = pd.DataFrame(rows)

    # Add human-readable helper columns (rounded values)
    df["tempo_bpm"]  = df["tempo"].round(0)
    df["energy_pct"] = (df["energy"] * 100).round(0)
    df["mood_pct"]   = (df["mood"] * 100).round(0)
    df["duration_s"] = df["duration"].round(1)

    # Save as UTF-8 CSV for easy import later
    df.to_csv(outcsv, index=False, encoding="utf-8")
    print(f"✅ Features saved to: {outcsv}")


# ---------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python score.py <music_dir> <out_csv>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
