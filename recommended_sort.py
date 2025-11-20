import csv
from typing import List, Callable, Any
import pandas as pd


#Define Song data 
class Song:
    
    def __init__(self, file: str, mood: float, tempo: float, energy: float, duration: float):
        self.file = file
        self.mood = float(mood)
        self.tempo = float(tempo)
        self.energy = float(energy)
        self.duration = float(duration)

    def __repr__(self) -> str:
        
        return f"{self.file} (mood={self.mood:.2f}, tempo={self.tempo:.2f}, energy={self.energy:.2f})"



#Load songs from a CSV file and return a list of Song objects.
def load_songs(csv_path: str) -> List[Song]:

    songs: List[Song] = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = Song(
                file=row["file"],
                mood=row["mood"],
                tempo=row["tempo"],
                energy=row["energy"],
                duration=row["duration"],
            )
            songs.append(song)
    return songs



# merge sort implementation
# Stable, O(n log n)
def merge_sort(items: List[Any], key_function: Callable[[Any], Any]) -> List[Any]:

    if len(items) <= 1:
        return items

    # Split into two halves
    mid = len(items) // 2
    left = merge_sort(items[:mid], key_function)
    right = merge_sort(items[mid:], key_function)

    # Merge two sorted halves
    merged: List[Any] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key_function(left[i]) <= key_function(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining items
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Default sorting scheme:
#      1. Sort by mood (main key)
#      2. If mood is equal, sort by tempo
#      3. If tempo is equal, sort by energy
#    Supports ascending ("asc") or descending ("desc") order.

def recommended_sort(songs: List[Song], order: str = "asc") -> List[Song]:

    if order not in ("asc", "desc"):
        raise ValueError('order must be "asc" or "desc"')

    # factor = 1 for ascending; -1 for descending
    factor = 1 if order == "asc" else -1

    def key_function(song: Song):
        # Create a tuple (mood, tempo, energy) multiplied by factor
        return (
            factor * song.mood,
            factor * song.tempo,
            factor * song.energy,
        )

    return merge_sort(songs, key_function)


#Save sorted songs to a CSV file.
def save_csv(songs: List[Song], filename: str) -> None:

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["file", "mood", "tempo", "energy", "duration"])
        for s in songs:
            writer.writerow([s.file, s.mood, s.tempo, s.energy, s.duration])


# main
if __name__ == "__main__":

    csv_path = "/Users/wanyuanyuan/Documents/NEU /CS5800 Algorithms/Assignment/Final/songs_features.csv"
    songs = load_songs(csv_path)

    sorted_songs = recommended_sort(songs)

    recommended_sort = pd.DataFrame([{
        "file": s.file,
        "mood": s.mood,
        "tempo": s.tempo,
        "energy": s.energy,
        "duration": s.duration
    } for s in sorted_songs])

    print(recommended_sort)  
    recommended_sort.to_csv("recommended_sorted.csv", index=False, encoding="utf-8")

