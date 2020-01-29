import random
A=['A','B','C','D']
a=random choice(A)
for i in range(5):
    b=input('')
    if a==b:
        print('win')
    else:
        print('try again')
print('lost')
