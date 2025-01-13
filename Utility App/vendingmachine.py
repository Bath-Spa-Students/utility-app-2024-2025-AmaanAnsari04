NonCarbonated_drinks = {                #creating a dictionary for non-carbonated drinks and another dictionary inside for each item to include price and stock
    "NCD_1":{   "name":"Water",
                "price": 1.00,
                "stock": 10 }, 

    "NCD_2":{   "name":"Apple Juice",
                "price": 1.50,
                "stock": 10 },

    "NCD_3":{   "name":"Mango Juice",
                "price": 1.50,
                "stock": 10 },
                
    "NCD_4":{   "name":"Orange Juice",
                "price": 1.50,
                "stock": 10},

    "NCD_5":{   "name":"Lemon Juice",
                "price": 1.50, 
                "stock": 10},

    "NCD_6":{   "name":"Berry Juice",
                "price": 1.50,
                "stock": 10},

    "NCD_7":{   "name":"Strawberry Juice",
                "price": 1.50,
                "stock": 10},

    "NCD_8":{   "name":"Pomegranate Juice",
                "price": 1.50,
                "stock": 10},

    "NCD_9":{   "name":"Grape Juice",
                "price": 1.50,
                "stock": 10},

    "NCD_10":{  "name":"Coconut water",
                "price": 1.50, 
                "stock": 10}
    }



Carbonated_drinks = {                       #creating a dictionary for carbonated drinks and another dictionary inside for each item to include price and stock
    "CD_1":{    "name":"Pepsi",
                "price": 2.00,
                "stock": 10},
                        
    "CD_2":{    "name":"7up",
                "price": 2.00,
                "stock": 10},

    "CD_3":{    "name":"Coke", 
                "price": 2.00, 
                "stock": 10},

    "CD_4":{    "name":"Mountain Dew", 
                "price": 2.00, 
                "stock": 10},

    "CD_5":{    "name":"Marinda",
                "price": 2.00, 
                "stock": 10},

    "CD_6":{    "name":"Lemon Soda",
                "price": 2.00,
                "stock": 10},

    "CD_7":{    "name":"Fanta", 
                "price": 2.00, 
                "stock": 10},

    "CD_8":{    "name":"Sparkling Water", 
                "price": 3.00, 
                "stock": 10},
    }



Caffeinated_drinks = {                      #creating a dictionary for caffeinated drinks and another dictionary inside for each item to include price and stock
    "CFD_1":{   "name":"Iced Black Coffee", 
                "price": 3.50, 
                "stock": 10},
                       
    "CFD_2":{   "name":"Iced Black Tea", 
                "price": 3.50, 
                "stock": 10},

    "CFD_3":{   "name":"Lipton Iced Lemon Tea", 
                "price": 3.00, 
                "stock": 10},

    "CFD_4":{   "name":"Lipton Iced Peach Tea", 
                "price": 3.00, 
                "stock": 10},

    "CFD_5":{   "name":"Iced Green Tea", 
                "price": 3.00,
                "stock": 10},

    "CFD_6":{   "name":"Iced Americano",
                "price": 3.50, 
                "stock": 10},

    "CFD_7":{   "name":"Expresso", 
                "price": 3.00, 
                "stock": 10},

    "CFD_8":{   "name":"Iced Matcha", 
                "price": 3.00, 
                "stock": 10},

    "CFD_9":{   "name":"Red Bull",
                "price": 4.00, 
                "stock": 10},

    "CFD_10":{  "name":"Monster Energy", 
                "price": 4.00, 
                "stock": 10}
    }



Snack = {                               #creating a dictionary for Snack and another dictionary inside for each item to include price and stock
    "SK_1":{    "name":"Lays", 
                "price": 1.50, 
                "stock": 10},
                       
    "SK_2":{    "name":"Doritos", 
                "price": 1.50, 
                "stock": 10},

    "SK_3":{    "name":"Oreos",     
                "price": 1.00, 
                "stock": 10},

    "SK_4":{    "name":"Salted Pretzels", 
                "price": 2.00, 
                "stock": 10},

    "SK_5":{    "name":"Salted Mixed Nuts",
                "price": 2.00, 
                "stock": 10},

    "SK_6":{    "name":"Salted Popcorn", 
                "price": 1.50, 
                "stock": 10},

    "SK_7":{    "name":"Crackers", 
                "price": 2.00, 
                "stock": 10},

    "SK_8":{    "name":"Rice Crackers", 
                "price": 3.00, 
                "stock": 10},

    "SK_9":{    "name":"Chocolate Wafers", 
                "price": 2.00, 
                "stock": 10},

    "SK_10":{   "name":"Strawberry Wafers", 
                "price": 2.00, 
                "stock": 10}
    }




Candy = {                                                        #creating a dictionary for Candy and another dictionary inside for each item to include price and stock
    "CD_1":{    "name":"Kitkat", 
                "price": 3.50, 
                "stock": 10},

    "CD_2":{    "name":"Mars Bar", 
                "price": 3.50, 
                "stock": 10},

    "CD_3":{    "name":"Dairy Milk", 
                "price": 3.00, 
                "stock": 10},

    "CD_4":{    "name":"Galaxy Bar", 
                "price": 3.00, 
                "stock": 10},

    "CD_5":{    "name":"Skittles", 
                "price": 2.50, 
                "stock": 10},

    "CD_6":{    "name":"Starburst", 
                "price": 3.00, 
                "stock": 10},

    "CD_7":{    "name":"Sour Patch Kids", 
                "price": 3.00, 
                "stock": 10},

    "CD_8":{    "name":"Lemon Drops", 
                "price": 2.00, 
                "stock": 10},

    "CD_9":{    "name":"Gummy Bear", 
                "price": 2.00, 
                "stock": 10},

    "CD_10":{   "name":"Pop Rocks", 
                "price": 2.00, 
                "stock": 10}
    }

