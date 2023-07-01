import promotions

"""classes for products"""


def validate_product_init_params(name: str, price: int, quantity: int) -> None:
    """
    validate input of Product class to have the desired type.

        name:
            should be a non-empty string

        price:
            should be a positive integer

        quantity:
            should be a positive integer
    """
    if not isinstance(name, str) or name == "":
        raise ValueError(f"Invalid product name '{name}': should be a non-empty string")

    if not isinstance(price, int) or price < 0:
        raise ValueError(f"Invalid product price '{price}': should be a positive integer")

    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError(f"Invalid product quantity '{quantity}': should be a positive integer")


class Product:
    """Represents a product."""

    def __init__(self, name: str, price: int, quantity: int) -> None:
        """
        Constructor of class Product. Validate input before constructing following instance
        variables:
            name (str): The name of the product.
            price (int): The price of the product.
            quantity (int): The quantity of the product.
            active (bool): The activation status of the product.
            promotion (obj): The Promotion obj of the product.
            maximum ()
        """
        validate_product_init_params(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> int:
        """Getter function for quantity. Returns the quantity (integer)."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def get_promotion(self):
        """Getter function for product promotion."""
        return self.promotion

    def set_promotion(self, promotion):
        """Setter function for product promotion object."""
        self.promotion = promotion

    def is_active(self) -> bool:
        """Getter function for active. Returns True if the product is active, otherwise False."""
        return self.active

    def activate(self) -> None:
        """Activates the product."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string that represents the product and corresponding promotions."""
        if self.promotion is None:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: " \
               f"{self.promotion.get_name()}"

    def buy(self, quantity: int) -> float:
        """
        Processes an order for the product with the given quantity.

        Args:
            quantity (int): The quantity of the product to be ordered.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the order quantity exceeds the stock in the store or exceeds the
                maximum limit for LimitedProduct.

        Notes:
            - For NonStockedProduct:
                the purchase is always successful, and the function returns the total price of
                the purchase without affecting the quantity.

            - For LimitedProduct:
                if the order quantity exceeds the maximum limit, a ValueError is raised.
                Otherwise, the quantity is deducted from the available stock.

            - For other products, the order quantity is deducted from the available stock.

        """
        # TODO:
        #   - Add exception for apply_promotion() method for products with no promotion
        #       • With workaround for | self.promotion = NoneType ?
        #   - more readable buy method ?
        #       • shorten / simplify / add helper function
        try:
            # check if order quantity exceeds stock in store
            if not isinstance(self, NonStockedProduct) and self.quantity - quantity < 0:
                raise ValueError(f"Order quantity for {self.name} is larger than current stock: "
                                 f"({self.quantity})")

            # filter non-stocked products -> purchase always successful
            elif isinstance(self, NonStockedProduct):
                print(f"You successfully purchased {quantity} units of"
                      f" {self.name} for {self.promotion.apply_promotion(self, quantity)}$!")
                return float(self.promotion.apply_promotion(self, quantity))

            # filter limited products
            elif isinstance(self, LimitedProduct):
                if quantity > self.maximum:
                    raise ValueError(f"Order quantity for {self.name} exceeds the maximum "
                                     f"limit: ({self.maximum})")
                self.set_quantity(self.quantity - quantity)
                print(
                    f"You successfully purchased {quantity} units of {self.name} for"
                    f" {self.promotion.apply_promotion(self, quantity)}$!")
                return float(self.promotion.apply_promotion(self, quantity))

            else:
                self.set_quantity(self.quantity - quantity)
                print(f"You successfully purchased {quantity} units of"
                      f" {self.name} for {self.promotion.apply_promotion(self, quantity)}$!")
                return float(self.promotion.apply_promotion(self, quantity))
        except ValueError as error:
            print(f"Error while making order! {error}")
            return 0.0


class NonStockedProduct(Product):
    """Subclass for products that have no tracking for their stock"""

    def __init__(self, name: str, price: int):
        super().__init__(name, price, 0)


class LimitedProduct(Product):
    """
    Subclass for products with a maximum limit on the quantity that can be bought  in a
    single order.
    """

    def __init__(self, name: str, price: int, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum
