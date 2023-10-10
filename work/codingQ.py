#Question 1

def hello_name(user_name):
    user_name = input("What is your name? ")
    print ("hello_",user_name + "!")

#Question 2

def first_odds():
    for x in range (1,101,2):
        print (x)
    return
    
#Question 3

def max_num_in_list(a_list):
    number = max(a_list)
    return number

#Question 4

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0:
            return True
    return False

#Question 5
a_list = [1,2,3,4,5,6,7,8,9,10,11]
def is_consecutive(a_list):
    
    return a_list == list(range(a_list[0], a_list[-1]))

print(is_consecutive(a_list))