Checklist = []   #list stores the items you select

def itemdisplay(category, category_name):    #displays the list of items for each category
    print (f"{category_name}: ")
    for number, item in category.items():
        print(f"{number}: {item['name']}: ${item['price']}, Stock: {item['stock']}")
    print()

def addchecklist(category, number):         #adds item to the checklist and lets the user know it has been added
    if number in category:
        item = category[number]
        if (int(item["stock"]) > 0):        #checks the stock number
            Checklist.append({"name": item["name"], "price": item["price"]}) #adds item to cart
            (item["stock"]) -= 1                                            #reduces stock when item is selected
            print(f"{item['name']} has been added to cart!")
        else:
            print(f"Sorry, {item['name']} is out of stock. It will be restocked shortly!") #displays when items are out of stock
    else:
        print("Invalid code. Please try again.")

def totalprice():                   # calculates the total price for the items
    total = sum(item["price"] for item in Checklist)
    return total

print ("""
██╗   ██╗███████╗███╗  ██╗██████╗ ██╗███╗  ██╗ ██████╗   ███╗   ███╗ █████╗  █████╗ ██╗  ██╗██╗███╗  ██╗███████╗
██║   ██║██╔════╝████╗ ██║██╔══██╗██║████╗ ██║██╔════╝   ████╗ ████║██╔══██╗██╔══██╗██║  ██║██║████╗ ██║██╔════╝
╚██╗ ██╔╝█████╗  ██╔██╗██║██║  ██║██║██╔██╗██║██║  ██╗   ██╔████╔██║███████║██║  ╚═╝███████║██║██╔██╗██║█████╗  
 ╚████╔╝ ██╔══╝  ██║╚████║██║  ██║██║██║╚████║██║  ╚██╗  ██║╚██╔╝██║██╔══██║██║  ██╗██╔══██║██║██║╚████║██╔══╝  
  ╚██╔╝  ███████╗██║ ╚███║██████╔╝██║██║ ╚███║╚██████╔╝  ██║ ╚═╝ ██║██║  ██║╚█████╔╝██║  ██║██║██║ ╚███║███████╗
   ╚═╝   ╚══════╝╚═╝  ╚══╝╚═════╝ ╚═╝╚═╝  ╚══╝ ╚═════╝   ╚═╝     ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚══╝╚══════╝""")

print ( """
       
       
       
     
       
        """)


print (""" Categories:

            NonCarbonated Drinks       Carbonated Drinks      Caffeinated_drinks  
        
                                 Snacks                  Candy                   
                                                                                """)     #shows all the categories



while True:
    Category = input("Please pick a category or type quit if you are done: ") 
    if Category.lower() == "quit":
        if not Checklist:  #checks if the checklist is empty
            print ("Returning...") #output statment if the checklist is empty
            break
        else:
            
            print ("Proceeding to checkout...")
            print ("Items in cart: ")
            for item in Checklist:      #prints out the items in the checklist
                print (f"{item['name']} (${item['price']})")
            total = totalprice()                      
            print (f"Your total is ${total}")
            Item_pay = (input("Please enter your payment: ")) #asks user to input payment
            try:
                Item_pay = int(Item_pay)
                if Item_pay > total:
                    Item_return = (Item_pay) - (total)
                    print(f"Your change is ${Item_return}")  #prints out the change
                    print ("Please collect your item from below. Thank you! Come again!!") #displays to show items have been dispenced
                if Item_pay == (total):
                    print ("Please collect your item from below. Thank you! Come again!!")
                if Item_pay < (total):
                    print ("insuffient funds...")
            except ValueError:
                print ("Please enter whole numbers only")
        break


    if Category == "NonCarbonated Drinks":                                  #to display all the items in the list for the category selected
        itemdisplay (NonCarbonated_drinks, "Non-Carbonated Drinks")
        Select = input("Please enter the code of the item you wish to get or enter 'Quit' to leave:  ")

    if Category == "Carbonated Drinks":
        itemdisplay (Carbonated_drinks, "Carbonated Drinks")
        Select = input("Please enter the code of the item you wish to get or enter 'Quit' to leave:  ")

    if Category == "Caffeinated Drinks":
        itemdisplay (Caffeinated_drinks, "Caffeinated Drinks")
        Select = input("Please enter the code of the item you wish to get or enter 'Quit' to leave:  ")

    if Category == "Snacks":
        itemdisplay (Snack, "Snacks")
        Select = input("Please enter the code of the item you wish to get or enter 'Quit' to leave:  ")

    if Category == "Candy":
        itemdisplay (Candy, "Candy")
        Select = input("Please enter the code of the item you wish to get or enter 'Quit' to leave:  ")


    if Category == "NonCarbonated Drinks":           #adds the selected item from the category to the checklist
        addchecklist(NonCarbonated_drinks, Select)
    elif Category == "Carbonated Drinks":
        addchecklist(Carbonated_drinks, Select)
    elif Category == "Caffeinated Drinks":
        addchecklist(Caffeinated_drinks, Select)
    elif Category == "Snacks":
        addchecklist(Snack, Select)
    elif Category == "Candy":
        addchecklist(Candy, Select)