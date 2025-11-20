Instructions for Running the Sorting Modules

I’m sharing two Python files that you will use for the greedy algorithm implementation. Please follow the instructions below to run them correctly.

1. What These Files Do

You will see two Python scripts:

recommended_sort.py – performs sorting based on the recommended rules (mood → tempo → energy).

custom_sort.py – performs sorting based on one single field chosen by the user (mood, tempo, or energy).

When you run each script:

The sorted results will appear directly in the Variable Explorer (as a DataFrame table).

A CSV file containing the sorted results will also be automatically generated on your computer.

These CSV files and data can be used as input for your next step.

2. Important: Update the File Path in the main() Function

Inside each script, there is a line in the main() function that loads the CSV file:

csv_path = "..../songs_features.csv"

songs = load_songs(csv_path)

Please update this file path to match the location of the CSV file on your own computer.

If you do not update this path, the script will not be able to load the data properly.
