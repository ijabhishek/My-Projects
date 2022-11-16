class Item:
    def __init__(self, id:int, name:str, price:float, measurement_unit:str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.mesurement_unit = measurement_unit  #e.g -> Kg or ml

    def __repr__(self) -> str:
        return "<class 'item'>"

    def __str__(self) -> str:
        return f" {self.name}: {self.price}/{self.mesurement_unit}"