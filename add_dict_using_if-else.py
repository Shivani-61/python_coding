#Write a Python program to combine two dictionary by adding values for common keys.
#d1 = 0a 0 : 100, 0 b 0 : 200, 0 c 0 : 300 d2 = 0a 0 : 300, 0 b 0 : 200, 0 d 0 : 400
#Sample output: Counter( 0a 0 : 400, 0 b 0 : 400, 0 d 0 : 400, 0 c 0 : 300)

dict1 = {'a':100,'b':200,'c':300}
dict2 = {'a':300,'b':200,'d':400}
for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
    else:
        pass      
print(dict1 and dict2)
