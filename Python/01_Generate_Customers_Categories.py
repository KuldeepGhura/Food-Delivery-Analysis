from faker import Faker
import random

fake = Faker("en_IN")

with open("Insert_Data.sql", "w") as file:
    for i in range(500):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone = "9" + "".join(str(random.randint(0, 9)) for _ in range(9))
        city = fake.city()
        state = fake.state()
        join_date = fake.date_between(start_date="-2y", end_date="today")

        sql = f"""INSERT INTO Customers(First_Name, Last_Name, Email, Phone, City, State, Join_Date)
            VALUES
            ('{first_name}', '{last_name}', '{email}', '{phone}', '{city}', '{state}', '{join_date}');"""

        file.write(sql)


print("SQL file created successfully!")

categories = [
    "Electronics",
    "Fashion",
    "Home & Kitchen",
    "Books",
    "Beauty",
    "Sports",
    "Toys",
    "Groceries",
    "Furniture",
    "Automotive",
    "Health",
    "Jewellery",
    "Footwear",
    "Stationery",
    "Pet Supplies"
]

with open("Insert_Data.sql", "a") as file:
    file.write("\n\n-- Categories\n\n")

    for category in categories:
        sql = f"""INSERT INTO Categories (Category_Name)
VALUES ('{category}');

"""
        file.write(sql)

print("Categories generated successfully!")