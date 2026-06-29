# =====================================================
# SAFE FILE ORGANIZER
# Organizes Downloads folder only
# No file deletion
# No overwrite
# =====================================================

import shutil
from pathlib import Path


# User home folder
home = Path.home()

# Downloads folder
downloads = home / "Downloads"


# -----------------------------------------------------
# File categories
# -----------------------------------------------------

FILE_CATEGORIES = {

    "PDFs": [".pdf"],

    "Documents": [
        ".doc",
        ".docx",
        ".txt",
        ".rtf",
        ".xlsx",
        ".csv"
    ],

    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".webp"
    ],

    "Videos": [
        ".mp4",
        ".mkv",
        ".avi",
        ".mov"
    ],

    "Audio": [
        ".mp3",
        ".wav",
        ".aac"
    ],

    "ZIP_Files": [
        ".zip",
        ".rar",
        ".7z"
    ],

    "Software": [
        ".exe",
        ".msi",
        ".msix"
    ]
}


# -----------------------------------------------------
# Create folders if not exist
# -----------------------------------------------------

for folder_name in FILE_CATEGORIES:

    folder_path = downloads / folder_name

    folder_path.mkdir(exist_ok=True)


# -----------------------------------------------------
# Function to get category
# -----------------------------------------------------

def get_category(extension):

    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():

        if extension in extensions:
            return category

    return None


# -----------------------------------------------------
# Start organizing
# -----------------------------------------------------

print("Organizing files...\n")

moved_count = 0

for item in downloads.iterdir():

    # Skip folders
    if item.is_dir():
        continue

    category = get_category(item.suffix)

    if category is None:
        continue

    destination_folder = downloads / category

    destination_file = destination_folder / item.name


    # -----------------------------------------
    # Avoid overwrite
    # -----------------------------------------

    if destination_file.exists():

        counter = 1

        while True:

            new_name = (
                f"{item.stem}_{counter}"
                f"{item.suffix}"
            )

            new_path = destination_folder / new_name

            if not new_path.exists():

                destination_file = new_path
                break

            counter += 1


    # -----------------------------------------
    # Move file
    # -----------------------------------------

    try:

        shutil.move(
            str(item),
            str(destination_file)
        )

        print(
            f"Moved -> {item.name}"
            f" --> {category}"
        )

        moved_count += 1

    except Exception as e:

        print(
            f"Error moving {item.name}"
        )


print("\nFinished.")
print(f"Total files moved: {moved_count}")