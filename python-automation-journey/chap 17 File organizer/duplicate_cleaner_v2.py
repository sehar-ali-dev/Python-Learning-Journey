# =====================================================
# Duplicate Cleaner v2
# Scan Downloads folder only
# Create report
# Ask confirmation before deleting
# Safe duplicate removal
# =====================================================

import hashlib
from pathlib import Path

# -----------------------------------------------------
# Downloads folder only
# -----------------------------------------------------

home = Path.home()

folders_to_scan = [
    home / "Downloads"
]

# -----------------------------------------------------
# Ignore folders
# -----------------------------------------------------

IGNORE_FOLDERS = {
    "Microsoft VS Code",
    "VS Code",
    ".git",
    "__pycache__",
    "node_modules"
}

# -----------------------------------------------------
# Store hashes and duplicates
# -----------------------------------------------------

file_hashes = {}
duplicates = []

# -----------------------------------------------------
# Calculate file hash (MD5)
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


print("Duplicate Cleaner v2 Started...\n")

# -----------------------------------------------------
# Scan files
# -----------------------------------------------------

for folder in folders_to_scan:

    if not folder.exists():
        continue

    for file in folder.rglob("*"):

        # Skip non-files
        if not file.is_file():
            continue

        # Skip ignored folders
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
                (str(file), file_hashes[file_hash])
            )

        else:

            file_hashes[file_hash] = str(file)

# -----------------------------------------------------
# Create report
# -----------------------------------------------------

report_file = "Duplicate Cleaner v2.txt"

with open(report_file, "w", encoding="utf-8") as report:

    report.write("DUPLICATE CLEANER V2 REPORT\n")
    report.write("=" * 60 + "\n\n")

    if duplicates:

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
                f"Duplicate: {dup}\n"
            )
            report.write(
                "Action   : Pending\n\n"
            )

    else:

        report.write(
            "No duplicate files found.\n"
        )

print(f"Report created: {report_file}")

# -----------------------------------------------------
# Ask before deleting
# -----------------------------------------------------

if duplicates:

    print(
        f"\nDuplicates Found: {len(duplicates)}"
    )

    choice = input(
        "\nDelete duplicate files? (y/n): "
    ).lower()

    if choice == "y":

        deleted = 0

        delete_log = open(
            "deleted_duplicates_log.txt",
            "w",
            encoding="utf-8"
        )

        for dup, original in duplicates:

            try:

                Path(dup).unlink()

                delete_log.write(
                    f"DELETED : {dup}\n"
                )

                print(
                    f"Deleted: {dup}"
                )

                deleted += 1

            except Exception:

                delete_log.write(
                    f"FAILED : {dup}\n"
                )

        delete_log.close()

        print(
            f"\nTotal Deleted: {deleted}"
        )

        print(
            "Delete log saved as: deleted_duplicates_log.txt"
        )

    else:

        print(
            "\nNo files deleted."
        )

else:

    print(
        "\nNo duplicate files found."
    )