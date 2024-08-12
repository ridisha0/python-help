# Title of the application
print("-------------------------------------------------------------------")
print("*******************************************************************")
print("                 Welcome to BRJ Furnitures            ")
print("*******************************************************************")
print("-------------------------------------------------------------------")

def get_files():
    with open("database.txt", "r") as file:
        return file.readlines()

def data_dict(fileContent):
    data = {}
    for index, line in enumerate(fileContent):
        data[index + 1] = line.strip().split(",")
    return data

def f_print(mainData):
    print("-------------------------------------------------------------")
    print("SNo", "\t", "Manufacturer", "\t", "Product", "\t\t", "Quantity", "\t", "Price")
    print("-------------------------------------------------------------\n")
    for key, value in mainData.items():
        print(f"{key}\t{value[0]}\t{value[1]}\t{value[2]}\t{value[3]}")
    print("\n-------------------------------------------------------------\n")

def selldata(mainData):
    id_valid = False
    while not id_valid:
        
            ID = int(input("Enter the ID of the product: "))
            if ID in mainData:
                if int(mainData[ID][3]) > 0:
                    id_valid = True
                    return ID
                else:
                    print("\n**************************")
                    print("      Out of Stock!!         ")
                    print("*****************************\n")
            else:
                print("\n**************************")
                print("      Invalid ID!!            ")
                print("*****************************\n")
        

def q_valid_sell(mainData, ID):
    while True:
        try:
            quantity = int(input("Enter the quantity of the product: "))
            if 0 < quantity <= int(mainData[ID][3]):
                return quantity
            else:
                print("\n************************")
                print("Not available.")
                print("*************************\n")
        except ValueError:
            print("Enter a valid quantity.")

def writeFile(mainData):
    with open("database.txt", "w") as file:
        for value in mainData.values():
            file.write(f"{value[0]},{value[1]},{value[2]},{value[3]}\n")

def dateTime():
    from datetime import datetime
    return datetime.now()

def sell_invoice(furnitures):
    fileContent = get_files()
    mainData = data_dict(fileContent)

    name = input("Please enter your Name: ")
    contact = input("Please enter your Contact Number: ")

    print("\n                           INVOICE                                \n")
    print("--------------------------------------------------------------------------")
    print("SNo", "\t", "Manufacturer", "\t", "Product", "\t\t", "Quantity", "\t", "Price")
    print("------------------------------------------------------------------------\n")

    total = 0
    for index, (Id, quantity) in enumerate(furnitures):
        Manufacturer = mainData[Id][0]
        Product = mainData[Id][1]
        Price = int(mainData[Id][2].replace("$", "")) * quantity
        total += Price
        print(f"{index + 1}\t{Manufacturer}\t{Product}\t{quantity}\t{Price}")
        print("\n")

    print("Your Grand Total is: " + str(total))
    print("\nName: " + name)
    print("Phone no.: " + contact)
    print("Sell Date: " + str(dateTime()) + "\n")

    with open(name + ".txt", "w") as j:
        j.write("\n                           INVOICE                              \n")
        j.write("-------------------------------------------------------------\n")
        j.write("SNo\tManufacturer\tProduct\t\tQuantity\tPrice\n")
        j.write("-------------------------------------------------------------\n\n")

        total = 0
        for index, (Id, quantity) in enumerate(furnitures):
            Manufacturer = mainData[Id][0]
            Product = mainData[Id][1]
            Price = int(mainData[Id][2].replace("$", "")) * quantity
            total += Price
            j.write(f"{index + 1}\t{Manufacturer}\t{Product}\t{quantity}\t{Price}\n")
        
        j.write("Grand Total: " + str(total))
        j.write("\nName: " + name + "\n")
        j.write("Phone Number.: " + contact + "\n")
        j.write("Sell Date: " + str(dateTime()) + "\n\n")

        j.write("\n\n**********************************************************************")
        j.write("\n              Thank you. Your purchase has been completed!!        \n")
        j.write("************************************************************************")

def sell():
    print("\n Let's sell furniture. \n")
    
    fileContent = get_files()
    mainData = data_dict(fileContent)

    furnitures = []
    while True:
        f_print(mainData)
        Id = selldata(mainData)
        print("\n****************************")
        print("       available!!  ")
        print("*****************************\n")
        
        quantity = q_valid_sell(mainData, Id)
        mainData[Id][3] = int(mainData[Id][3]) - quantity
        furnitures.append([Id, quantity])

        writeFile(mainData)
        f_print(mainData)
        
        userInput = input("Do you want to rent more costumes? (yes/no) ").strip().lower()
        if userInput == "no":
            break
    
    print()
    f_print(mainData)
    sell_invoice(furnitures)
    print("\n******************************************************")
    print("      Thank you. Your costume has been rented!!         ")
    print("******************************************************\n")

