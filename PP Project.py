#Experiences
Exp=input("Have you had any previous experience in the export industry ? (Yes/No): ")
if Exp =='Yes':
    print("Great! Please specify which commodity you have had experience handling: ")
    print("1.Petroleum Products")
    print("2.Gemstones & Precious Metals")
    print("3.Drugs Formulation, Biologicals")
    print("4.Cotton Yarn/Fabrics/Made-ups, Textile Products etc.")
    print("5.Electronic Goods")
    print("6.Food, Spices & Dairy Products")
    
    choice=input('Enter choice(1/2/3/4/5/6): ')
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

elif Exp == 'NO':
    print("No worries! ")
else:
     print("Invalid input. Please enter 'Yes' or 'No'.")
    
#Capital Availability
CAPAV=int(input('Enter your Capital Availability: '))
print(CAPAV)

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

#User location
Location=str(input('Enter the location: '))
print(Location)

