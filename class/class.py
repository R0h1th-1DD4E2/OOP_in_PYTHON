from item import Item 
from phone import Phone

item1 = Item("PC", 1000,1)
item1.apply_increment(0.2)

print(item1.price)