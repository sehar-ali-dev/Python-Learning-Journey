import hashlib
from pathlib import Path

# User folders

home = Path.home()

folders_to_scan = [
    home / "Downloads",
    home / "Documents",
    home / "Desktop"
]

# Store hashes and duplicates

file_hashes = {}
duplicates = []


# Function to calculate file hash

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


print("Scanning for duplicates...\n")

# Scan folders

for folder in folders_to_scan:

    if not folder.exists():
        continue

    for file in folder.rglob("*"):

        if not file.is_file():
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


# Create report

report_file = "duplicate_report.txt"

with open(report_file, "w", encoding="utf-8") as report:

    report.write("DUPLICATE FILE REPORT\n")
    report.write("=" * 60 + "\n\n")

    if duplicates:

        for i, (dup, original) in enumerate(
            duplicates,
            start=1
        ):

            report.write(f"{i}\n")
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
            "No duplicates found.\n"
        )

print(f"Report created: {report_file}")

# Ask before deleting

if duplicates:

    choice = input(
        "\nDelete duplicate files? (y/n): "
    ).lower()

    if choice == "y":

        deleted = 0

        for dup, original in duplicates:

            try:

                Path(dup).unlink()

                print(
                    f"Deleted: {dup}"
                )

                deleted += 1

            except Exception:

                print(
                    f"Could not delete: {dup}"
                )

        print(
            f"\nTotal deleted: {deleted}"
        )

    else:

        print(
            "\nNo files deleted."
        )

else:

    print(
        "\nNo duplicate files found."
    )