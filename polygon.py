class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):

        if self.width >= 50 or self.height >= 50:
            return 'Too big for picture.'
        else:

            shape = ''

            for h in range(self.height):
                for w in range(self.width):
                    shape += '*'

                shape += '\n'

            return shape

    def get_amount_inside(self, otherShape):

        fitsHorizontally = int(self.width / otherShape.width)
        fitsVertically = int(self.height / otherShape.height)

        return fitsHorizontally * fitsVertically



    def __str__(self):
        return f'Rectangle(width={str(self.width)}, height={str(self.height)})'



class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'



rect = Rectangle(10, 5)
rect.set_width(7)
rect.set_height(3)
print(rect.get_picture())



# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)