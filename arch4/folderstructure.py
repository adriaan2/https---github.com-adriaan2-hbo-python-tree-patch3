def rec_print_folders(n:int,pref:str,root:list)->None:
    if any(case):
           for i in case:
               if any(i):
                print("test")
          
    else:
           print(case)
def rec_count_files(root:list)->int:
    numberoffolders=0
    if case =='[]':
        rec_count_files()
    else:
        numberoffolders+=1

        
    return numberoffolders

    

	# todo: implement the body of this function

test_cases =[
    ['file_1',[]] ,
    ['file_1','file_2',['file_1']] ,
    ['file_1','file_2',['file_3','file_4','file_5'],['file_6',['file_7','file_8'],['file_9'],'file_9',['file_10']],[]] ,
    ['file_1',['file_3',['file_2',['file_10',['file_9','file_8']]]],[] ],
    [[],[[],[[]]]] 
    ]
for case in test_cases:
    rec_print_folders(0,'',case)

    print('Number of files in case: ',case, ' is ',rec_count_files(case))


