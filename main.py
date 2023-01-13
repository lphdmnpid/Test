def two(a):
    #Декоратор к one
    def dec(*args,**kwargs):
        ans=0
        for i in range(3):
            ans+=a(*args,**kwargs)
            print(i+1)
            print(ans)
    return dec

def one(*args,**kwargs):
    #Считает сумму квадратов
    ans=0
    for i in args:
        ans+=i**2
    for i in kwargs.items():
        ans+=i[1]**2
    return ans

print(one(1,2,3,6,one=5,two=3))

three=two(one)
three(1,2,3,6,one=5,two=3)
