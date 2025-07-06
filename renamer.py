import os
import re

# Configuration 
folder_path = r"" 
name = "Solo Leveling"
year = 2024
season_number = 1

# Supported video file extensions 
video_extensions = ['.mp4', '.mkv', '.avi', '.mov', '.flv','.ts']


def rename_files():
    files = sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    episode_number = 1

    for file_name in files:
        _, ext = os.path.splitext(file_name)
        if ext.lower() not in video_extensions:
            continue

        new_name = f"{name} ({year}) - S{season_number:02d}E{episode_number:02d}{ext}"
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        print(f"Renaming: {file_name} → {new_name}")
        os.rename(old_path, new_path)
        episode_number += 1


if __name__ == "__main__":
    rename_files()
