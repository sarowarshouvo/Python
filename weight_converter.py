weight = int(input("Weight: "))
unit= input("(K)g or (L)bs: ")
if  unit.upper()== 'K':
    sum = float(weight*2.20)
    print(f'Weight in kg:{sum}')
else:
    sum=float(weight*0.45)
    print(f'Weight in lb:{sum}')





