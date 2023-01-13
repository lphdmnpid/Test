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
    
    def check(a):
        #Проверка
        try:
            int(a)
        except:
            print("TypeError")
            exit()
    
    ans=0
    for i in args:
        check(i)
        ans+=int(i)**2
    for i in kwargs.items():
        check(i[1])
        ans+=int(i[1])**2
    return ans

print(one(1,2,3,6,one=5,two=3))

three=two(one)
three(1,2,3,6,one=5,two=3)
one("four")
