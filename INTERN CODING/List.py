#length

num=[10,0,-1,7,8,10,-67]
print(len(num)) 

print(num[1:4])

#Sorting

num.sort()
print(num)

#reversing

num.reverse()
print(num)

#minimum

print(min(num))

#maximum

print(max(num))

#adding

num.append(45)

#inserting

num.insert(2,45)
print(num)

#extending

num.extend([45,56,87,90])
print(num)

#making changes in given ist

num[3]=89
print(num)

num[1:4]=[45,46,47]
print(num)

#remove

num.remove(45)
print(num)

#pop

num.pop()
print(num)
