name=input("Enter your name: ")
m=int(input("Enter your marks:"))
if(m>=90):
    grade= "A grade"
elif(80<=m<=89):
    grade= "B grade"
elif(70<=m<=79):
    grade= "C grade"
elif(60<=m<=69):
    grade= "D grade"
else:
    grade= " Fail"
print(grade)
