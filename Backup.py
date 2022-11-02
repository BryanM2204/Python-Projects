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
    
    def add_items(self, item_name):
        self.cart_items = cart_items.append(item_name)
    
    def remove_item(self, item_name):
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
                
                if i != item_name:
                    continue
            else: 
                print('Item not found in cart. Nothing modified')\
    
    #def get_num_items_in_cart(self):
        
    #def get_cost_of_cart(self):
        
    #def print_total(self):
        
    #def print_descriptions(self):
        #print(self.item_description)
    
    def print_menu(self):
        allowed_characters = ['a', 'r', 'c', 'i', 'o', 'q']
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
                
        user_character = input('\nChoose an option:')
        flag=0
        for i in allowed_characters:
            if i==user_character:
                flag=1
                break
            elif i != user_character:
                user_character = input('\nChoose an option:')
        if flag==1:
            item1.execute_menu(user_character, cart_items)
                
    #def execute_menu(user_character, cart_items):
   
        

                
            
if __name__ == "__main__":
    
    customer_name = input('Enter customer\'s name:\n')
    current_date = input('Enter today\'s date:\n')
    print(f'\nCustomer name: {customer_name}')
    print(f'Today\'s date: {current_date}\n')

    item1 = ItemToPurchase()
    item1 = ShoppingCart()

    item1.print_menu()
    