
# 📁 Episode Renamer Script

A simple Python script to rename video files in a folder to a consistent format like:

```
Kaiju No. 8 (2022) - S01E01
```

### 🧠 Format

```
<Name> (<Year>) - S<season_number>E<episode_number>
```

---

## ⚙️ Features

- Supports popular video file types (`.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`)
- Renames files in natural (human-friendly) order
- Automatically formats episode numbers with leading zeros
- Easy to configure and extend

---

## 📦 Requirements

- Python 3.6+
- `natsort` module for natural sorting

Install dependencies:

```bash
pip install natsort
```

---

## 📁 Folder Structure Example

Make sure your video files are named in a way that can be sorted naturally:

```
C:\Users\YourName\Videos\Kaiju
  ├── ep1.mkv
  ├── ep2.mkv
  ├── ep10.mkv
```

---

## 🧪 How to Use

1. Clone or download this repository.
2. Open `rename_episodes.py` and update the configuration section:

```python
folder_path = r"C:\Users\YourName\Videos\Kaiju"
name = "Kaiju No. 8"
year = 2022
season_number = 1
```

3. Run the script from Command Prompt or Terminal:

```bash
python rename_episodes.py
```

The files will be renamed like:

```
Kaiju No. 8 (2022) - S01E01.mkv
Kaiju No. 8 (2022) - S01E02.mkv
...
```

---

## ✅ Example Output

```
Renaming: ep1.mkv → Kaiju No. 8 (2022) - S01E01.mkv
Renaming: ep2.mkv → Kaiju No. 8 (2022) - S01E02.mkv
Renaming: ep10.mkv → Kaiju No. 8 (2022) - S01E03.mkv
```

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
