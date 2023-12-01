import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog as fd 
import json

# Create a list
list_to_store = [1, 2, 3]

# Write the list to a file
with open('list.json', 'w') as f:
    json.dump(list_to_store, f)

# Read the list from the file
with open('list.json', 'r') as f:
    list_from_file = json.load(f)

# Print the list
print(list_from_file)