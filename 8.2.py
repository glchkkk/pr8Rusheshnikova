class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not (isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)) and isinstance(self.c, (int, float))):
            return "Нужно вводить только числа!"

        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "С отрицательными числами ничего не выйдет!"

        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return "ура можно построить треугольник!"
        else:
            return "жаль но из этого треугольник не сделать(("

def main():
    try:
        a = float(input("введите длину первой стороны: "))
        b = float(input("введите длину второй стороны: "))
        c = float(input("введите длину третьей стороны: "))
    except ValueError:
        print("нужно вводить только числа!")
        return

    triangle_checker = TriangleChecker(a, b, c)
    result = triangle_checker.is_triangle()
    print(result)

if __name__ == "__main__":
    main()