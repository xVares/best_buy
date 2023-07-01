class Store:
    """Represents a store that contains a list of products."""

    def __init__(self, product):
        """
       (List[Product]):
            List of products in the store.
        """
        self.store_products = product

    def add_product(self, product):
        """Adds a product to the store."""
        self.store_products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        store_product_index = self.store_products.index(product)
        del self.store_products[store_product_index]

    def get_total_quantity(self) -> int:
        """Returns the total quantity of items in the store."""
        total_product_quantity = 0
        for product in self.store_products:
            total_product_quantity += product.quantity
        return total_product_quantity

    def get_all_products(self) -> list:
        """Returns a list of all active products in the store."""
        active_products = []
        for product in self.store_products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """
        Buys the products specified in the shopping list and returns the total price of the
        order.
        """
        order_price = 0

        for item in shopping_list:
            order_class = item[0]  # which product to buy
            order_quantity = item[1]  # how many units to buy

            # loop over store products and subtract order quantity from stock
            for product in self.store_products:
                if order_class.name == product.name:
                    order_price += product.buy(order_quantity)
        return order_price
