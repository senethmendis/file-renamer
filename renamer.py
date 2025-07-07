import os
import re
from natsort import natsorted

# Configuration 
folder_path = r"C:\Users\seneth\Videos\Kaiju"
name = "Kaiju No. 8"
year = 2022
season_number = 1
video_extensions = ['.mp4', '.mkv', '.avi', '.mov', '.flv']

def rename_files():
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files = [f for f in files if os.path.splitext(f)[1].lower() in video_extensions]
    files = natsorted(files)  # <-- natural sorting

    episode_number = 1
    for file_name in files:
        _, ext = os.path.splitext(file_name)
        new_name = f"{name} ({year}) - S{season_number:02d}E{episode_number:02d}{ext}"
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        print(f"Renaming: {file_name} → {new_name}")
        os.rename(old_path, new_path)
        episode_number += 1

if __name__ == "__main__":
    rename_files()
