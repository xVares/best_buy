import products as products_file
import store as store_file


def start(store):
    """Prints menu and returns user input"""

    while True:
        print("\n"
              "1. List all products in store\n"
              "2. Show total amount in store\n"
              "3. Make an order\n"
              "4. Quit\n")

        user_input = 0
        try:
            user_input = int(input("Please choose a number: "))
            if not isinstance(user_input, int) or user_input <= 0 or user_input > 4:
                raise ValueError("invalid choice")
        except ValueError:
            print("Error with your choice! Try again! (1-4)")

        # Menu Choice 1
        if user_input == 1:
            bullet_point = 1
            print("--------------------------------------------")
            for product in store.get_all_products():
                print(f"{bullet_point}. {product.show()}")
                bullet_point += 1
            print("--------------------------------------------")

        # Menu Choice 2
        if user_input == 2:
            print(f"Total of {store.get_total_quantity()} items in store")

        # Menu Choice 3
        if user_input == 3:
            while True:
                bullet_point = 1
                order_basket = []

                # list items and append every item to order_basket
                print("--------------------------------------------")
                for product in store.get_all_products():
                    print(f"{bullet_point}. {product.show()}")
                    bullet_point += 1
                    order_basket.append(product)
                print("--------------------------------------------")
                print("When you want to finish order, enter empty text.")

                try:
                    user_product_choice = int(input("Which product do you want?"))
                    user_product_quantity = int(input("What amount do you want?"))
                    order_basket_product = order_basket[user_product_choice - 1]

                    # back to menu if user input is empty string by raising error
                    if user_product_choice == "" or user_product_quantity == "":
                        raise ValueError
                    store.order([(order_basket_product, user_product_quantity)])
                except IndexError:
                    print("Invalid product choice! Please try again.")
                except ValueError:
                    print("\nBack to the menu!")
                    break

        # Menu Choice 4
        if user_input == 4:
            print("Bye!")
            break


def main():
    """Starts the program and handles the main menu interactions.

    This function initializes a list of products, creates a store instance, and presents a menu
    to the user.
    The user can choose options from the menu to perform actions such as listing products,
    displaying the total quantity in the store, making an order, or quitting the program.

    The function continuously loops until the user chooses to quit.

    Menu Options:
    1. List all products in store:
        Displays a numbered list of all products in the store.

    2. Show total quantity of products in store:
        Prints the total quantity of items available in the store.

    3. Make an order:
        Guides the user through making an order by selecting products and quantities.

    4. Quit:
        Exits the program.

    Note: The function relies on the `start()` function to retrieve user input.

    """
    product_list = [products_file.Product("MacBook Air M2", price=1450, quantity=100),
                    products_file.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products_file.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store_file.Store(product_list)
    start(best_buy)


if __name__ == '__main__':
    main()
