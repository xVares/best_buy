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

    if not isinstance(price, int) or price <= 0:
        raise ValueError(f"Invalid product price '{price}': should be a positive integer")

    if not isinstance(quantity, int) or quantity <= 0:
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
        """
        validate_product_init_params(name, price, quantity)

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Getter function for quantity. Returns the quantity (integer)."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        self.quantity = quantity
        if self.quantity < 0:
            self.active = False

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
        """Returns a string that represents the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product. Returns the total price (float) of the purchase.
        Updates the quantity of the product. Raises a specific exception in case of a problem.
        """
        try:
            if self.quantity - quantity < 0:
                raise ValueError(f"Order quantity larger than current stock: ({self.quantity})")
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()
            print(f"You successfully purchased {quantity} units of"
                  f" {self.name} for {self.price * quantity}$!")
            return float(self.price * quantity)
        except ValueError as error:
            print(f"Error while making order! {error}")
            return 0.0
