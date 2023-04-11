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
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # appending to the all for list of objects
        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
    
    @property
    # property decorator | read only attribute
    def name(self):
        return self.__name    
    
    def calculate_total_price(self):
        return self.__price * self.quantity
    
    @name.setter
    def name(self, value):
        if len(value) > 15:
            raise Exception("The name is too long")
        else:
            self.__name = value

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
        return f"{self.__class__.__name__}('{self.name}','{self.__price}','{self.quantity}')"
