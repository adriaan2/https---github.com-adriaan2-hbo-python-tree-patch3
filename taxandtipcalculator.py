Cost_of_Meal  = float((input()))
Tax = 0.21 * Cost_of_Meal
Tip = 0.15 * Cost_of_Meal
Total_Amount = Tax + Tip + Cost_of_Meal
result=round(Total_Amount,3)
print("Tax:",Tax,",""Tip:",Tip,",","Total:",result)

