import sqlite3

# Connect to the database
conn = sqlite3.connect('india_trade.db')

# Define the user's capital availability
capital = float(input("Enter your capital availability: "))

# Define the SQL query to retrieve data based on the user's capital availability
if capital <= 10000:
    sql = "SELECT commodity FROM exports WHERE value <= 5"
elif capital <= 50000:
    sql = "SELECT commodity FROM exports WHERE value > 5 AND value <= 10"
else:
    sql = "SELECT commodity FROM exports WHERE value > 10"

# Execute the SQL query and retrieve the data
result_set = conn.execute(sql)
result_list = [result[0] for result in result_set]

# Recommend a commodity based on the retrieved data
if len(result_list) > 0:
    print("Based on your capital availability, the following commodities are recommended:")
    for commodity in result_list:
        print(commodity)
else:
    print("No commodities were found that match your capital availability.")
