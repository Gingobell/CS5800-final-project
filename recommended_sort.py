# recommended_sort.py
# ---------------------------------------
# Recommended sorting:
#   sort by mood, then tempo, then energy
# ---------------------------------------

from merge_sort import merge_sort

def recommended_sort(songs, order="asc"):
    """
    Default sorting scheme:
      1. Sort by mood (main key)
      2. If mood is equal, sort by tempo
      3. If tempo is equal, sort by energy
    Supports ascending (asc) or descending (desc) order.
    """
    # factor = 1 for ascending; -1 for descending
    factor = 1 if order == "asc" else -1

    def key_function(song):
        # Create a tuple (mood, tempo, energy) multiplied by factor
        return (
            factor * song.mood,
            factor * song.tempo,
            factor * song.energy
        )

    return merge_sort(songs, key_function)

