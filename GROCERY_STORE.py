# Grocery Shop
# Importing Modules and Packages
from math import *
from datetime import *
from prettytable import *
from pymongo import *
from termcolor import *
#Shop Name
print(colored("\t\t\t\t\t\t\tSJSL STORE\t\t","green",attrs=['underline']))
# Checking time :
Current_time = datetime.now()
Open = datetime.strptime("09:00", "%H:%M")
Close = datetime.strptime("22:00", "%H:%M")
Time = Current_time.time()
if not (Open.time() <= Time < Close.time()):
    print(colored("Sorry for the inconvenince !! The shop is being closed","red",attrs=['bold']))
else : 
  print()
  print(colored("\n\tThe store is opened you can shop now ","magenta",attrs=['bold']))
  print()
# Establishing MongoDB connection , Data base  and  collections
  connect = MongoClient('mongodb://localhost:27017/')
  DB = connect['SJSL_Store']
  Collection = DB['Stocks']
  UserCollection = DB['Selected_Items']
# Data adding 
  Data = [{
    "_id":1,
      "Stock": {
        "Dairy": {
          "category_id": 1,
          "items": [
            {"item_id": 1, "name": "Milk", "quantity": 100, "price_per_unit": 50, "unit": "litre"},
            {"item_id": 2, "name": "Cheese", "quantity": 50, "price_per_unit": 300, "unit": "kg"},
            {"item_id": 3, "name": "Butter", "quantity": 30, "price_per_unit": 400, "unit": "kg"},
            {"item_id": 4, "name": "Yogurt", "quantity": 80, "price_per_unit": 60, "unit": "litre"},
            {"item_id": 5, "name": "Cream", "quantity": 20, "price_per_unit": 200, "unit": "litre"}
          ]
        },
        "Meat": {
          "category_id": 2,
          "items": [
            {"item_id": 6, "name": "Chicken", "quantity": 100, "price_per_unit": 200, "unit": "kg"},
            {"item_id": 7, "name": "Beef", "quantity": 80, "price_per_unit": 300, "unit": "kg"},
            {"item_id": 8, "name": "Pork", "quantity": 50, "price_per_unit": 250, "unit": "kg"},
            {"item_id": 9, "name": "Lamb", "quantity": 30, "price_per_unit": 400, "unit": "kg"},
            {"item_id": 10, "name": "Turkey", "quantity": 20, "price_per_unit": 350, "unit": "kg"}
          ]
        },
        "Grains": {
          "category_id": 3,
          "items": [
            {"item_id": 11, "name": "Rice", "quantity": 150, "price_per_unit": 50, "unit": "kg"},
            {"item_id": 12, "name": "Wheat", "quantity": 200, "price_per_unit": 30, "unit": "kg"},
            {"item_id": 13, "name": "Oats", "quantity": 50, "price_per_unit": 60, "unit": "kg"},
            {"item_id": 14, "name": "Cornmeal", "quantity": 25, "price_per_unit": 40, "unit": "kg"},
            {"item_id": 15, "name": "Rye", "quantity": 20, "price_per_unit": 60, "unit": "kg"}
          ]
        },
        "Beverages": {
          "category_id": 4,
          "items": [
            {"item_id": 16, "name": "Coffee", "quantity": 100, "price_per_unit": 500, "unit": "kg"},
            {"item_id": 17, "name": "Tea", "quantity": 150, "price_per_unit": 300, "unit": "kg"},
            {"item_id": 18, "name": "Juice", "quantity": 200, "price_per_unit": 100, "unit": "litre"},
            {"item_id": 19, "name": "Soda", "quantity": 180, "price_per_unit": 50, "unit": "litre"},
            {"item_id": 20, "name": "Water", "quantity": 300, "price_per_unit": 20, "unit": "litre"}
          ]
        },
        "Fruits": {
          "category_id": 5,
          "items": [
            {"item_id": 21, "name": "Apple", "quantity": 150, "price_per_unit": 100, "unit": "kg"},
            {"item_id": 22, "name": "Banana", "quantity": 200, "price_per_unit": 40, "unit": "kg"},
            {"item_id": 23, "name": "Mango", "quantity": 80, "price_per_unit": 120, "unit": "kg"},
            {"item_id": 24, "name": "Orange", "quantity": 90, "price_per_unit": 90, "unit": "kg"},
            {"item_id": 25, "name": "Strawberry", "quantity": 50, "price_per_unit": 300, "unit": "kg"}
          ]
        },
        "Vegetables": {
          "category_id": 6,
          "items": [
            {"item_id": 26, "name": "Carrot", "quantity": 150, "price_per_unit": 60, "unit": "kg"},
            {"item_id": 27, "name": "Potato", "quantity": 250, "price_per_unit": 30, "unit": "kg"},
            {"item_id": 28, "name": "Tomato", "quantity": 200, "price_per_unit": 50, "unit": "kg"},
            {"item_id": 29, "name": "Onion", "quantity": 100, "price_per_unit": 40, "unit": "kg"},
            {"item_id": 30, "name": "Cucumber", "quantity": 120, "price_per_unit": 70, "unit": "kg"}
          ]
        },
        "Snacks": {
          "category_id": 7,
          "items": [
            {"item_id": 31, "name": "Chips", "quantity": 200, "price_per_unit": 20, "unit": "pack"},
            {"item_id": 32, "name": "Biscuits", "quantity": 150, "price_per_unit": 40, "unit": "pack"},
            {"item_id": 33, "name": "Popcorn", "quantity": 100, "price_per_unit": 30, "unit": "pack"},
            {"item_id": 34, "name": "Pretzels", "quantity": 50, "price_per_unit": 60, "unit": "pack"},
            {"item_id": 35, "name": "Nuts", "quantity": 60, "price_per_unit": 200, "unit": "kg"}
          ]
        },
        "Bakery": {
          "category_id": 8,
          "items": [
            {"item_id": 36, "name": "Bread", "quantity": 100, "price_per_unit": 40, "unit": "loaf"},
            {"item_id": 37, "name": "Cake", "quantity": 50, "price_per_unit": 300, "unit": "kg"},
            {"item_id": 38, "name": "Muffins", "quantity": 80, "price_per_unit": 100, "unit": "pack"},
            {"item_id": 39, "name": "Croissant", "quantity": 60, "price_per_unit": 120, "unit": "pack"},
            {"item_id": 40, "name": "Bagels", "quantity": 30, "price_per_unit": 90, "unit": "pack"}
          ]
        },
        "Frozen Foods": {
          "category_id": 9,
          "items": [
            {"item_id": 41, "name": "Frozen Vegetables", "quantity": 100, "price_per_unit": 120, "unit": "kg"},
            {"item_id": 42, "name": "Frozen Pizza", "quantity": 50, "price_per_unit": 250, "unit": "kg"},
            {"item_id": 43, "name": "Frozen Meat", "quantity": 80, "price_per_unit": 400, "unit": "kg"},
            {"item_id": 44, "name": "Frozen Fish", "quantity": 60, "price_per_unit": 350, "unit": "kg"},
            {"item_id": 45, "name": "Frozen Snacks", "quantity": 120, "price_per_unit": 150, "unit": "pack"}
          ]   
        },
        "Spices": {
          "category_id": 10,
          "items": [
            {"item_id": 46, "name": "Cumin", "quantity": 50, "price_per_unit": 300, "unit": "kg"},
            {"item_id": 47, "name": "Turmeric", "quantity": 60, "price_per_unit": 200, "unit": "kg"},
            {"item_id": 48, "name": "Chili Powder", "quantity": 40, "price_per_unit": 250, "unit": "kg"},
            {"item_id": 49, "name": "Coriander", "quantity": 30, "price_per_unit": 150, "unit": "kg"},
            {"item_id": 50, "name": "Cinnamon", "quantity": 20, "price_per_unit": 500, "unit": "kg"}
          ] 
        },
        "Sugars & Sweeteners": {
          "category_id": 11,
          "items": [
            {"item_id": 51, "name": "White Sugar", "quantity": 200, "price_per_unit": 40, "unit": "kg"},
            {"item_id": 52, "name": "Brown Sugar", "quantity": 80, "price_per_unit": 50, "unit": "kg"},
            {"item_id": 53, "name": "Honey", "quantity": 50, "price_per_unit": 500, "unit": "kg"},
            {"item_id": 54, "name": "Maple Syrup", "quantity": 30, "price_per_unit": 700, "unit": "bottle"},
            {"item_id": 55, "name": "Stevia", "quantity": 40, "price_per_unit": 300, "unit": "pack"}
          ]
        },
        "Oil": {
          "category_id": 12,
          "items": [
            {"item_id": 56, "name": "Olive Oil", "quantity": 100, "price_per_unit": 500, "unit": "litre"},
            {"item_id": 57, "name": "Vegetable Oil", "quantity": 150, "price_per_unit": 120, "unit": "litre"},
            {"item_id": 58, "name": "Coconut Oil", "quantity": 80, "price_per_unit": 300, "unit": "litre"},
            {"item_id": 59, "name": "Sunflower Oil", "quantity": 90, "price_per_unit": 100, "unit": "litre"},
            {"item_id": 60, "name": "Mustard Oil", "quantity": 60, "price_per_unit": 150, "unit": "litre"}
          ]
        }
      }
    }]
