


import os

import sys




def load_txt_file(file_name):
    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            file_content.append(line.split())
            temperature=convert_to_dict(file_content)
        

def convert_to_dict(file_content):
    temp_dict = {}
    for line in file_content:
        if line[2] not in temp_dict:
            temp_dict[line[2]] = {}
        if line[0] not in temp_dict[line[2]]:
            temp_dict[line[2]][line[0]] = []
        temp_dict[line[2]][line[0]].append(float(line[-1]))
    print(temp_dict[0])

 

if __name__ =="__main__":
    load_txt_file('NLAMSTDM.txt')
    