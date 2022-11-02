
class ShapeFactory:
    def createShape(name):
        if name == 'circle':
            return Circle()
        elif name == 'square':
            return Square()
        elif name == 'line':
            return Line()
        else:
            raise ValueError("Invaild name", name)


class Shape:
    @staticmethod
    def create(name):
        # TODO: Fill the code here
        # NOTE: Raise `ValueError("Invalid name", name)` if there is no such shape.
        shape = ShapeFactory.createShape(name)
        return shape

class Circle(Shape):
    def draw(self):
        print("ㅇ")


class Square(Shape):
    def draw(self):
        print("ㅁ")


class Line(Shape):
    def draw(self):
        print("ㅡ")


if __name__ == "__main__":
    x = Shape.create("circle")
    x.draw()
    x = Shape.create("square")
    x.draw()
    x = Shape.create("line")
    x.draw()

    # Expected Output
    # > ㅇ
    # > ㅁ
    # > ㅡ
