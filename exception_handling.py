def ary(list):
    top=0
    for x in list:
        top+=x
    avg=top/len(list)
    return top,avg
try:
    limit=int(input("Enter the limit "))
    for i in (0,limit):
        a=ary([])
    print('total=(),average={}'.format(t,a))
except TypeError:
    print('type error.plz provide numbers')
except ZeroDivisionError:
    print("zero division error,plz don't give empty list")
