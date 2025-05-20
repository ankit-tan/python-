# define the menu  of  restaurant
menu ={
    'pezza':40,
    'pasta':30,
    'burger':60,
    'salad':80,
    'coffee':80
}
#greet
print("welcome to pytho resurants ")
print("pizza:Rs40\npata:Rs30\nburger:RS60\nsalad:Rs 80\ncoffee:Rs80")

order_total =0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not avaialanle yet")
    another_order=  input("do you wnat to add another item? (yes/no)") 
    if another_order =="yes":
       item_2 = input("Enter the name of second item=")
       if item_2 in menu:
           order_total+= menu[item_2]
           print(f"item {item_2} has been added to order")
       else:
           print(f"ordered item{item_2} is not avaialable!")
           print(f"The toral  amount of item is pay to  {order_total}")