import csv
from faker import Faker

# Set up Faker
fake = Faker()

# Generate 20 random names
random_names = [fake.name() for _ in range(10)]

# Specify the CSV file path
csv_file_path = "c:/diplomas/random_names.csv"

# Write the names to the CSV file
with open(csv_file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows([[name] for name in random_names])

print(f"CSV file with random names created at: {csv_file_path}")
