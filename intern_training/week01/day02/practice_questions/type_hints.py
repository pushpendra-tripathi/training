'''
practice module: type_hints
'''

from typing import Callable


def process_data(
    data: list[int],
    transform: Callable[[int], list[int]] | None = None,
    filter_fn: Callable[[int], bool] | None = None,
):
    """Process list with optional transform and filter."""
    pass


def group_items(items: list[n], key_func: Callable[[int], bool] | None):
    """Group items by key_func result."""
    pass
