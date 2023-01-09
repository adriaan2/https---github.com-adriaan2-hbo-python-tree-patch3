def rec_print_folders(n: int, pref: str, root: list) -> None:
  Pref = pref.replace("-",">")
  print(f"{Pref}Folder_{n}")
  for i in root:
    if isinstance(i,str):
      print(pref,i)
    else:
      rec_print_folders(n+1,pref+"-",i)

def rec_count_files(root: list) -> int:
  res = 0
  for i in root:
    if type(i) == str:
      res += 1
    elif type(i) == list:
      res += rec_count_files(i)
  return res

if __name__ == "__main__":
    test_cases = [
        ['file_1', []],
        ['file_1', 'file_2', ['file_1']],
        ['file_1', 'file_2', ['file_3', 'file_4', 'file_5'], ['file_6', ['file_7', 'file_8'], ['file_9'], 'file_9', ['file_10']], []],
        ['file_1', ['file_3', ['file_2', ['file_10', ['file_9', 'file_8']]]], []],
        [[], [[], [[]]]]
    ]

    for case in test_cases:
        rec_print_folders(0, '', case)
        print('Number of files in case: ', case, ' is ', rec_count_files(case))
