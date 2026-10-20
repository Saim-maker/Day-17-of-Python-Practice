#Concession stand program using dictionaries

# menu = {
#     "pizza": 20,
#     "nachos": 10,
#     "fries": 30,
#     "popcorn": 40,
#     "chicken": 50,
#     "chips": 35,
#     "soda": 30,
#     "lemonade": 40
# }
#
# cart = []
# total = 0
#
# print("--------Menu--------")
#
# for key, value in menu.items():
#     print(f"{key:10}: {value:.2f}")
#
# print("--------------------")
#
# while True:
#     food = input("Select your food from menu (q to quit): ").lower()
#
#     if food == "q":
#         break
#
#     elif menu.get(food) is not None:
#         cart.append(food)
#
#     else:
#         print("Sorry! This item is not available.")
#
# print("\n--------Your Order--------")
#
# for food in cart:
#     print(food)
#     total += menu.get(food)
#
# print("--------------------------")
# print(f"Your total bill is: ${total:.2f}")


# Grocery store billing system

# products = {
#     "apple": 50,
#     "banana": 30,
#     "milk": 180,
#     "bread": 120,
#     "eggs": 300
# }
#
# cart = []
# total = 0
#
# print("------ Grocery Store ------")
#
# for product, price in products.items():
#     print(f"{product:10}: Rs. {price:.2f}")
#
# print("---------------------------")
#
# while True:
#     item = input("Enter a product (q to quit): ").lower()
#
#     if item == "q":
#         break
#     elif item in products:
#         cart.append(item)
#     else:
#         print("Sorry! Product not available.")
#
# print("\n------ Your Cart ------")
#
#
# for item in cart:
#     print(f"{item:10} Rs. {products[item]:.2f}")
#     total += products[item]
#
# print("-----------------------")
# print(f"Total Bill: Rs. {total:.2f}")

# Inventory system

stock =  {
    "pen": 20,
    "book": 10,
    "eraser": 30,
    "marker": 15
}

cart = []
total = 0
print("-----The Stock System-----")
for key,value in stock.items():
    print(f"{key:10}: {value:.2f}")
print("--------")
while True:
    choice = input("Enter your choice (q to exit): ").lower()
    if choice == "q":
        break
    elif stock.get(choice):
        cart.append(choice)
print("-------Your Cart-------")
for item in cart:
    print(f"{item:10}: {stock[item]:.2f}")
    total = total + stock[item]
print(f"Your total is ${total:.2f}")