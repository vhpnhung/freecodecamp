class Rectangle():

    def __init__(self, height=10, width=5):
        self.height = height
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def set_width(self, width):
        self.width = width     
    
    def get_area(self):
        self.area = self.height*self.width
        return self.area

    def get_perimeter(self):
        self.area = (self.height+self.width)*2
        return self.area

    def get_diagonal(self):
        self.area = (self.height**2+self.width**2)**0.5
        return self.area
    
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big to be illustrated"
        else:
            for _ in range(self.height):
                print("*"*self.width)

    def get_amount_inside(self, h, w):
        if h>self.height or w>self.width:
            return 0
        else:
            return int(self.height/h)*int(self.width/w)
    



class Square(Rectangle):
    def __init__(self, side=9):
        self.height = self.width = side

    def set_side(self, side):
        self.height = self.width = side

    def set_height(self, height):
        self.height = self.width = height
    
    def set_width(self, width):
        self.height = self.width = width 