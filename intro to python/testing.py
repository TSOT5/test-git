speed = input("how fast do you want it to go med or fast?")

alien0 = {'xpos' : 0, 'speed': 'med' }

if speed.lower()[0] in 'm':
    alien0.update({'xpos' : 1, 'speed': 'med'})

if speed.lower()[0] in 'f':
    alien0.update({'xpos' : 2, 'speed': 'fast'})



print(alien0)