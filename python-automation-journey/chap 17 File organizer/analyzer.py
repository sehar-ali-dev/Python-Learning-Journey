# os = folders aur files access karne ke liye
import os

# pathlib = modern path handling ke liye
from pathlib import Path

# hashlib = duplicate files detect karne ke liye
import hashlib

# User ka home folder hasil karna
home = Path.home()

# Jin folders ko scan karna hai
folders_to_scan = [
    home / "Downloads",
    home / "Documents",
    home / "Desktop"
]

# File types count store karne ke liye
file_types = {}

# Large files store karne ke liye
large_files = []

# Duplicate detection ke liye
file_hashes = {}

# Duplicate files list
duplicates = []


# File ka hash calculate karne wala function
def get_file_hash(filepath):

    # MD5 hash object banana
    md5 = hashlib.md5()

    try:
        with open(filepath, "rb") as f:

            # File ko chunks mein read karna
            while chunk := f.read(4096):
                md5.update(chunk)

        return md5.hexdigest()

    except Exception:
        return None


print("Scanning started...\n")

# Har folder scan karna
for folder in folders_to_scan:

    if not folder.exists():
        continue

    # Folder ke andar recursively scan karna
    for root, dirs, files in os.walk(folder):

        for file in files:

            filepath = Path(root) / file

            try:

                # File extension nikalna
                ext = filepath.suffix.lower()

                if ext == "":
                    ext = "NO_EXTENSION"

                # File type count karna
                file_types[ext] = file_types.get(ext, 0) + 1

                # File size MB mein
                size_mb = filepath.stat().st_size / (1024 * 1024)

                # Agar file 100MB se bari ho
                if size_mb >= 100:
                    large_files.append(
                        (str(filepath), round(size_mb, 2))
                    )

                # Duplicate detection
                file_hash = get_file_hash(filepath)

                if file_hash:

                    if file_hash in file_hashes:

                        duplicates.append(
                            (str(filepath),
                             file_hashes[file_hash])
                        )

                    else:
                        file_hashes[file_hash] = str(filepath)

            except Exception:
                pass


# Report file create karna
report_file = "file_report.txt"

with open(report_file, "w", encoding="utf-8") as report:

    report.write("FILE ANALYSIS REPORT\n")
    report.write("=" * 60 + "\n\n")

    # File types section
    report.write("FILE TYPES\n")
    report.write("-" * 40 + "\n")

    for ext, count in sorted(file_types.items()):
        report.write(f"{ext} : {count}\n")

    report.write("\n\n")

    # Large files section
    report.write("LARGE FILES (100MB+)\n")
    report.write("-" * 40 + "\n")

    if large_files:
        for path, size in large_files:
            report.write(f"{size} MB -> {path}\n")
    else:
        report.write("No large files found.\n")

    report.write("\n\n")

    # Duplicate files section
    report.write("DUPLICATE FILES\n")
    report.write("-" * 40 + "\n")

    if duplicates:
        for dup, original in duplicates:
            report.write(f"\nDuplicate: {dup}\n")
            report.write(f"Original : {original}\n")
    else:
        report.write("No duplicates found.\n")

    report.write("\n\n")

    # Folder suggestions
    report.write("SUGGESTED FOLDER STRUCTURE\n")
    report.write("-" * 40 + "\n")

    report.write("PDFs\n")
    report.write("Images\n")
    report.write("Videos\n")
    report.write("ZIP_Files\n")
    report.write("Software\n")
    report.write("Assignments\n")
    report.write("Python_Projects\n")
    report.write("Certificates\n")

print("\nScanning completed.")
print(f"Report saved as: {report_file}")