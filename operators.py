#arithmetic operator
num1 =int(input('Enter a first no:'))
num2 =int(input('Enter second no:'))
mod= num1 % num2
mul= num1 * num2
add= num1 + num2
suc= num1 - num2
div = num1 / num2
exp = num1 ** num2
print(' mod of two no is:',mod)
print(' multiply of two no is:',mul)
print(' addition of two no is:',add)
print(' substraction of two no is:',suc)
print(' divition of two no is:',div)
print(' exponential of two no is:',exp)
#relational operator
print(num1>num2)
print(num1<num2)
print(num1!=num2)
print(num1>=num2)
print(num1<=num2)
print(num1==num2)
#logical operator
x=True
y=False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)
#bitwise operator
print('Bitwise and of x and y is',x&y)
print('Bitwise or of x and y is',x|y)
print('Bitwise not of x is',~x)
print('Bitwise xor of x and y is',x^y)
print('Bitwise 2 right shift of x  is',x>>y)
print('Bitwise 2 left shift of x  is',x<<y)

#assignment operator
x=4
print('the x value is ',x)
x+=4
print('additional assignment of x', x)
x-=4
print('Subtraction assignment of x', x)
x*=4
print('multiplicational assignment of x',x)
x/=4
print('divitional assignment of x ',x)
x%=4
print('modules assignment of x ',x)
x=4
x//=4
print('floor divitional assignment of x',x)
x=4
x**=4
print('exponential assignment of x',x)
#identity operators
print('~identity operator')
x=4
y=4
print(x is not y)
print(x is y)
#membership operator
x='Boomer friend'
print('B' in x)
print('2' in x)
print('2' not in x)
