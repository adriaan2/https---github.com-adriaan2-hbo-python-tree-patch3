""
date_entry = input('')
year, month, day = map(int, date_entry.split('-'))
months_31= [1,3,5,7,8,10,12]
months_30=[4,6,9,11]
month1=month+1
day2=day+1

if month==2 and day2>28  :
     month=month+1  
     day2=day2-28
     print(day)
     
if month in months_31 and day2>31:
  month=month+1   
  day2=day2-31

if month in months_30 and day2>30:
    month=month+1
    day2=day2-30
    
if month>12:
    year=year+1
    month=month-12

print("Next date:" + str(year) + "-" + str(month).zfill(2) + "-" + str(day2).zfill(2))
    
