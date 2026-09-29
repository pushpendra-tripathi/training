"""
shopping cart class
"""

from dataclasses import dataclass


@dataclass
class Product:
    """
    data class for products
    """

    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")


class ShoppingCart:
    """Shopping cart with products."""

    def __init__(self):
        self._items: dict[str, tuple[Product, int]] = {}  # name -> (product, quantity)

    def add_item(self, product: Product, quantity: int = 1) -> None:
        """
        method to add products to list
        """
        self._items[str(product.name)] = (product, quantity)

    def remove_item(self, product_name: str) -> None:
        """Remove product from cart."""
        del self._items[product_name]

    def get_total(self) -> float:
        """Calculate total price."""
        total_price = 0
        for i in self._items:
            total_price += self._items[i][0].price * self._items[i][1]
        return total_price

    def __len__(self) -> int:
        """Return total number of items (considering quantities)."""
        total_items = 0
        for i in self._items:
            total_items += self._items[i][1]
        return total_items
