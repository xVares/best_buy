import products
import store
import promotions


def start(final_store):
    """Displays a menu of options, receives user input, and performs corresponding actions."""

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
            for product in final_store.get_all_products():
                print(f"{bullet_point}. {product.show()}")
                bullet_point += 1
            print("--------------------------------------------")

        # Menu Choice 2
        if user_input == 2:
            print(f"Total of {final_store.get_total_quantity()} items in store")

        # Menu Choice 3
        if user_input == 3:
            while True:
                bullet_point = 1
                order_basket = []

                # list items and append every item to order_basket
                print("--------------------------------------------")
                for product in final_store.get_all_products():
                    print(f"{bullet_point}. {product.show()}")
                    bullet_point += 1
                    order_basket.append(product)
                print("--------------------------------------------")
                print("When you want to finish order, enter empty text.")

                try:
                    product_choice = int(input("Which product do you want?"))
                    quantity = int(input("What amount do you want?"))
                    selected_product = order_basket[product_choice - 1]

                    # back to menu if user input is empty string by raising error
                    if selected_product == "" or quantity == "":
                        raise ValueError
                    basket_price = final_store.order([(selected_product, quantity)])
                    print(f"You successfully purchased {quantity} units of"
                          f" {selected_product.name} for {basket_price}$!")
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
    """
    Starts the program and handles the main menu interactions.

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


# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

start(store.Store(product_list))

if __name__ == '__main__':
    main()
