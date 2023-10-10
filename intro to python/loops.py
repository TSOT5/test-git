my_list = ["apple", "banana", "orange", "spinach", "kale", "curry", "potatoes"]

urgent_list = []

for item in my_list:
    if item[0] in ['a','b', 'c']:
        urgent_list.append(item)
    else:
        continue

my_groveries = [item for item in my_list if item[0] in ['a','b', 'c']]
print(my_groveries)

print(urgent_list)

#very important
my_info = [x + 1 for x in range(20) if x % 2 == 0]
print(my_info)

for i in my_list:
    print(i)
    break
    print("yeah")
    




#letter_to_check = input("what letter to check")

#counter = 0

#for item in my_list:
    #if item[0] == letter_to_check:
       # print(item)
   #else:
       # print("nothing")
    #counter += 1
    #print(counter)


#for i in range(0,20**2,15):
#    print(i)