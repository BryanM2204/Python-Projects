class ItemToPurchase:
    
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        
    def print_item_cost(self):
        self.item_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_cost}')
    
    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')
        
class ShoppingCart:
    
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
    def add_item(self):
        print('ADD ITEM TO CART')
        self.item_name = input('Enter the item name:\n')
        self.item_description = input('Enter the item description:\n')
        self.item_price = int(input('Enter the item price:\n'))
        self.item_quantity = int(input('Enter the item quantity:\n'))
        self.cart_items.append(ItemToPurchase(self.item_name, self.item_price, self.item_quantity, self.item_description))

    def remove_item(self, item_name, cart_items):
        for i in self.cart_items:
            if i == item_name:
                self.cart_items = cart_items.remove(item_name)
                if i != item_name:
                    continue
            else:
                print('Item not found in cart. Nothing removed.')
    
    def modify_item(self, item_quantity):
        for i in self.cart_items:
            if i == self.item_name:
                
                if i != self.item_name:
                    continue
            else: 
                print('Item not found in cart. Nothing modified')
    
    def get_num_items_in_cart(self):
        total = 0
        for i in self.cart_items: 
            total += i.item_quantity
        return total
        
    def get_cost_of_cart(self):
        total_cost = 0
        for i in self.cart_items:
            print(f'{i.item_name} {i.item_quantity} @ ${i.item_price} = ${i.item_quantity * i.item_price}')
            total_cost += i.item_quantity * i.item_price
        return total_cost
        
    def print_total(self):
        print('\nOUTPUT SHOPPING CART')
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print(f'Number of Items: {ShoppingCart.get_num_items_in_cart(self)}\n')
        if self.total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        print(f'\nTotal: ${ShoppingCart.get_cost_of_cart(self)}')

    #def print_descriptions(self):
        #print(self.item_description)
    
    def print_menu(self, user_cart):
        allowed_characters = ['a', 'r', 'c', 'i', 'o', 'q']
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
        user_character = ''
        user_character = input('\nChoose an option:\n')
        while user_character not in allowed_characters:
            user_character = input('Choose an option:\n')
            if user_character in allowed_characters:
                break
        self.execute_menu(user_character, user_cart)
        
                
    def execute_menu(self, user_character, user_cart):

        if user_character == 'a':
            user_cart.add_item()
            self.print_menu(user_cart)

        elif user_character == 'o':
            self.print_total()
            self.print_menu(user_cart)

if __name__ == "__main__":
    
    customer_name = input('Enter customer\'s name:\n')
    current_date = input('Enter today\'s date:\n')
    print(f'\nCustomer name: {customer_name}')
    print(f'Today\'s date: {current_date}\n')

    user_cart = ShoppingCart(customer_name, current_date)
    user_cart.print_menu(user_cart)
    
    
    
    