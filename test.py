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
test=""
for i in hashmap_key_value:
  test+=hashmap_key_value[i]
print(test)

def encode_string(data: str, key: str = None) -> str:

  
 pass
  # if key == None:
  #    key=test  
  # res = ""
  # for i in data:
  #   temp = key.index(i)
  #   res += key[temp+1]
  # return res

#encode_string(test)

def decode_string(data: str, key: str = None) -> str:
  if key == None:
     pass
  res = "test"
  for i in data:
    temp = key.index(i)
    res += key[temp-1]
  return res