def dtob(dec):
    if(dec>1):
        dtob(dec//2)
        print dec%2
if __name__=='__main__':
    dec=int(input("Enter a decimal number "))
    dtob(dec)
