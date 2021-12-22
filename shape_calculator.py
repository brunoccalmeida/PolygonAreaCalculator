class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
        self.height = height
        return self.height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2*self.width + 2*self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        with open('rectangle.txt', 'w+') as fh:
            fh.write(f'{"*"*self.width}\n')
            return fh.read()

    def get_amount_inside(self):
        pass


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.height = side
        self.width = side

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self, side_length):
        self.side = side_length
        return self.side

    def set_width(self, width):
        self.width = width
        self.height = width
        self.side = width
        return self.side

    def set_height(self, height):
        self.width = height
        self.height = height
        self.side = height
        return self.side


if __name__ == '__main__':
    rectangle = Rectangle(5,4)
    print(rectangle.get_picture())
