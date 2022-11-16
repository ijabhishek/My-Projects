class Customer:
    def __init__(self, f_name:str, l_name:str)->None:
        self.f_name = f_name
        self.l_name = l_name
    
    def __repr__(self) ->str:
        return "<class 'customer'>"

    def __str__(self) -> str:
        return f"{self.f_name} {self.l_name}"

