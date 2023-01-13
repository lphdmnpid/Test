def one(*args,**kwargs):
    ans=0
    for i in args:
        ans+=i**2
    for i in kwargs.items():
        ans+=i[1]**2
    return ans

print(one(1,2,3,6,one=5,two=3))
