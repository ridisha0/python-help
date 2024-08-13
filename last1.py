from datetime import datetime

print("------------------------------------------------")
print("************************************************")
print("          Welcome to BRJ Furnitures             ")
print("Kamalpokhari, Kathmandu | Contact no.9812345678")
print("************************************************")
print("------------------------------------------------")

def read_file():
    with open("database.txt", "r") as file:
        file_data = file.readlines()
        return file_data

def dict(file_content):
    data_dict = {}
    for index in range(len(file_content)):
        data_dict[index + 1] = file_content[index].replace("\n", "").split(",") 
    return data_dict

def f_print(file_content, main_data):
    print("---------------------------------------------------------------------------")
    print("SNo", "\t", "Manufacturer", "\t", "Product", "\t", "Quantity", "\t", "Price")
    print("---------------------------------------------------------------------------")
    for key,value in main_data.items(): 
        print(key, "\t", value[0], "\t", value[1], "\t", value[2], "\t", value[3])
    print("---------------------------------------------------------------------------")
    print("\n") 

def write_file(main_data):
    file = open("database.txt", "w")
    for value in main_data.values():
        write_data = str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + "\n"
        file.write(write_data)
    file.close()

def date_time():
    return datetime.now()

def purchaseID(main_data):
    p_id_valid = False
    while p_id_valid == False:
        try:
            ID_p = int(input("Enter the ID of item you want to purchase: "))
            if ID_p > 0 and ID_p <= len(main_data):
                p_id_valid = True
                return ID_p
            else:
                print("Enter valid ID!")
        except ValueError:
            print("Enter valid ID!")

def purchaseQuantity(main_data, ID_p):
    pquantity_valid = False
    while pquantity_valid == False:
        quantity_p = int(input("Enter the quantity of items you want to purchase:  "))
        if quantity_p > 0:
            pquantity_valid = True
            return quantity_p
        else:
            print("Enter valid quantity:")


def p_invoice(cart):

    file_content = read_file()
    main_data = dict(file_content)

    employee_name = input("Enter the name of employee: ")

    print("\n  INVOICE")
    print("\n" + "Employee Name: " + employee_name)
    date = date_time()
    print("Purchase Date: " + str(date))
    print("----------------------------------------------------------------------")
    print("SNo", "\t", "Manufacturer", "\t","Product","\t","Quantity","\t","Price")
    print("----------------------------------------------------------------------")

    total_quantity = 0
    total_price = 0

    for index in range(len(cart)):
        Id= int(cart[index][0])
        Quantity = int(cart[index][1])
        Manufacturer = main_data[Id][0]
        Product = main_data[Id][1]
        Price = int(main_data[Id][2].replace("$", ""))
        
        total_quantity += Quantity
        total_price = Price * Quantity

        print(str(index + 1) , "\t" , Manufacturer , "\t" , Product , "\t" , str(Quantity) , "\t" , str(Price))
        print("\n")
        
        print("------------------------------------------------")
        print("Total Quantity: " + str(total_quantity))
        print("Total Price: $" + str(total_price))
        print("------------------------------------------------")

        r = open (employee_name + ".txt" , w)

        r.write("\n      INVOICE                     \n")
        r.write("\n" + "Employee Name: " + employee_name + "\n")
        r.write("Purchase Date: " + str(date) + "\n")
        r.write("------------------------------------------------\n")
        r.write("SNo\tManufacturer\tProduct\tQuantity\tPrice\n")
        r.write("------------------------------------------------\n")

        
        for index in range(len(cart)):
            Id = int(cart[index][0])
            Quantity = int(cart[index][1])
            Manufacturer = main_data[Id][0]
            Product = main_data[Id][1]
            Price = int(main_data[Id][2].replace("$", ""))
            
            r.write(str(index + 1) + "\t" + Manufacturer + "\t" + Product + "\t" + str(Quantity) + "\t" + str(Price) + "\n")

            r.write("------------------------------------------------\n")
            r.write("Total Quantity: " + str(total_quantity) + "\n")
            r.write("Total Price: $" + str(total_price) + "\n")
            r.write("------------------------------------------------\n")
            r.write("------------------------------------------------\n")
            r.write("            Thank you for your purchase!      \n")
            r.write("------------------------------------------------\n")

            r.close()


def purchase():
        print("\n")
        print("Purchasing a furniture.")
        

        file_content = read_file()
        main_data = dict(file_content)

        cart=[]
        continueLoop = True
        while continueLoop == True:
            f_print(file_content, main_data)
            Id = purchaseID(main_data)
            p = int(purchaseQuantity(main_data, Id))
            main_data[Id][2] = str(int(main_data[Id][2]) + p)
            cart.append([Id, p])

            write_file(main_data)
            f_print(file_content, main_data)

            user_input = input("Do you want to purchase more furniture? (yes/no): ")
            if user_input.lower() == "no":
                continueLoop = False

        f_print(file_content, main_data)
        p_invoice(cart)
        print("------------------------------------------------")
        print("     Thankyou, the furniture has been purchased!")
        print("------------------------------------------------")

