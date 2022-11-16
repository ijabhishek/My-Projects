from datetime import datetime

from customer import Customer
from invoice_item import InvoiceItem
from item import Item

class CashRegister:
    """Cash Register for each customer"""

    def __init__(self, customer:Customer) -> None:
        self.customer = customer
        self.items: dict[str,InvoiceItem] = {}
        self.purchase_date = datetime.now()
    # Private Member
        self._invoice_total:float = 0
    def __repr__(self) -> str:
        return "<class 'CashRegister'>"
    
    def __str__(self) -> str:
        return f"Customer: {self.customer}, Total Item: {len(self.items)}"

    def inc_invoice_total(self, item: InvoiceItem) -> None:
        """Increment the total invoice value each time an item is added"""
        self._invoice_total += item.get_sub_total()

    def dec_invoice_total(self, item: InvoiceItem) -> None:
        """Dencrement the total invoice value each time an item is removed"""
        self._invoice_total -= item.get_sub_total()


    def add_item(self, item: Item, qty: int, discount:float=0) -> None:
        """Add's an item to cash register"""    
        if item.name not in self.items:
            new_item = InvoiceItem(item, qty, discount)
            self.items[item.name] = new_item
            self._inc_invoice_total(new_item)

        else:
            print(f"{item.name} already in cart, update instead")


