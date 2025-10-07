#Create a variable ItemsInCart and initialize it to 0. Write a function called add_to_cart that accepts an integer parameter items_to_add.
#If items_to_add is less than 0, raise an exception with the message "Cannot add a negative number of items."
#If the total count of items after addition exceeds 5, raise an exception with the message "Cart limit exceeded."


ItemsInCart = 0
def add_to_cart(items_to_add: int):
    global ItemsInCart  # so we can update the global variable

    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")

    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")

    ItemsInCart += items_to_add
    return ItemsInCart

try:
    #print(add_to_cart(-1))
    print(add_to_cart(2))
    print(add_to_cart(3))
    #print(add_to_cart(1))

except Exception as e:
    print("Error:", e)









