password = 'abcd1234'
count = 0
while True:
    a = input('Enter your password:')
    if a == 'abcd1234':
        print('Welcome')
        break
    if a != 'abcd1234':
        print('Incorrect Password, try again')
        count += 1
    if count >= 5:
        print('Too many wrong attempts, please try later')
        break