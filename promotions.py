from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract class for all promotions"""

    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    """Subclass for promotion. Applies -50% discount to every second instance of the same item"""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies a -50% discount for every second instance of the same item and returns  the
        discounted price.

        If the quantity is even, half of the quantity is considered for the discount.
        Otherwise,  half of the quantity plus one is used.

        The discounted price is calculated by dividing the original price by 2 and then
        multiplied by the discounted quantity.
        """
        if quantity % 2 == 0:
            discounted_quantity = quantity / 2
        else:
            discounted_quantity = (quantity // 2) + 1
        discounted_price = product.price / 2
        return discounted_price * discounted_quantity


class ThirdOneFree(Promotion):
    """Subclass for promotion. Every third instance of the same item is free."""

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """
        Reduces the order quantity by one-third, calculates the remaining amount, if any,
        and returns the discounted price.
        """
        free_items = quantity // 3
        remaining_items = quantity % 3
        discounted_price = product.price * (quantity - free_items)
        return discounted_price + (remaining_items * product.price)


class PercentDiscount(Promotion):
    """Subclass for promotion, which gives every second item -50% discount"""

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the percentage discount to the product price and returns
        the discounted price.
        """
        discounted_price = product.price * (1 - self.percent / 100)
        return discounted_price * quantity
