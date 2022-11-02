highway_number = int(input())

def classify_highway(number):
    if number < 100 and number > 0:
        if number % 2 == 0: 
            print(f'I-{number} is primary, going east/west.')
        else:
            print(f'I-{number} is primary, going north/south.')
    elif number > 99 and number < 1000:
        if number % 2 == 0 and number % 100 != 0:
            print(f'I-{number} is auxiliary, serving I-{number % 100}, going east/west.')
        elif number % 2 != 0 and number % 100 != 0:
            print(f'I-{number} is auxiliary, serving I-{number % 100}, going north/south.')
        elif number % 100 == 0:
            print(f'{number} is not a valid interstate highway number.')
    

Highway = classify_highway(highway_number)

print(Highway.strip(Highway))