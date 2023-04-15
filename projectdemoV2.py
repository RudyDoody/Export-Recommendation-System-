import sqlite3
# MAKE FAQ SECTION
# Connect to the database
conn = sqlite3.connect('india_trade.db')
c = conn.cursor()
print(" Hello! Welcome to our state of the line Import/Export Recommendation System!\n If you have any doubts or queries about us and our work, please visit our FAQ's section. ")
while True:
    # Ask the user if they want to access the FAQ section
    faq_choice = input("Do you want to access the FAQ section? (y/n) ")
    
    # If the user chooses to access the FAQ section, display it and ask if they want to continue with the program
    if faq_choice.lower() == "y":
        print("Welcome to the FAQ section!")
        print("Let us start with Explaining what our program is actually about!\n\nThe Import/Export Recommendation System is a program designed for organisations,co-operations and even individuals looking for a place to start in the field of import/export and get some guidance from our program!")
        print("Q: What if I don't have any previous experience in this field?")
        print("A: This program is designed to...")
        print("Q: What are all the input options? Please explain them briefly.")
        print("A: This program is designed to...")
        print("Q: What if I have some options/preferences that i want to factor in for my recommendation?")
        print("A: This program is designed to...")
        
        continue_choice = input("Do you want to continue with the program? (y/n) ")
        if continue_choice.lower() != "y":
            # If the user doesn't want to continue with the program, break out of the while loop and exit
            print("Thank you for using this program.")
        break
    
    # If the user chooses not to access the FAQ section or chooses to continue with the program after accessing it, display the main menu
    else:
        print("Welcome to the main program!")

#Experiences
Experience=input("Have you had any previous experience in the export industry ? (Y/N): ")
Experience=Experience.lower()
if Experience =='Y':
    print("Great! Please specify which commodity you have had experience handling\nIt will help us in aiding you properly!:\n ")
    print("1.Petroleum Products")
    print("2.Gemstones & Precious Metals")
    print("3.Drugs Formulation, Biologicals")
    print("4.Cotton Yarn/Fabrics/Made-ups, Textile Products etc.")
    print("5.Electronic Goods")
    print("6.Food, Spices & Dairy Products")
    
    choice=input('Enter choice(1/2/3/4/5/6): ')
    if choice == '1':
        print("1.Petroleum Products")
        print('Thankyou for your input! Please continue.')
    elif choice == '2':
        print("2.Gemstones & Precious Metals")
        print('Thankyou for your input! Please continue.')
    elif choice == '3':
        print("3.Drugs Formulation, Biologicals")
        print('Thankyou for your input! Please continue.')
    elif choice == '4':
        print("4.Cotton Yarn/Fabrics/Made-ups, Textile Products etc.")
        print('Thankyou for your input! Please continue.')
    elif choice == '5':
        print("5.Electronic Goods")
        print('Thankyou for your input! Please continue.')
    elif choice == '6':
        print("6.Food, Spices & Dairy Products")
        print('Thankyou for your input! Please continue.')

elif Experience == 'N':
    print("No worries! We will still be able to provide you with our services. ")
else:
     print("Invalid input. Please enter 'Y' or 'N'.")

#Preferences
print("1.Petroleum Products")
print("2.Gemstones & Precious Metals")
print("3.Drugs Formulation, Biologicals")
print("4.Cotton Yarn/Fabrics/Made-ups, Textile Products etc.")
print("5.Electronic Goods")
print("6.Food, Spices & Dairy Products")
choice=input('Enter Preferences(1/2/3/4/5/6): ')
if choice == '1':
        print("1.Petroleum Products")
elif choice == '2':
        print("2.Gemstones & Precious Metals")
elif choice == '3':
        print("3.Drugs Formulation, Biologicals")
elif choice == '4':
        print("4.Cotton Yarn/Fabrics/Made-ups, Textile Products etc.")
elif choice == '5':
        print("5.Electronic Goods")
elif choice == '6':
        print("6.Food, Spices & Dairy Products")

# # User location (NOT UTILIZED)
# Location=str(input('Enter the location: '))
# print(Location)

# DATA parts

# EXPORT DATA HERE - FROM DATABASE


