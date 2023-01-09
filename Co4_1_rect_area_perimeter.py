class rect():
    def __init__(self,l,b):
        self.length = l
        self.breath = b

    def rect_area(self):
        return self.length*self.breath

    def rect_perimeter(self):
        return 2*(self.breath+self.breath)


l1 = float(input("Enter the length :"))
b1 = float(input("Enter the breath :"))
l2 = float(input("Enter the length :"))
b2 = float(input("Enter the breath :"))
obj1 = rect(l1,b1)
obj2 = rect(l2,b2)
print("Area is :{} perimeter is :{}".format(obj1.rect_area(),obj1.rect_perimeter()))
print("Area is :",obj2.rect_area()," perimeter is :",obj2.rect_perimeter())
print(obj1.rect_area()>obj2.rect_area())
