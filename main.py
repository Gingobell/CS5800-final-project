# main.py
# ---------------------------------------
# Main program:
#   - load songs
#   - run recommended and custom sorting
#   - print results
#   - plot original vs sorted mood curves
# ---------------------------------------

from songs_loader import load_songs
from recommended_sort import recommended_sort
from custom_sort import single_field_sort

import matplotlib.pyplot as plt


def main():
    # 1. Load dataset from local CSV path
    csv_path = "/Users/wanyuanyuan/Documents/NEU /CS5800 Algorithms/Assignment/Final/songs_features.csv"
    songs = load_songs(csv_path)

    # 2. Recommended sort (mood -> tempo -> energy, ascending)
    playlist_recommended = recommended_sort(songs, order="asc")

    # 3. Custom sort example: sort by mood descending
    playlist_custom = single_field_sort(songs, field="mood", order="desc")

    # 4. Print results
    print("=== Recommended Sort (mood -> tempo -> energy, ascending) ===")
    for idx, s in enumerate(playlist_recommended, start=1):
        print(f"{idx:02d}. {s.file}  | mood={s.mood:.3f}  tempo={s.tempo:.1f}  energy={s.energy:.3f}")
    print("\nTotal songs sorted (recommended):", len(playlist_recommended))

    print("\n=== Custom Sort (by mood, descending) ===")
    for idx, s in enumerate(playlist_custom, start=1):
        print(f"{idx:02d}. {s.file}  | mood={s.mood:.3f}  tempo={s.tempo:.1f}  energy={s.energy:.3f}")
    print("\nTotal songs sorted (custom):", len(playlist_custom))

    # 5. Prepare data for plotting (original vs recommended)
    original_moods = [song.mood for song in songs]
    sorted_moods = [song.mood for song in playlist_recommended]

    x_original = list(range(1, len(original_moods) + 1))
    x_sorted = list(range(1, len(sorted_moods) + 1))

    # 6. Plot original vs sorted mood curves
    plt.figure(figsize=(10, 5))

    # Left: original order
    plt.subplot(1, 2, 1)
    plt.plot(x_original, original_moods, marker="o")
    plt.title("Original Order (Mood)")
    plt.xlabel("Song Index (original)")
    plt.ylabel("Mood Score")

    # Right: sorted order
    plt.subplot(1, 2, 2)
    plt.plot(x_sorted, sorted_moods, marker="o")
    plt.title("Sorted Order (Mood)")
    plt.xlabel("Song Index (sorted)")
    plt.ylabel("Mood Score")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
