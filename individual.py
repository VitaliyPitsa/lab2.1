import math
print("введите основания трапеции")
osn1=float(input())
osn2=float(input())
print("введите угол при большем основании трапеции")
ugol=float(input())
S =1/2*(osn1**2+osn2**2)*((math.sin(ugol)*math.sin(ugol))/(math.sin(2*ugol)))
print(S)