# Creating an empty collections for the custmer 
  Selected_items = []
# Handling exceptions for insertions of data to mongodb
  try:
    Collection.insert_many(Data)
  except:
    print()
# Creating class for displaying 
  class Display:
    def __init__(self, collection):
      self.collection = collection
    def display(self):
# Creating one table for all categories and items
      table = PrettyTable()
      table.field_names = [colored("SI.NO:","blue",attrs=['bold']),
                         colored("Category","blue",attrs=['bold']),
                         colored("Item Name","blue",attrs=['bold']),
                         colored("Quantity","blue",attrs=['bold']),
                         colored("Prices_Per_Unit","blue",attrs=['bold']),
                         colored("Unit","red",attrs=['bold'])]
# Fetching all data from the collection
      data = self.collection.find()  # Fetch all documents in the collection  
# Iterate through all documents and display name, quantity, price, and unit
      for doc in data:
        stock = doc["Stock"]  # Accessing the "Stock" field
        for category, category_data in stock.items():
          for i in category_data["items"]:
            table.add_row([ colored(i["item_id"],"yellow",attrs=['bold']),colored(category,"magenta"),colored(i["name"],"green",attrs=['underline']),colored(i["quantity"],"white"),colored(i["price_per_unit"],"cyan"),colored(i['unit'],"red")])
          table.add_row(["-" * 22, "-" * 22, "-" * 22, "-" * 22,"-"*22,"-"*22])
      print(table)
    def Bill(self, Items):
      bill = PrettyTable()
      bill.field_names = [colored("Item Name","cyan",attrs=['bold']),
                        colored("Quantity","cyan",attrs=['bold']), 
                        colored("Price Per Unit","cyan",attrs=['bold']),
                        colored("Total price per item","cyan",attrs=['bold'])
                       ]
