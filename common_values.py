# Write a Python function that takes two lists and returns True
#if they have at least one common member

def common(list1,list2):
    result=False
    for a in list1:
        for b in list2:
            if a==b:
                result=True
                return result
print(common([1,2,3,4],[4,7,8,9]))
print(common([1,2,3,4,5],[6,7,8,9]))
