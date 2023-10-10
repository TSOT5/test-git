# x = 0

# flag = True

# while flag:
#     print(x)
#     x += 17
#     if x > 100:
#         flag = False

while True:
    myname = input("What is your name \n")
    if myname.lower() == 'quit':
        break
    elif myname.lower()[0] in 'abcdefg':
        print('please go to table 1')
    elif myname.lower()[0] in 'hijklmnop':
        print('Please go to table 2')
    elif myname.lower()[0] in 'qrstuvwxyz':
        print('please go to table 3')
    

# for letter in 'ye man':
#     print(letter)