def sellID(main_data):
    s_id_valid = False
    while s_id_valid == False:
        ID_s = int(input("Enter the ID of furniture you want to sell: "))
        if ID_s > 0 and ID_s <= len(main_data):
            s_id_valid = True
            return ID_s
        else:
            print("Enter valid ID!")

def sellQuantity(main_data,ID_s):
    squantity_valid = False
    while squantity_valid == False:
        quantity_s = int(input("Enter the quantity of furniture: "))
        if quantity_s > 0 and quantity_s <= int(main_data[ID_s][2]):
            squantity_valid = True
            return quantity_s
        else:
            print("Not available!")
            print("\n")

def s_invoice(cart):

    file_content = read_file()
    main_data = dict(file_content)

    user_name = input("Enter your name: ")

    print("\n  INVOICE")
    print("\n" + "Name: " + user_name)
    date = date_time()
    print("Sell Date: " + str(date))
    print("---------------------------------------------------------------")
    print("SNo", "\t", "Brand", "\t","Product","\t","Quantity","\t","Price")
    print("---------------------------------------------------------------")

    total = 0
    for index in range(len(cart)):
        Id = int(cart[index][0])
        Quantity = int(cart[index][1])
        Brand = main_data[Id][0]
        Product = main_data[Id][1]
        Price = int(main_data[Id][2].replace("$", ""))*Quantity

        total += Price

        print(str(index + 1), "\t", Brand, "\t", Product, "\t", str(Quantity), "\t", str(Price))
        print("\n")

        shipping= input("Do you want the furniture shipped? (yes/no): ").strip().lower()
        shipping_cost = 15 if shipping== 'yes' else 0

        vat_rate = 0.13
        vat_amount = total * vat_rate

        #total amount with vat and then shipping cost
        total_with_vat = total + vat_amount
        grand_total = total_with_vat + shipping_cost

        print("------------------------------------------------")
        print("Total: $" + str(total))
        print("VAT 13% : $" + str(vat_amount))
        if shipping_cost > 0:
            print("Shipping cost: $" + str(shipping_cost))
        print("Total Amount: $" + str(grand_total))
        print("------------------------------------------------")
        print("\n")

        with open(user_name + ".txt", "w") as r:
            r.write("\n        INVOICE               \n")
            r.write("\nName: " + user_name + "\n")
            r.write("Sell Date: " + str(date) + "\n")
            r.write("---------------------------------------------")
            r.write("SNo\tBrand\tProduct\tQuantity\tPrice\n")
            r.write("----------------------------------------------")

            for index in range(len(cart)):
                Id = int(cart[index][0])
                Quantity = int(cart[index][1])
                Brand = main_data[Id][0]
                Product = main_data[Id][1]
                Price = int(main_data[Id][2].replace("$", "")) * Quantity

                r.write(str(index + 1), "\t", Brand, "\t", Product, "\t", str(Quantity), "\t", str(Price))

                r.write("\n-------------------------------------------------\n")
                r.write("Total: $" + str(total))
                r.write("VAT 13% : $" + str(vat_amount))
                if shipping_cost > 0:
                    r.write("Shipping cost: $" + str(shipping_cost))
                r.write("Total Amount: $" + str(grand_total))
                r.write("------------------------------------------------")
                r.write("------------------------------------------------")

                r.close()

def sell():
    print("Selling a furniture.")
    print("\n")

    file_content = read_file()
    main_data = dict(file_content)

    cart = []
    continueLoop = True
    while continueLoop == True:
        f_print(file_content, main_data)
        Id = sellID(main_data)
        s = int(sellQuantity(main_data, Id))
        main_data[Id][2] = str(int(main_data[Id][2]) - s)
        cart.append([Id, s])

        write_file(main_data)
        f_print(file_content, main_data)

        user_input = input("Do you want to sell more furniture? (yes/no): ")

        if user_input.lower() == "no":
            continueLoop = False

    f_print(file_content, main_data)
    s_invoice(cart)
    print("------------------------------------------------")
    print("     Thankyou, the furniture has been sold!")
    print("------------------------------------------------")
    

def exit_program():
    print(" Thankyou!")
    print("\n")
    return exit_program

loop = True

while loop == True:

    print("------------------------------------------------")
    print("Select the preferred option")
    print("Press 1 to view furnitures.")
    print("Press 2 to sell the items to the customers.")
    print("Press 3 to purchase from the manufacturer.")
    print("Press 4 to exit.")
    print("------------------------------------------------")

    choose = int(input("Enter your preferred option: "))

    if choose ==1:
        file_content = read_file()
        main_data = dict(file_content)
        f_print(file_content, main_data)
        

    if choose == 2:
        sell()

    elif choose == 3:
        purchase()

    elif choose == 4:
        exit_program()
        loop = False
          
        



        
        
            
            


            

        
        
        



          

    
    
    




            
