def auto_service(first, second):
    if first == '-':
        print(f'Service 1: No service')
    else:
        print(f'Service 1: {first}, ${services.get(first)}')
    if second ==  '-':
        print(f'Service 2: No service')
    else:
        print(f'Service 2: {second}, ${services.get(second)}')

services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}

print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

first_service = input('Select first service:\n')
second_service = input('Select second service:\n')

print("\nDavy's auto shop invoice\n")
auto_service(first_service, second_service)
print(f'\nTotal: ${services.get(first_service) + services.get(second_service)}')
