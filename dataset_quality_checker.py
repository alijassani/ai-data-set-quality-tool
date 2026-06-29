import csv

def check_dataset(file_path):
    total_rows = 0
    missing_labels = 0
    duplicate_rows = 0
    seen_rows = set()

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_rows += 1
            row_tuple = tuple(row.items())

            if row_tuple in seen_rows:
                duplicate_rows += 1
            else:
                seen_rows.add(row_tuple)

            if not row.get("label"):
                missing_labels += 1

    print("Dataset Quality Report")
    print("----------------------")
    print(f"Total rows: {total_rows}")
    print(f"Missing labels: {missing_labels}")
    print(f"Duplicate rows: {duplicate_rows}")

check_dataset("sample_dataset.csv")