# Add selected items to the table
      Total = 0
      for item in Items:
        bill.add_row([colored(item["name"],"blue"),
                    colored(item["quantity"],"yellow"), 
                    colored(item["price_per_unit"],"green") , 
                    colored(item["price_per_unit"]*item["quantity"],"red")
                  ])
        Total +=   item["price_per_unit"]*item["quantity"]
      bill.add_row(["-"*18,"-"*18,"-"*18,"-"*18])
      bill.add_row([colored("The total bill amount","cyan",attrs=['bold']),
                  colored("with including","cyan",attrs=['bold']),
                  colored("GST is :","cyan",attrs=['bold']),
                  colored(Total,"white",attrs=['bold'])
                ])
# Print the selected items table
      print(colored("\nThe Bill of Selected Items : ","grey",attrs=['bold']))
      print(bill)

#displaying all the stockes
  Display = Display(Collection)
  Display.display()
  print(colored("\n\n\t\t\t\t\t\tWELCOME sir!! \t\t\t\n\n\t\t\t\t    We have displayed the available stockes\n","blue",attrs=['bold']))
#Selecting the items needed
  while True:
    item_id = int(input(colored("Enter the Item ID to select (or 0 to finish): ","yellow",attrs=['bold'])))  
    if item_id == 0:
      break
    quantity = int(input(colored("Enter the quantity : ","cyan",attrs=['bold'])))
# Find the item in stock
    Find = False
    for i in Data:
      stock = i["Stock"]
      for category, details in stock.items():
        for item in details["items"]:
          if item["item_id"] == item_id:
# Check stock availability
            if item["quantity"] >= quantity:
# Add item to selected list
              Selected_items.append({
                                  "item_id": item["item_id"],
                                  "name": item["name"],
                                  "quantity": quantity,
                                  "price_per_unit": item["price_per_unit"],
                                  "unit": item["unit"],
                                  "category": category
                                })
          # Update stock quantity
              item["quantity"] -= quantity
              print(colored(f"Added {quantity} {item['unit']} {item['name']} to your selection.","magenta",attrs=['bold']))
              print()
            else:
              print(colored(f"Insufficient stock for {item['name']}. Available: {item['quantity']}","red",attrs=['bold']))

# Store selected items into New collection
  if Selected_items:
    UserCollection.insert_many(Selected_items)
    print()
    print(colored("Your items have been successfully stored in the Purchases collection.","green",attrs=['bold']))
  else:
    print(colored("No items selected.","red",attrs=['bold']))

# Updating the stock with the collection with new quantities
  Collection.update_one({"_id": 1}, {"$set": {"Stock": Data[0]["Stock"]}})
# Displaying the bill
  Display.Bill(Selected_items)
  print(colored("\n\t\t\t\tThankYou For shoping !!\t\t\n\n\t\t\t\t   Have a nice day!!\t",'blue',attrs=['bold']))