exports_data = [('Petroleum Products', 21.20),
                ('Gems & Jewellery', 17.70),
                ('Drug Formulations, Biologicals', 15.70),
                ('Cotton Yarn/Fabrics/Made-ups, Handloom Products etc.', 5.30),
                ('Organic & Inorganic Chemicals', 5.20),
                ('Engineering Goods', 4.40),
                ('Electronic Goods', 3.90),
                ('Rice', 3.60),
                ('Meat, Dairy & Poultry Products', 1.90),
                ('Plastics & Linoleum', 1.80)]

#import_data
imports_data = [('Crude Oil', 61.08),
                ('Natural Gas', 5.61),
                ('Pearls, precious & Semi-precious stones', 3.92),
                ('Electronic Goods', 3.31),
                ('Gold', 2.59),
                ('Petroleum Products', 2.41),
                ('Coal, Coke & Briquettes', 1.83),
                ('Chemicals (Organic/Inorganic)', 1.79),
                ('Iron & Steel', 1.48),
                ('Fertilizers', 1.30)]




# Define the user's capital availability
capital = float(input("Enter your Capital Availability: ")) #ADD TO INPUT

# Export Value Input (og on line 105)
exports= float(input("Enter your export value[Value between 0.01 - 0.99]: "))

# get user input for investment value
investment_value = float(input("Enter your investment value: "))

# import value
imports= float(input("Enter your import value[Value between 0.01 - 0.99]: "))

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

#Exports data (input og here)

# Calculate the total export value
total_export_value = sum([item[1] for item in exports_data])

# Categorize the export data into high, moderate, and low values using if/else statements
high_value_exports = []
moderate_value_exports = []
low_value_exports = []

for item in exports_data:
    if item[1]/total_export_value >= 0.10:
        high_value_exports.append(item[0])
    elif item[1]/total_export_value >= 0.05:
        moderate_value_exports.append(item[0])
    else:
        low_value_exports.append(item[0])

# Print the results
print("High value exports: ", high_value_exports)
print("Moderate value exports: ", moderate_value_exports)
print("Low value exports: ", low_value_exports)

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

# # get user input for investment value
# investment_value = float(input("Enter your investment value: "))

# recommend commodity for import and export
recommended_import = recommend_commodity(investment_value, 'imports')
recommended_export = recommend_commodity(investment_value, 'exports')

# print recommendations
print(f"For an investment value of {investment_value}, we recommend importing {recommended_import} and exporting {recommended_export}.")

#import_data


# INPUT import    
# imports= float(input("Enter your import value[Value between 0.01 - 0.99]: ")) 

# Calculate the total export value
total_import_value = sum([item[1] for item in imports_data])

# Categorize the export data into high, moderate, and low values using if/else statements
high_value_imports = []
moderate_value_imports = []
low_value_imports = []

for item in imports_data:
    if item[1]/total_import_value >= 0.10:
        high_value_imports.append(item[0])
    elif item[1]/total_import_value >= 0.05:
        moderate_value_imports.append(item[0])
    else:
        low_value_imports.append(item[0])

# Print the results
#print("High value exports: ", high_value_imports)
#print("Moderate value exports: ", moderate_value_imports)
#print("Low value exports: ", low_value_imports)

# Print the results based on the user's input value
if 0.05 < float(imports) <= 0.1: 
    print("Low value imports: ", low_value_imports)
elif float(imports) <= 0.05:
    print("Moderate value imports: ", moderate_value_imports)
else:
    print("High value imports: ", high_value_imports)
    
# TRADING PARTNERS
# TRADING PARTNERS DATA

trading_partners_data = [('United States', 15.87, 9.71),
                        ('United Arab Emirates', 11.62, 14.21),
                        ('China', 10.85, 78.44),
                        ('Hong Kong', 5.70, 1.72),
                        ('Singapore', 5.38, 3.20),
                        ('United Kingdom', 3.76, 2.66),
                        ('Netherlands', 3.53, 3.55),
                        ('Germany', 3.15, 8.20),
                        ('Bangladesh', 2.95, 0.81),
                        ('Vietnam', 2.71, 1.61)]


# calculate the total trade volume for each partner
trade_volume_data = [(partner[0], partner[1]+partner[2]) for partner in trading_partners_data]

# sort the data by total trade volume in descending order
sorted_trade_volume_data = sorted(trade_volume_data, key=lambda x: x[1], reverse=True)

# print the top trading partner recommendation for import and export
print("Top trading partners recommendation for import and export in India:")
print(f"1. For Import: {sorted_trade_volume_data[0][0]}")
print(f"2. For Export: {sorted_trade_volume_data[1][0]}")    


# BEAUTIFY OUTPUT