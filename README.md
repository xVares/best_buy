# Best Buy - (A simple Store Management System)

This Python program is a Store Management System that allows you to perform various operations related to managing
products in a store. It provides a menu-driven interface where you can list products, display the total quantity in the
store, make orders, and quit the program.

## Features

- List all products in the store, along with their details such as name, price, and quantity.
- Show the total quantity of items available in the store.
- Make an order by selecting products and specifying quantities.
- Quit the program when you're done.

## Usage

To start the program, run `main.py` in your terminal. It will initialize a list of products, create a store instance,
and present a menu to the user. Follow the terminal instructions to interact with the program.

### Menu Options

1. **List all products in store**: This option displays a numbered list of all products available in the store,
   including their details like name, price, and quantity.

2. **Show total quantity of products in store**: Selecting this option will print the total quantity of items available
   in the store.

3. **Make an order**: This option guides you through the process of placing an order. It presents a list of products and
   asks you to enter the desired product number and quantity. Once you finish adding products to your order, simply
   enter an empty text to return to the main menu.

4. **Quit**: Choosing this option will exit the program.

## Adding New Features

If you wish to add new features or functionality to this program, you can modify the code accordingly. Feel free to
extend the `Product` and `Store` classes in the `products.py` and `store.py` files, respectively, to incorporate
additional capabilities.

## Requirements

This program requires the `products.py` and `store.py` files, which contain the necessary classes and functions for
product and store management. Ensure that these files are present in the same directory as the main script.

## Notes

- The program uses the `start()` function to retrieve user input and handle the main menu interactions.
- The program uses the OOP principles to create instances of products and a store.
- The initial product list in the `main()` function can be customized according to your specific store requirements.

Feel free to enhance and customize this Store Management System to suit your needs. Happy managing!