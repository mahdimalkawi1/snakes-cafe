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
