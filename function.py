tom_exp_list = [2300,3400,1233]
joe_exp_list = [233,455,344]

"""total = 0
for item in tom_exp_list:
    total = total+item
print("toms total expenses:",total)

total = 0
for item in joe_exp_list:
    total = total+item
print("joes total expenses:",total)
"""
#we can also write it using function
print("we can also write it using function as")
def calculate_total(exp):
    total = 0
    for item in exp:
        total = total+item
    return total

tom_exp_list = [2300,3400,1233]
joe_exp_list = [233,455,344]

toms_total = calculate_total(tom_exp_list)
joes_total = calculate_total(joe_exp_list)
print("toms total expenses:",toms_total)
print("joes total expenses:",joes_total)

#ex2
def sum(a,b):
    total=a+b
    return total

n = sum(5,6)
print("Total:",n)