def p_data(mainData):
    while True:
        try:
            ID = int(input("Enter the ID  you want to purchase: "))
            if ID > 0 and ID <= len(mainData):
                return ID
            else:
                print("Invalid ID! Please enter a valid ID.")
        except ValueError:
            print("Please enter a valid number.")

def quantity_valid_p(mainData, ID):
    while True:
        try:
            quantity = int(input("quantity u want to purchase? "))
            if quantity > 0:
                if quantity <= int(mainData[ID][3]):
                    return quantity
                else:
                    print("Not enough stock available!")
            else:
                print("Invalid quantity! It must be a positive number.")
        except ValueError:
            print("Please enter a valid number.")

def p_invoice(furnitures):
    fileContent = get_files()
    mainData = data_dict(fileContent)

    name = input("Please enter your name: ")
    contact = input("Please enter your contact number: ")
    
    shipping_option = input("Do you want the furniture to be shipped? (Y/N): ").upper()
    shipping_cost = 15 if shipping_option == "Y" else 0

    print()
    print("\n                            INVOICE                                 ")
    print("\n" + "Name: " + name)
    print("Phone Number: " + contact)
    print("Purchase Date: " + str(dateTime()))
    print("Shipping Cost: $" + str(shipping_cost) + "\n")
        
    print("-------------------------------------------------------------")
    print("SNo", "\t", "Manufacturer", "\t", "Product", "\t\t", "Quantity", "\t", "Price")
    print("-------------------------------------------------------------\n")

    totalQuantity = 0
    totalPrice = 0
    for index, (Id, quantity) in enumerate(furnitures):
        Name = mainData[Id][0]
        Product = mainData[Id][1]
        Price = int(mainData[Id][2].replace("$", "")) * quantity
        totalQuantity += quantity
        totalPrice += Price

        print(f"{index + 1}\t{Name}\t{Product}\t{quantity}\t${Price}")
        print("\n")

    print("Total Price: $" + str(totalPrice))
    print("Shipping Cost: $" + str(shipping_cost))
    print("Grand Total: $" + str(totalPrice + shipping_cost) + "\n")

    with open(name + ".txt", "w") as j:
        j.write("\n                           INVOICE                                \n")
        j.write("\n" + "Name: " + name + "\n")
        j.write("Phone Number: " + contact + "\n")
        j.write("Purchase Date: " + str(dateTime()) + "\n")
        j.write("Shipping Cost: $" + str(shipping_cost) + "\n")
        j.write("\n-------------------------------------------------------------")
        j.write("\nSNo\tManufacturer\tProduct\t\tQuantity\tPrice\n")
        j.write("-------------------------------------------------------------\n\n")

        totalQuantity = 0
        totalPrice = 0
        for index, (Id, quantity) in enumerate(furnitures):
            Name = mainData[Id][0]
            Product = mainData[Id][1]
            Price = int(mainData[Id][2].replace("$", "")) * quantity
            totalQuantity += quantity
            totalPrice += Price
            
            j.write(f"{index + 1}\t{Name}\t{Product}\t{quantity}\t${Price}\n")
        
        j.write("-------------------------------------------------------------\n\n")
        j.write("Total Price: $" + str(totalPrice) + "\n")
        j.write("Shipping Cost: $" + str(shipping_cost) + "\n")
        j.write("Grand Total: $" + str(totalPrice + shipping_cost) + "\n\n")
        j.write("\n\n************************************************************************")
        j.write("\n            Thank you for your purchase!                     \n")
        j.write("****************************************************************************")

def purchase():
    print("\n Let's purchase furniture. \n")
    
    fileContent = get_files()
    mainData = data_dict(fileContent)

    furnitures = []
    while True:
        f_print(mainData)
        Id = p_data(mainData)
        quantity = quantity_valid_p(mainData, Id)
        
        mainData[Id][3] = int(mainData[Id][3]) + quantity
        furnitures.append([Id, quantity])

        writeFile(mainData)
        f_print(mainData)
        
        userInput = input("Do you want to purchase more? (Y/N) ").strip().lower()
        if userInput == "no":
            break

    print()
    f_print(mainData, mainData)
    p_invoice(furnitures)
    print("\n******************************************************")
    print("      Thank you. Your purchase has been completed!        ")
    print("******************************************************\n")

def exitf():
    print("      Thank you for using our app                ")

loop = True

while loop:
    print("Select a preferred option")
    print("1) Press 1 to sell.")
    print("2) Press 2 to purchase.")
    print("3) Press 3 to exit.")

    try:
        choose = int(input("Enter an option: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choose == 1:
        sell()
    elif choose == 2:
        purchase()
    elif choose == 3:
        exitf()
        loop = False
    else:
        print("Invalid option! Please choose 1, 2, or 3.")
