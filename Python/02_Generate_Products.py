from faker import Faker
import random

fake = Faker("en_IN")

brands = [
    "Samsung","Apple","Sony","HP","Dell",
    "Nike","Adidas","Puma","Boat","LG",
    "Philips","Lenovo","Mi","Realme","Titan"
]

with open("Insert_Data.sql", "a") as file:
    file.write("\n\n-- Products\n\n")

    for i in range(200):

        product_name = fake.word().capitalize() + " " + random.choice(
            ["Phone","Laptop","Shoes","Watch","Headphones","Bag","Chair","Bottle"]
        )

        category_id = random.randint(1,15)

        brand = random.choice(brands)

        cost = random.randint(300,5000)

        selling = cost + random.randint(100,2000)

        stock = random.randint(10,300)

        sql = f"""INSERT INTO Products
(Product_Name,Category_ID,Brand,Selling_Price,Cost_Price,Stock)
VALUES
('{product_name}',{category_id},'{brand}',{selling},{cost},{stock});

"""

        file.write(sql)

print("Products generated!")