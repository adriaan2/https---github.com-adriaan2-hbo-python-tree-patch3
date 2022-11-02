string="abcderfgtreergrefefrgtr"
Hashmap = list(string)
    
    keys = []
    values = []
    i = 0
    #
    while (i < len(Hashmap)):
        if i % 2 == 0:
            keys.append(Hashmap[i])
        else:
            values.append(Hashmap[i])
            i += 1
    
    Hashdict = dict()
    j = 0
    while j < len(keys):
        if (j < len(values)):
            Hashdict.update({keys[j]: values[j]})
        else:
            Hashdict.update({keys[j]: None})
        j += 1