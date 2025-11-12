# custom_sort.py
# ---------------------------------------
# User custom sorting: one field + order
# ---------------------------------------

from merge_sort import merge_sort

def single_field_sort(songs, field, order="asc"):
    """
    User-custom sorting scheme (only one field allowed).
    Parameters:
      field: "mood", "tempo", or "energy"
      order: "asc" for ascending, "desc" for descending
    """
    factor = 1 if order == "asc" else -1

    def key_function(song):
        value = getattr(song, field)  # Get the selected field value
        return (factor * value,)

    return merge_sort(songs, key_function)
