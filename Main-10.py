class Rectangle:
 def __init__(self, Height=0, Width= 0):
   self.Height= Height
   self.Width= Width
 def getHeight(self):
   return self.Height
 def getPerimeter(self):
   return 2 * self.Height + 2 * self.Width
 
 def getWidth(self):
   return self.Width
 
 def getArea(self):
   return self.Height * self.Width
 
class Square(Rectangle):
 def __init__(self,side= 0):
   Rectangle.__init__(self,side,side)
 
 
def main():
 print("Rectangle Calculator")
 
 while True:
    choice =input("Rectangle or square? (r/s):")
    if choice == "r":
        h= int(input("Height:"))
        w = int(input("Width:"))
        r = Rectangle(h,w)
        print("Perimeter:",r.getPerimeter())
        print("Area:",r.getArea())
        print()
    else:
        side = int(input("Length:"))
        s = Square(side)
        print("Perimeter:",s.getPerimeter())
        print("Area:",s.getArea())
        print()
    state = input("Continue? (y/n):")
    if state == "n":
        print("Thank you for using my app")
        break
    

main()
