# shopping_cart.py
from datetime import datetime, date
import os
from dotenv import load_dotenv

load_dotenv()

#Set Tax Rate
TAX_RATE = os.getenv('TAX_RATE')

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# Ask for a product identifier

product_ids = [str(i['id']) for i in products]

shopping_cart_ids = []
checkout_start_time = datetime.now()

while True:
    product_entered = input("Scan or enter product code ")
    if product_entered == "done":
        break
    elif product_entered in product_ids:
        shopping_cart_ids.append(product_entered)
    else:
        print("Invalid product id")

# Build the shopping cart
shopping_cart = [i for i in products if str(i["id"]) in shopping_cart_ids]

#Set the store details
store_name = "Mike's Bodega"
store_phone_number = "555-456-1981"
store_address = "45 Winding Way"
store_website = "www.mikesbodega.com"

#Print the store details and date/time
print("__________________")
print(store_name)
print(store_phone_number)
print(store_address)
print(store_website)
print("__________________")
print(checkout_start_time.strftime("%x"), checkout_start_time.strftime("%X"))
print("__________________")

#Create list to track subtotal
items_to_subtotal = []

#Print the shopping cart items
print("Items:")
for item in shopping_cart:
    print(item["name"]," ", to_usd(item["price"]))
    items_to_subtotal.append(item["price"])

# Calculate totals
item_subtotal = sum(items_to_subtotal)
total_tax = item_subtotal*float(TAX_RATE)
total = item_subtotal + total_tax

# Print the totals
print("__________________")
print("Subotal = ", to_usd(item_subtotal))
print("Tax = ", to_usd(total_tax))
print("Total = ", to_usd(total))
print("__________________")
print("Thank you for shopping! Please come again soon.")
