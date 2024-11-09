class Figure:
    unit = "cm"  # Атрибут уровня класса, единица измерения величин

    def __init__(self):
        pass

    def calculate_area(self):
        # Нереализованный метод для подсчета площади
        raise NotImplementedError("Метод calculate_area должен быть реализован в подклассе")

    def info(self):
        # Нереализованный метод для вывода информации о фигуре
        raise NotImplementedError("Метод info должен быть реализован в подклассе")


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()  # Вызов конструктора родительского класса
        self.__side_length = side_length  # Приватный атрибут для длины стороны квадрата

    def calculate_area(self):
        # Площадь квадрата = сторона * сторона
        return self.__side_length ** 2

    def info(self):
        # Вывод информации о квадрате: длина стороны и площадь
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{Figure.unit}, area: {area}{Figure.unit}²")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()  # Вызов конструктора родительского класса
        self.__length = length  # Приватный атрибут для длины прямоугольника
        self.__width = width    # Приватный атрибут для ширины прямоугольника

    def calculate_area(self):
        # Площадь прямоугольника = длина * ширина
        return self.__length * self.__width

    def info(self):
        # Вывод информации о прямоугольнике: длина, ширина и площадь
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, area: {area}{Figure.unit}²")


# В исполнении кода создаем список фигур (квадраты и прямоугольники)
if __name__ == "__main__":
    # Создаем объекты квадратов
    square1 = Square(side_length=5)
    square2 = Square(side_length=7)

    # Создаем объекты прямоугольников
    rectangle1 = Rectangle(length=5, width=8)
    rectangle2 = Rectangle(length=10, width=3)
    rectangle3 = Rectangle(length=6, width=12)

    # Список всех объектов
    figures = [square1, square2, rectangle1, rectangle2, rectangle3]

    # Вызов метода info у каждого объекта из списка
    for figure in figures:
        figure.info()
