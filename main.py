print("========================================")
print("              DATACLEAN")
print("      Simple Data Quality Checker")
print("========================================")


# ========================================
# GET DATASET
# ========================================

column_count = int(input("\nEnter number of columns: "))

columns = []

print("\nEnter column names:")

for i in range(column_count):

    column_name = input(f"Column {i + 1}: ")

    columns.append(column_name)


# Get number of records

record_count = int(input("\nEnter number of records: "))

records = []

print("\nEnter your data:")

for i in range(record_count):

    print(f"\nRecord {i + 1}")

    record = []

    for column in columns:

        value = input(f"{column}: ")

        record.append(value)

    records.append(record)


# ========================================
# ANALYZE DATA
# ========================================

print("\n\n========================================")
print("          DATA QUALITY REPORT")
print("========================================")


print("\nDataset Information")
print("----------------------------------------")

print("Total Records :", len(records))
print("Total Columns :", len(columns))


# ========================================
# FIND MISSING VALUES
# ========================================

print("\nMissing Values")
print("----------------------------------------")

total_missing = 0

for i in range(len(columns)):

    missing_count = 0

    for record in records:

        if record[i].strip() == "":

            missing_count += 1

    print(columns[i], ":", missing_count)

    total_missing += missing_count


# ========================================
# FIND DUPLICATES
# ========================================

duplicate_count = 0

checked_records = []

for record in records:

    if record in checked_records:

        duplicate_count += 1

    else:

        checked_records.append(record)


print("\nDuplicate Records")
print("----------------------------------------")

print("Duplicate Records :", duplicate_count)


# ========================================
# REMOVE DUPLICATES
# ========================================

if duplicate_count > 0:

    print("\nDuplicate records were found.")

    choice = input(
        "Do you want to remove duplicates? (yes/no): "
    ).lower()

    if choice == "yes":

        records = checked_records

        duplicate_count = 0

        print("\nDuplicate records removed successfully.")

    else:

        print("\nDuplicate records were not removed.")

else:

    print("\nNo duplicate records found.")


# ========================================
# FINAL STATUS
# ========================================

print("\nData Quality Status")
print("----------------------------------------")

if total_missing == 0 and duplicate_count == 0:

    print("Dataset is clean.")

else:

    print("Dataset needs cleaning.")


print("\n========================================")
print("             END OF REPORT")
print("========================================")