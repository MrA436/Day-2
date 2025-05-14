a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=input(('choose operation: +, -, *, /: ' ))
if c == '+':
    d= print(a+b)
elif c == '-':
    if a>b:
        d= print(a-b)
    else:
        d= print(b-a)
elif c == '*':
    d= print(a*b)
else:
    d= print(a/b)
print(d)