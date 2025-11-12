# songs_loader.py
# ---------------------------------------
# Define the Song class and load songs from CSV
# ---------------------------------------

import csv

class Song:
    def __init__(self, file, mood, tempo, energy, duration):
        self.file = file
        self.mood = float(mood)
        self.tempo = float(tempo)
        self.energy = float(energy)
        self.duration = float(duration)

    def __repr__(self):
        # Make printing more readable
        return f"{self.file} (mood={self.mood:.2f}, tempo={self.tempo:.2f}, energy={self.energy:.2f})"


def load_songs(csv_path):
    """
    Load songs from a CSV file and return a list of Song objects.
    """
    songs = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = Song(
                file=row["file"],
                mood=row["mood"],
                tempo=row["tempo"],
                energy=row["energy"],
                duration=row["duration"]
            )
            songs.append(song)
    return songs
