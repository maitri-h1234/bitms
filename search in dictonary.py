'''my_dict={'apple':10,'banana':20,'angle':30,'balaji':40,'chennai':100,'zebra':120}
for key,value in my_dict.items():
    if key[0].lower()=='b':
        print(f"the value of'{key}'is {value}")'''

d={'A':1,'B':2,'c':3}
key=input("enter key to check:")
if key in d.keys():
    print("key is present and value of the key is:")
    print(d[key])
else:
    print("key is not present:")