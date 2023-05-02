

# def intro():
#     print('''
# **************************************
# **    Welcome to the Snakes Cafe!   **
# **    Please see our menu below.    **
# **
# ** To quit at any time, type "quit" **
# **************************************
# Appetizers
# ----------
# Wings
# Cookies
# Spring Rolls

# Entrees
# -------
# Salmon
# Steak
# Meat Tornado
# A Literal Garden

# Desserts
# --------
# Ice Cream
# Cake
# Pie

# Drinks
# ------
# Coffee
# Tea
# Unicorn Tears

# ***********************************
# ** What would you like to order? **
# ***********************************
# ''')

# def user_order():
#     user_input=input(">")
#     return user_input
# print(user_order())


# def main():
#     user_input = user_order()
#     while(user_input.lower() != "quit"):

#             if user_input in Appetizers:
#                 print(user_input)

#             else:
#                 print("sorry we dont have this item !")

#             user_input = user_order()


# def end_application():
#     print("thanks for using snakes cafe application !")

# if __name__ == "__main__":
#     intro()
#     main()
#     end_application()


# print("**************************************")
# print("**    Welcome to the Snakes Cafe!   **")
# print("**    Please see our menu below.    **")
# print("**")
# print("** To quit at any time, type \"quit\" **")
# print("**************************************")

# refactore it & keep it DRY
# Appetizers = ["Wings",'Cookies'," Spring Rolls"]

# Appetizers = ["Wings", "Cookies", "Spring Rolls"]

# Entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]

# Desserts = ["Ice Cream", "Cake", "Pie"]

# Drinks = ["Coffee", "Tea", "Unicorn Tears"]


# def intro():
#     print('''
# **************************************
# **    Welcome to the Snakes Cafe!   **
# **    Please see our menu below.    **
# **
# ** To quit at any time, type "quit" **
# **************************************
# Appetizers
# ----------
# Wings
# Cookies
# Spring Rolls

# Entrees
# -------
# Salmon
# Steak
# Meat Tornado
# A Literal Garden

# Desserts
# --------
# Ice Cream
# Cake
# Pie

# Drinks
# ------
# Coffee
# Tea
# Unicorn Tears

# ***********************************
# ** What would you like to order? **
# ***********************************
# ''')


# def user_insertion():
#     user_input = input(">")
#     return user_input


# def main():
#     user_input = user_insertion()
#     while (user_input.lower() != "quit"):

#         # if user_input.lower() == "quit":
#         #     end_application()
#         if user_input in Appetizers:
#             print(user_input)
#             # TODO: handle the order numbers
#         elif user_input in Entrees:
#                 print(user_input)
#         elif user_input in Desserts:
#                 print(user_input)
#         elif user_input in Drinks:
#                 print(user_input)
#         else:
#             print("sorry we dont have this item !")

#         user_input = user_insertion()

#     end_application()


# def end_application():
#     print("thanks for using snakes cafe application !")


# # invoke the function
# if __name__ == "__main__":
#     intro()
#     main()

Appetizers = ["Wings", "Cookies", "Spring Rolls"]
Entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
Desserts = ["Ice Cream", "Cake", "Pie"]
Drinks = ["Coffee", "Tea", "Unicorn Tears"]

orders = {}

def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
''')

def user_insertion():
    user_input = input(">")
    return user_input.title()

def add_order(item):
    if item in orders:
        orders[item] += 1
    else:
        orders[item] = 1
    print(f"** {orders[item]} orders of {item} have been added to your meal **")

def main():
    user_input = user_insertion()
    while (user_input.lower() != "quit"):
        if user_input in Appetizers:
            add_order(user_input)
        elif user_input in Entrees:
            add_order(user_input)
        elif user_input in Desserts:
            add_order(user_input)
        elif user_input in Drinks:
            add_order(user_input)
        else:
            print("sorry we dont have this item !")

        user_input = user_insertion()

    end_application()

def end_application():
    print("Your order:")
    for item in orders:
        print(f"{orders[item]} orders of {item}")
    print("Thanks for using snakes cafe application !")

if __name__ == "__main__":
    intro()
    main()
