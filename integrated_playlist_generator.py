import csv
import pandas as pd
from typing import List, Callable, Any


# 1) SONG DATA CLASS

class Song:
    def __init__(self, file: str, mood: float, tempo: float, energy: float, duration: float):
        self.file = file
        self.mood = float(mood)
        self.tempo = float(tempo)
        self.energy = float(energy)
        self.duration = float(duration)

    def __repr__(self) -> str:
        return f"{self.file} (mood={self.mood:.2f}, tempo={self.tempo:.2f}, energy={self.energy:.2f})"



# 2) LOAD SONGS FUNCTION


def load_songs(csv_path: str) -> List[Song]:
    songs: List[Song] = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append(
                Song(row["file"], row["mood"], row["tempo"], row["energy"], row["duration"])
            )
    return songs



# 3) MERGE SORT (used for both sorting methods)#


def merge_sort(items: List[Any], key_function: Callable[[Any], Any]) -> List[Any]:
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid], key_function)
    right = merge_sort(items[mid:], key_function)

    merged: List[Any] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key_function(left[i]) <= key_function(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged



# 4) RECOMMENDED SORT


def recommended_sort(songs: List[Song], order: str = "asc") -> List[Song]:
    factor = 1 if order == "asc" else -1

    def key_function(song: Song):
        return (factor * song.mood, factor * song.tempo, factor * song.energy)

    return merge_sort(songs, key_function)



# 5) CUSTOM SORT


def custom_sort(songs, field="mood", order="asc"):
    if field not in ("mood", "tempo", "energy"):
        raise ValueError('field must be one of: "mood", "tempo", "energy"')

    factor = 1 if order == "asc" else -1

    def key_function(song):
        return factor * getattr(song, field)

    return merge_sort(songs, key_function)



# 6) SAVE SORT RESULTS TO CSV#


def save_csv(songs: List[Song], filename: str):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["file", "mood", "tempo", "energy", "duration"])
        for s in songs:
            writer.writerow([s.file, s.mood, s.tempo, s.energy, s.duration])



# 7) GREEDY PLAYLIST GENERATOR#

def feature_distance(songA, songB):
    return abs(songA["tempo"] - songB["tempo"]) + abs(songA["mood"] - songB["mood"]) + abs(songA["energy"] - songB["energy"])


def greedy_playlist(df):
    used = set()
    current_idx = df["energy"].idxmin()   # start with lowest energy
    playlist_indices = [current_idx]
    used.add(current_idx)

    while len(used) < len(df):
        current_song = df.loc[current_idx]
        candidates = df[~df.index.isin(used)]
        next_idx = candidates.apply(lambda x: feature_distance(x, current_song), axis=1).idxmin()
        playlist_indices.append(next_idx)
        used.add(next_idx)
        current_idx = next_idx

    return df.loc[playlist_indices]



# 8) MAIN SCRIPT

if __name__ == "__main__":

    # CHANGE THIS PATH ONLY
    csv_path = "songs_features.csv"

    # Load Song objects
    songs = load_songs(csv_path)

    
    # SORTING OUTPUTS
    

    sorted_rec = recommended_sort(songs)
    sorted_cus = custom_sort(songs, field="tempo", order="asc")  
    # Save sorting results
    save_csv(sorted_rec, "recommended_sorted.csv")
    save_csv(sorted_cus, "custom_sorted.csv")

    # Convert one of the sorted lists to DataFrame for greedy algorithm
    sorted_df = pd.DataFrame([{
        "file": s.file,
        "tempo": s.tempo,
        "energy": s.energy,
        "mood": s.mood,
        "duration": s.duration
    } for s in sorted_rec])   # use recommended results

    
    # RUN GREEDY PLAYLIST ON SORTED DATA
    

    greedy_df = greedy_playlist(sorted_df)
    greedy_df.to_csv("greedy_playlist.csv", index=False, encoding="utf-8")

    print("\nAll Tasks Completed!")
   
  
