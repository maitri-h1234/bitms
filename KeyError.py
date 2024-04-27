'''a=int(input())
myDict={1:10,2:20,3:30}
print("the dictionary is:",myDict)
#print(myDict[a])

if a>3:
    raise KeyError('keys errors raised by your end')
'''
myDict={1:10,2:20,3:30}
print("the dictionary is:",myDict)
key=3
print("key is:",key)
try:
    val=myDict[key]
    print("value associated to the key is:",val)
except KeyError:
    print("key not present in the dictionary")
      


