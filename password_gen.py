word = input('Enter a word to generate a password:')
password = ''

list_letters = {'i': '1', 'a': '@', 'm': 'M', 'B': '8', 's': '$', 'o': '0', 'O': '0'}

for i in word:
    if i in list_letters:
        new_letter = list_letters.get(i)
        password += new_letter
    else:
        password += i

print(password + '!')