
# num=46
# if (num % 2) == 0:

#               print("even")

# else:

#               print("The provided number is odd")




hashmap_key_value={}

x=False
while  not x:
   key=input("an even number of letters")
   if len(key)%2==0:
    x=True

i=0 
while i<len(key):
    hashmap_key_value.update({key[i]:key[i+1]})
    i+=2

# def encode_string(data: str, key: str = None) -> str:
#   if key == None:
    
#     key=hashmap_key_value
#   res = ""
#   for i in data:
#     temp = key.index(i)
#     res += key[temp+1]
#   return res


# def decode_string(data: str, key: str = None) -> str:
#   if key == None:
#      pass
#   res = ""
#   for i in data:
#     temp = key.index(i)
#     res += key[temp-1]
#   return res


