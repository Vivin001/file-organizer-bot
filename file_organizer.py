import os
import shutil

# Define the folder you want to organize
SOURCE_FOLDER = "C:/Users/YourUsername/Downloads"  # Change this to your path

# Define folder categories and extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".ps1"],
    "Others": []
}

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(filename)
        moved = False

        for folder_name, extensions in FILE_TYPES.items():
            if extension.lower() in extensions:
                target_folder = os.path.join(folder_path, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} to {folder_name}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved {filename} to Others")

if __name__ == "__main__":
    organize_folder(SOURCE_FOLDER)
    print("🎉 Folder organized successfully!")
