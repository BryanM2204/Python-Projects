class ItemToPurchase:
    
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        
    def print_item_cost(self):
        self.item_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_cost}')
        
class ShoppingCart:
    
    def __init__(self, customer_name="none", current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)


    def remove_item(self, Selected_input):
        for i in self.cart_items:
            if i.item_name == Selected_input:
                self.cart_items.remove(i)
                print()
                break
        else:
            print('Item not found in cart. Nothing removed.')
            print()

    def modify_item(self):
        print('CHANGE ITEM QUANTITY')
        alter_input = input('Enter the item name:\n')
        new_quantity = int(input('Enter the new quantity:'))
        for i in self.cart_items:
            if i.item_name == alter_input:
                i.item_quantity = new_quantity
                print()
                break
        else:
            print('\nItem not found in cart. Nothing modified.')
            print()

    def get_num_items_in_cart(self):
        total_items = 0
        for i in self.cart_items:
            total_items += i.item_quantity
        return total_items

    def get_cost_of_cart(self):
        total_cost = 0
        for i in self.cart_items:
            total_cost += (i.item_quantity * i.item_price)
        return total_cost
        
    def print_total(self):
        if self.get_num_items_in_cart() == 0:
            print('OUTPUT SHOPPING CART')
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print(f'Number of Items: {ShoppingCart.get_num_items_in_cart(self)}\n')
            print('SHOPPING CART IS EMPTY')
            print(f'\nTotal: ${ShoppingCart.get_cost_of_cart(self)}\n')
        else:
            print('OUTPUT SHOPPING CART')
            print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
            print(f'Number of Items: {ShoppingCart.get_num_items_in_cart(self)}\n')
            for i in self.cart_items:
                i.print_item_cost()
            print(f'\nTotal: ${ShoppingCart.get_cost_of_cart(self)}\n')


    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print(f'\nItem Descriptions')
        for i in self.cart_items:
            print(f'{i.item_name}: {i.item_description}')
        print()
    
def print_menu():
    allowed_characters = ['a', 'r', 'c', 'i', 'o', 'q']
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print('i - Output items\' descriptions')
    print('o - Output shopping cart')
    print('q - Quit')
    user_character = ''
    user_character = input('\nChoose an option:')
    while user_character not in allowed_characters:
        user_character = input('\nChoose an option:')
        if user_character in allowed_characters:
            break
    print()
    execute_menu(user_character)                           

def execute_menu(user_character):
    item_to_purchase = ItemToPurchase()
    if user_character == 'a':
        print('ADD ITEM TO CART')
        item_name = str(input('Enter the item name:\n'))
        item_description = str(input('Enter the item description:\n'))
        item_price = int(input('Enter the item price:\n'))
        item_quantity = int(input('Enter the item quantity:\n'))
        item_to_purchase = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        print()
        my_cart.add_item(item_to_purchase)
        print_menu()
    
    elif user_character == 'r':
        print('REMOVE ITEM FROM CART')
        Selected_input = input('Enter name of item to remove:\n')
        my_cart.remove_item(Selected_input)
        print_menu()


    elif user_character == 'c':
        my_cart.modify_item()
        print_menu()
       

    elif user_character == 'i':
        my_cart.print_descriptions()
        print_menu()


    elif user_character == 'o':
        my_cart.print_total()
        print_menu()


    elif user_character == 'q':
        return

if __name__ == "__main__":
    
    customer_name = input('Enter customer\'s name:\n')
    current_date = input('Enter today\'s date:\n')
    print(f'\nCustomer name: {customer_name}')
    print(f'Today\'s date: {current_date}\n')

    my_cart = ShoppingCart(customer_name, current_date)
    print_menu()
    
    
    
    