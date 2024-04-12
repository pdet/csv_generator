from faker import Faker
import random

# Create a Faker generator
fake = Faker()

# Seed the Faker instance
fake.seed_instance(12345)


random.seed(12345)

# Define the path for the CSV file
csv_file_path = 'yellow_book.csv'

header = b'name,address,birth_year,pets\n'

invalid_utf8_bytes = b'1,2,"pedro\xff\xff"\n' 

def generate_faker_row(file):
    name = fake.name()
    address = fake.address()
    current_year = 2024
    birth_year = random.randint(current_year - 100, current_year - 18)
    num_pets = random.randint(0, 5)
    formatted_string = f"{name},\"{address}\",{birth_year},{num_pets}\n"
    # UTF-8 because we are not animals.
    string_in_bytes = formatted_string.encode('utf-8')
    file.write(string_in_bytes)

# Open the file in binary write mode
with open(csv_file_path, 'wb') as file:
    file.write(header)
    # Lets pretend the first 100k lines are all beautiful
    for _ in range(100000):
        generate_faker_row(file)
    # Generate more 100000 rows but insert a random error every 100 rows
    for _ in range(100000):
        generate_faker_row(file)
    