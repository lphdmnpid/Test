'''
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
'''
class Item:
    def __init__(self,name,end,priority):
        self.__name=name
        self.__end=end
        self.__priority=priority

    def Change(self,**kwargs):
        for n,i in kwargs.items():
            if n=="name":
                self.__name=i
            if n=="end":
                self.__end=i
            if n=="priority":
                self.__priority=i
    
    @property
    def Deal(self):
        print(f"Название: {self.__name}")
        print(f"Сделать до {self.__end}")
        print(f"Приоритет: {self.__priority}")

class ItemList:
    def __init__(self):
        self.deals=[]
    
    def add(self,*args):
        if len(args)==3:
            self.deals.append(Item(*args))
        else:
            print("Нужно ровно 3 аргумента.")
    
    def GetAll(self):
        for i in self.deals:
            i.Deal
    
    def GetDate(self,date):
        for i in self.deals:
            if i.__end==date:
                i.Deal
    
    def GetPriority(self,priority):
        for i in self.deals:
            if i.__priority<=priority:
                i.Deal

    def dl(self,index):
        try:
            self.deals.pop(int(index))
        except:
            print("Неверный ввод.")
    
    def Change(self,index,**kwargs):
        try:
            self.deals[int(index)].Change(**kwargs)
        except:
            print("Неверный ввод.")

a=Item("Олимпиада","15.01.23","10")
a.Deal
al=ItemList()
al.add("Олимпиада","15.01.23","10")
al.GetAll()










