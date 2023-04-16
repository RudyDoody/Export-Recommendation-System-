import sqlite3
# Connection to the database
conn = sqlite3.connect('india_trade.db')
c = conn.cursor()

print(" Hello! Welcome to our state of the line Import/Export Recommendation System!\n If you have any doubts or queries about us and our work, please visit our FAQ's section. ")
while True:
    # Ask the user if they want to access the FAQ section
    faq_choice = input("Do you want to access the FAQ section? (y/n) ").lower()
    
    # If the user chooses to access the FAQ section, display it and ask if they want to continue with the program
    if faq_choice == "y":
        print("Welcome to the FAQ section!")
        print("Let us start with Explaining what our program is actually about!\n\nThe Import/Export Recommendation System is a program designed for organizations,co-operations and even individuals looking for a place to start in the field of import/export and get some guidance from our program!")
        print('We provide our recommendations by taking into account your availabilities(explained later on), and matching them against the current market trends, profitability adn other factors!')
        print('')
        print("Q.1: What if I don't have any previous experience in this field?")
        print("A: This program is designed to provide you with an ideal product and/or field nonetheless of you having any experience or not.")
        print('')
        print("Q.2: What are all the input options? Please explain them briefly.")
        print("A: Of-course! The input details that we require from you will be :")
        print('1.Capital availability - The amount of capital you will be willing/able to employ.')
        print('2.Import Value - How much percentage of the product would you actually wish to import.')
        print('3.Export Value - How much percentage of the product would you actually wish to export.')
        print('4.Investment value - The amount of money you would invest in any form such as capital,equity,shares etc ')
        print('')
        print("Q.3: What if I have some options/preferences that i want to factor in for my recommendation?")
        print("A: This program is designed to also factor in your personal choices and history to provide you with the best possible output!")
        
        continue_choice = input("Do you want to continue with the faq? (y/n) ")
        if continue_choice.lower() != "y":
            # If the user doesn't want to continue with the program, break out of the while loop and exit
            print("Thank you for using the faq's.")
            break
        elif continue_choice=='y':
            faq_choice = input("Do you want to access the FAQ section? (y/n) ").lower()
    
    # If the user chooses not to access the FAQ section or chooses to continue with the program after accessing it, display the main menu
    elif faq_choice=='n':
     print("Welcome to the main program then!")
     break
#Experiences
Experience=input("Have you had any previous experience in the export industry ? (y/n): ").lower()
Experience==Experience.lower()
if Experience =='y':
    print("Great! Please specify which commodity you have had experience handling\nIt will help us in aiding you properly!:\n ")
    print("1.Petroleum Products")
    print("2.Gemstones & Precious Metals")
    print("3.Drugs Formulation, Biologicals")
    print("4.Cotton Yarn/Fabrics/Made-ups, Textile Products etc.")
    print("5.Electronic Goods")
    print("6.Food, Spices & Dairy Products")
    
    exp_choice=input('Enter choice(1/2/3/4/5/6): ')
    if exp_choice == '1':
        print("1.Petroleum Products")
        print('Thankyou for your input! Please continue.')
    elif exp_choice == '2':
        print("2.Gemstones & Precious Metals")
        print('Thankyou for your input! Please continue.')
    elif exp_choice == '3':
        print("3.Drugs Formulation, Biologicals")
        print('Thankyou for your input! Please continue.')
    elif exp_choice == '4':
        print("4.Cotton Yarn/Fabrics/Made-ups, Textile Products etc.")
        print('Thankyou for your input! Please continue.')
    elif exp_choice == '5':
        print("5.Electronic Goods")
        print('Thankyou for your input! Please continue.')
    elif exp_choice == '6':
        print("6.Food, Spices & Dairy Products")
        print('Thankyou for your input! Please continue.')

elif Experience == 'N':
    print("No worries! We will still be able to provide you with our services. ")
else:
     print("Invalid input. Please enter 'Y' or 'N'.")
     
print('')
print('')
print('Please select your preference of commodity:')
print('')
#Preferences
print("1.Petroleum Products")
print("2.Gemstones & Precious Metals")
print("3.Drugs Formulation, Biologicals")
print("4.Cotton Yarn/Fabrics/Made-ups, Textile Products etc.")
print("5.Electronic Goods")
print("6.Food, Spices & Dairy Products")
pref_choice = input('Enter Preferences(1/2/3/4/5/6): ')

if pref_choice == '1':
        print("1.Petroleum Products")
elif pref_choice == '2':
        print("2.Gemstones & Precious Metals")
elif pref_choice == '3':
        print("3.Drugs Formulation, Biologicals")
elif pref_choice == '4':
        print("4.Cotton Yarn/Fabrics/Made-ups, Textile Products etc.")
elif pref_choice == '5':
        print("5.Electronic Goods")
elif pref_choice == '6':
        print("6.Food, Spices & Dairy Products")
print('')

# DATA tables - also in database
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

#import_data  - FROM DATABASE
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

# Define the user's capital availability
capital = float(input("Enter your Capital Availability: ")) #ADD TO INPUT

