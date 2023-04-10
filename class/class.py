import csv
class Item:
    #class attribute
    pay_rate = 0.8 # pay rate after discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        
        # running validation
        assert price >= 0, f"{price} => Price cannot be Negative"
        assert quantity >= 0, f"{quantity} => Quantity can be null or positive but not Negative"

        # assigning values
        self.name = name
        self.price = price
        self.quantity = quantity

        # appending to the all for list of objects
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls): #cls - class is passed as 1st argument
        with open("items.csv", 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # Checking float or int
        if isinstance(num, float):
            # to count out float
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # to represent the instance
    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

