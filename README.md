# 🗂 File Organizer Bot

A simple Python script to automatically organize files in a folder by type (Images, Documents, Videos, etc.). This tool helps clean up messy directories like your Downloads folder.

---

## ⚙️ Features

- Categorizes files into folders like: `Images`, `Documents`, `Videos`, `Music`, `Archives`, `Scripts`, and `Others`.
- Automatically creates folders if they don’t exist.
- Easy to configure and run.

---

## 🚀 How to Use

### 1. 🔧 Edit the Folder Path

Open the `file_organizer.py` file in any text editor or IDE (e.g., VS Code, Notepad++).

Locate this line:

```python
SOURCE_FOLDER = "C:/Users/YourUsername/Downloads"
```

Replace it with the path of the folder you want to organize.

**Example for Windows user:**

```python
SOURCE_FOLDER = "C:/Users/IBITS-1038/Downloads"
```

✅ **Important Notes:**
- The folder path must exist.
- Use forward slashes `/` or double backslashes `\` to avoid errors.

---

### 2. 💾 Save the File

After editing the folder path, save the file using your editor (File → Save or `Ctrl+S`).

---

### 3. ▶️ Run the Script

Open a terminal or Command Prompt.

Navigate to the folder where the script is saved using the `cd` command:

```bash
cd path/to/file-organizer-bot
```

Then run the script with:

```bash
python file_organizer.py
```

You should see output like this:

```
Moved resume.pdf to Documents
Moved movie.mp4 to Videos
🎉 Folder organized successfully!
```

---

## 🛠 Troubleshooting

### ❌ Error: `FileNotFoundError: [WinError 3]`

If you get this error:

```
FileNotFoundError: [WinError 3] The system cannot find the path specified
```

It means the path you provided in `SOURCE_FOLDER` does not exist.

✅ **Fix:**
- Double-check the path.
- Make sure there are no typos.
- Use valid formatting like `C:/Users/YourUsername/Downloads`.

---

## 📦 Supported File Categories

| Category   | Extensions |
|------------|------------|
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp` |
| Videos     | `.mp4`, `.mkv`, `.avi`, `.mov` |
| Documents  | `.pdf`, `.docx`, `.txt`, `.xls`, `.xlsx` |
| Music      | `.mp3`, `.wav`, `.aac` |
| Archives   | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Scripts    | `.py`, `.js`, `.sh`, `.bat`, `.ps1` |
| Others     | Anything not matched above |

---

## ✅ Customization

You can add or modify categories by editing the `FILE_TYPES` dictionary inside the script.

---

