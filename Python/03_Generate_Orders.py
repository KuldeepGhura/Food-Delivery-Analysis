from faker import Faker
import random

fake = Faker("en_IN")

with open("02_Insert_Data.sql", "a") as file:
    file.write("\n\n-- Orders\n\n")

    payment_methods = ["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash on Delivery"]
    order_status = ["Delivered", "Cancelled", "Returned", "Shipped", "Processing"]

    for i in range(2000):

        customer_id = random.randint(1, 500)

        order_date = fake.date_between(start_date="-2y", end_date="today")

        payment = random.choice(payment_methods)

        status = random.choice(order_status)

        total_amount = random.randint(500, 25000)

        sql = f"""INSERT INTO Orders
(Customer_ID, Order_Date, Total_Amount, Payment_Method, Order_Status)
VALUES
({customer_id}, '{order_date}', {total_amount}, '{payment}', '{status}');

"""

        file.write(sql)

print("Orders generated successfully!")

with open("02_Insert_Data.sql", "a") as file:
    file.write("\n\n-- OrderDetails\n\n")

    for i in range(5000):

        order_id = random.randint(1, 2000)

        product_id = random.randint(1, 200)

        quantity = random.randint(1, 5)

        price = random.randint(300, 5000)

        sql = f"""INSERT INTO OrderDetails
(Order_ID, Product_ID, Quantity, Price)
VALUES
({order_id}, {product_id}, {quantity}, {price});

"""

        file.write(sql)

print("OrderDetails generated successfully!")

reasons = [
    "Damaged Product",
    "Wrong Item",
    "Late Delivery",
    "Customer Changed Mind",
    "Defective Product"
]

with open("02_Insert_Data.sql", "a") as file:
    file.write("\n\n-- Returns\n\n")

    used_orders = random.sample(range(1, 2001), 150)

    for order_id in used_orders:

        return_date = fake.date_between(start_date="-1y", end_date="today")

        reason = random.choice(reasons)

        sql = f"""INSERT INTO Returns
(Order_ID, Return_Date, Return_Reason)
VALUES
({order_id}, '{return_date}', '{reason}');

"""

        file.write(sql)

print("Returns generated successfully!")