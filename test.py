
hashmap_key_value={}
key=input("an even number of letters")
i=0 
while i<len(key):
    hashmap_key_value.update({key[i]:key[i+1]})
    i+=2
    
print(hashmap_key_value)