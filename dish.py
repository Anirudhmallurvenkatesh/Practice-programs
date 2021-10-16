indian = ["samosa","curry","naan"]
chinese = ["egg roll","pot sticker","fried rice"]
itialian = ["pasta","pizza","risorto"]
dish = input("enter the dish")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in itialian:
    print("itialian")
else:
    print("Based on the little knowledge i have,i dont which dish is:",dish)
