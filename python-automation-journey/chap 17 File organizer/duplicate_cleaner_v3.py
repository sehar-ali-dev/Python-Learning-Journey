# =====================================================
# Duplicate Cleaner v3
# Safe Duplicate Manager
# Moves duplicates to Duplicate_Files folder
# Creates report
# =====================================================

import hashlib
import shutil
from pathlib import Path

# -----------------------------------------------------
# Downloads folder
# -----------------------------------------------------

home = Path.home()
downloads = home / "Downloads"

# -----------------------------------------------------
# Folder for duplicates
# -----------------------------------------------------

duplicate_folder = downloads / "Duplicate_Files"
duplicate_folder.mkdir(exist_ok=True)

# -----------------------------------------------------
# Ignore folders
# -----------------------------------------------------

IGNORE_FOLDERS = {
    "Duplicate_Files",
    "Microsoft VS Code",
    "VS Code",
    ".git",
    "__pycache__",
    "node_modules"
}

# -----------------------------------------------------
# Storage
# -----------------------------------------------------

file_hashes = {}
duplicates = []

# -----------------------------------------------------
# Hash Function
# -----------------------------------------------------

def get_file_hash(filepath):

    md5 = hashlib.md5()

    try:

        with open(filepath, "rb") as f:

            while True:

                chunk = f.read(4096)

                if not chunk:
                    break

                md5.update(chunk)

        return md5.hexdigest()

    except Exception:

        return None


print("Duplicate Cleaner v3 Started...\n")

# -----------------------------------------------------
# Scan Downloads
# -----------------------------------------------------

for file in downloads.rglob("*"):

    if not file.is_file():
        continue

    skip = False

    for part in file.parts:

        if part in IGNORE_FOLDERS:
            skip = True
            break

    if skip:
        continue

    file_hash = get_file_hash(file)

    if not file_hash:
        continue

    if file_hash in file_hashes:

        duplicates.append(
            (file, Path(file_hashes[file_hash]))
        )

    else:

        file_hashes[file_hash] = str(file)

# -----------------------------------------------------
# Create Report
# -----------------------------------------------------

report_file = "Duplicate Cleaner v3 Report.txt"

with open(report_file, "w", encoding="utf-8") as report:

    report.write("DUPLICATE CLEANER V3 REPORT\n")
    report.write("=" * 60 + "\n\n")

    report.write(
        f"Total Duplicates Found: {len(duplicates)}\n\n"
    )

    for count, (dup, original) in enumerate(
        duplicates,
        start=1
    ):

        report.write(f"{count}\n")
        report.write(
            f"Original : {original}\n"
        )
        report.write(
            f"Duplicate: {dup}\n\n"
        )

# -----------------------------------------------------
# Move Duplicates
# -----------------------------------------------------

moved = 0

for dup, original in duplicates:

    try:

        destination = duplicate_folder / dup.name

        if destination.exists():

            counter = 1

            while True:

                new_name = (
                    f"{dup.stem}_{counter}"
                    f"{dup.suffix}"
                )

                destination = (
                    duplicate_folder / new_name
                )

                if not destination.exists():
                    break

                counter += 1

        shutil.move(
            str(dup),
            str(destination)
        )

        moved += 1

    except Exception:

        pass

print(
    f"Total Duplicates Found : {len(duplicates)}"
)

print(
    f"Moved To Duplicate_Files : {moved}"
)

print(
    f"Report Saved : {report_file}"
)