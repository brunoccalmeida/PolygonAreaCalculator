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
            if self.width > 50 or self.height > 50:
                return f'Too big for picture.'
            for h in range(self.height):
                fh.write(f'{"*"*self.width}\n')
                fh.read().rstrip('\n')
        with open('rectangle.txt', 'r+') as file_handler:
            return file_handler.read()

    def get_amount_inside(self, shape):

        if isinstance(shape, Square) and isinstance(self, Square):
            side = self.width // shape.side
            return side**2

        elif isinstance(shape, Square) and isinstance(self, Rectangle):
            height = self.height // shape.side
            width = self.width // shape.side
            return height * width

        elif isinstance(shape, Rectangle) and isinstance(self, Square):
            height = self.height // shape.height
            width = self.width // shape.width
            return height * width

        elif isinstance(shape, Rectangle) and isinstance(self, Rectangle):
            height = self.height // shape.height
            width = self.width // shape.width
            return height * width


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.height = side
        self.width = side

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self, side):
        self.side = self.width = self.height = side
        return self.side

    def set_width(self, width):
        self.width = self.height = width
        self.side = width
        return self.side

    def set_height(self, height):
        self.width = self.height = height
        self.side = height
        return self.side


if __name__ == '__main__':
    square = Square(2)
    big_square = Square(8)
    print(big_square.get_amount_inside(square))
