CountryDB={}
while True:
    print(" 1. Insert")
    print(" 2. Show Country")
    print(" 3. Show all Capital")
    print(" 4. Get country")
    print(" 5. Delete")
    print(" 6. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        country=input("Enter country name:")
        capital=input("Enter capital name:")
        CountryDB[country]=capital
        print(CountryDB)  

    elif choice==2:
        for i in CountryDB.keys():
            print(i)
    elif choice==3:
        for i in CountryDB.values():
            print(i)
    elif choice==4:
        countryP=input("Enter country name:")
        if countryP in CountryDB.keys():
            print("Capital is:",CountryDB[countryP])
        else:
            print("Country not found.")
    elif choice==5: 
        country=input("Enter country name to delete:")
        if country in CountryDB.keys():
            del CountryDB[country]
            print("Country deleted.")
        else:
            print("country not found.")
    elif choice==6:
        print("Exiting...")
        break
