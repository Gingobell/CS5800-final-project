import csv
from typing import List, Callable, Any
import pandas as pd


#Define Song class
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


# Custom sorting:
# User can choose ONLY ONE dimension to sort on:
#   field ∈ {"mood", "tempo", "energy"}
#   order ∈ {"asc", "desc"}

def custom_sort(songs, field="mood", order="asc"):
    """
    Custom sorting scheme:
      Sort by a single field selected by the user.
      Supported fields: mood, tempo, energy
      Supported order: asc (ascending), desc (descending)
    """
    
    # Validate field
    if field not in ("mood", "tempo", "energy"):
        raise ValueError('field must be one of: "mood", "tempo", "energy"')

    # Determine ascending or descending
    factor = 1 if order == "asc" else -1

    # Build key function dynamically based on the field chosen
    def key_function(song):
        return factor * getattr(song, field)

    return merge_sort(songs, key_function)



#Save sorted songs to a CSV file
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
    
    sorted_custom = custom_sort(songs, field="tempo", order="asc")

    import pandas as pd
    custom_sort = pd.DataFrame([{
        "file": s.file,
        "mood": s.mood,
        "tempo": s.tempo,
        "energy": s.energy,
        "duration": s.duration
    } for s in sorted_custom])

    print(custom_sort)
    custom_sort.to_csv("custom_sorted.csv", index=False, encoding="utf-8")