# Export Value Input (og on line 105)
exports= float(input("Enter your export value[Value between 0.01 - 0.99]: "))

# get user input for investment value
investment_value = float(input("Enter your investment value: "))

# import value
imports= float(input("Enter your import value[Value between 0.01 - 0.99]: "))

#retrieve data based on the user's capital availability
if capital <= 10000:
    sql = "SELECT commodity FROM exports WHERE value <= 5"
elif capital <= 50000:
    sql = "SELECT commodity FROM exports WHERE value > 5 AND value <= 10"
else:
    sql = "SELECT commodity FROM exports WHERE value > 10"

# Execute the SQL query and retrieve the data
result_set = conn.execute(sql)
result_list = [result[0] for result in result_set]

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

# recommend commodity for import and export
recommended_import = recommend_commodity(investment_value, 'imports')
recommended_export = recommend_commodity(investment_value, 'exports')

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

# calculate the total trade volume for each partner
trade_volume_data = [(partner[0], partner[1]+partner[2]) for partner in trading_partners_data]

# sort the data by total trade volume in descending order
sorted_trade_volume_data = sorted(trade_volume_data, key=lambda x: x[1], reverse=True)

#ENDING PART

print('Thankyou for your patience! Your input will now be processed to provide you with the most appropriate recommendations for you and your business.')
print("")
print('Firstly, we would like to present you with recommendations that would result in the best possible utilization of your money accounting in your available parameters:')
print('')
print('1. The Recommended Commodity according to your Capital availability:')
# Recommend a commodity based on the retrieved data
if len(result_list) > 0:
    print("Based on your capital availability, the following commodities are recommended:")
    for commodity in result_list:
        print(commodity)
else:
    print("No commodities were found that match your capital availability.")
print('')
print('2. The Ideal Commodity and Field for you to invest into according to your Investment Value:')
print('')
print(f"For an investment value of {investment_value}, we recommend importing {recommended_import} \n And exporting {recommended_export}.")
print('')
print('3. The Recommended commodity for you to export:')
print('')
if 0.05 < float(exports) <= 0.1: 
    print("Low value exports: ", low_value_exports)
elif float(exports) <= 0.05:
    print("Moderate value exports: ", moderate_value_exports)
else:
    print("High value exports: ", high_value_exports)
print('')
print('4.The Import Recommendation for you:')
print('')
# Print the results based on the user's input value
if 0.05 < float(imports) <= 0.1: 
    print("Low value imports: ", low_value_imports)
elif float(imports) <= 0.05:
    print("Moderate value imports: ", moderate_value_imports)
else:
    print("High value imports: ", high_value_imports)  
  
print('')
print("5.Top trading partners recommendation for import and export in India:")
print('')
print(f"1. For Import: {sorted_trade_volume_data[0][0]}")
print(f"2. For Export: {sorted_trade_volume_data[1][0]}")
print('')
print('')
print('Now, we know that these commodities and fields may be the ideal for you to invest your resources in,\n but we understand that factors like your previous experiences and preferences potentially play a determining role in your ease of business and comfort of life.')    
print('So, taking this into account we would like to present another set of recommendations based on personal subjective factors!')
print('Do keep in note that these commodities may not be the most ideal for profitability and growth of revenue,\n but may be easier for you to carry out personally and may provide mental peace even :) ')
print('')
print('Commodity field for import/export based on personal factors: ')

print('This is the commodity and field you should focus on based on your preference: ')
if pref_choice == '1':
        print("1.Petroleum Products")
elif pref_choice == '2':
        print("2.Gemstones & Precious Metals")
elif pref_choice == '3':
        print("3.Drugs Formulation, Biologicals")
elif pref_choice == '4':
        print("4.Cotton Yarn/Fabrics/Made-ups, Textile Products etc.")
elif pref_choice == '5':
        print("5.Electronic Goods")
elif pref_choice == '6':
        print("6.Food, Spices & Dairy Products")
        
print('')
print('This is the commodity and field you should focus on based on your past experiences in the industry: ')
if exp_choice == '1':
        print("1.Petroleum Products")        
elif exp_choice == '2':
        print("2.Gemstones & Precious Metals")        
elif exp_choice == '3':
        print("3.Drugs Formulation, Biologicals")
elif exp_choice == '4':
        print("4.Cotton Yarn/Fabrics/Made-ups, Textile Products etc.")
elif exp_choice == '5':
        print("5.Electronic Goods")
elif exp_choice == '6':
        print("6.Food, Spices & Dairy Products")
print('')
print('We recommend the same trading partners as earlier, since they will be the most profitable according to research and trends.')
print('')
print("Top trading partners recommendation for import and export in India:")
print('')
print(f"1. For Import: {sorted_trade_volume_data[0][0]}")
print(f"2. For Export: {sorted_trade_volume_data[1][0]}")
print("")
print('Thankyou for utilizing our program we hope that our program has helped you in determining what commodity you should prioritize for your business.')
print('Hope to see you again!!')
#THE END.