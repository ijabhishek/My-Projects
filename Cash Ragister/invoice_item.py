from item import Item

class InvoiceItem:
    """Line Item for cash register with purchase quantity & discount"""

    def __init__(self, item:Item, qty: int, discount: float = 0) -> None: # we mentioned float = 0 cause if user does not provide unit for discount
        self.item = item
        self.qty = qty
        self.discount = discount
        #private Member _ simble using
        self._sub_total = (item.price*qty) - discount

    def __repr__(self) -> str:
        return "<class 'InvoiceItem'>"

    def __str__(self) -> str:
        return (
            f"Item: {self.item.name} , Quantity: {self.qty} ,"
            f"Discount: {self.discount} , Sub Total: {self.get_sub_total():.2} "
        )

    def get_sub_total(self) -> float:
        """Returns the sub-total"""
        return self._sub_total
    


