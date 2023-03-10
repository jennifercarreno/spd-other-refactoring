# by Kami Bigdely
# Extract superclass.

class Shape:
    def __init__(self, x,y, visible = True):
        self.x = x
        self.y = y
        self.visible = visible
    
    def hide(self):
        self.visible = False

    def make_visible(self):
            self.visible = True
    
    def display(self):
        print('drew the shape.')

class Circle(Shape):
    
    def __init__(self, x, y, visible, r):
        super().__init__(self, x, y, visible)
        self.center_x = x
        self.center_y = y
        self.r = r
        self.visible = True
        
    def get_center(self):
        return self.center_x, self.center_y
    
    
class Rectangle(Shape):
    
    def __init__(self, x, y, visible, width, height):
        super().__init__(self, x, y, visible)

        # left-bottom corner.
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = visible
        
    def get_center(self):
        return self.x + self.width/2, \
               self.y + self.height/2 



if __name__ == "__main__":
    circle = Circle(0,0, False, 10)
    circle.make_visible(True)
    circle.display()
    print('center point',circle.get_center())

    rect = Rectangle(10, 10, True, 20, 5)
    rect.hide()
    rect.display() # does not display because it's hidden.
    rect.make_visible()
    rect.display()
    print('center point',rect.get_center())