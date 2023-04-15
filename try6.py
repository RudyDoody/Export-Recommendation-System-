import sqlite3

# connect to database
conn = sqlite3.connect('india_trade.db')
c = conn.cursor()

# function to classify investment value into low, medium, or high categories
def classify_investment(investment_value):
    if investment_value < 500000:
        return 'low'
    elif 500000 <= investment_value < 1000000:
        return 'medium'
    else:
        return 'high'

# function to recommend a commodity based on investment value and table (exports/imports)
def recommend_commodity(investment_value, table):
    category = classify_investment(investment_value)
    if category == 'low':
        c.execute(f'SELECT commodity FROM {table} ORDER BY value DESC LIMIT 1')
    elif category == 'medium':
        c.execute(f'SELECT commodity FROM {table} WHERE value > 5 ORDER BY value DESC LIMIT 1')
    else:
        c.execute(f'SELECT commodity FROM {table} WHERE value > 10 ORDER BY value DESC LIMIT 1')
    result = c.fetchone()
    return result[0]

# get user input for investment value
investment_value = float(input("Enter your investment value: "))

# recommend commodity for import and export
recommended_import = recommend_commodity(investment_value, 'imports')
recommended_export = recommend_commodity(investment_value, 'exports')

# print recommendations
print(f"For an investment value of {investment_value}, we recommend importing {recommended_import} and exporting {recommended_export}.")