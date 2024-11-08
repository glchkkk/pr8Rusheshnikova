class RealString:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError('значение должно быть строкой')
        self.value = value

    def __len__(self):
        return len(self.value)

    def __gt__(self, other):
        if isinstance(other, str):
            return len(self.value) > len(other)
        elif isinstance(other, RealString):
            return len(self.value) > len(other.value)
        else:
            return NotImplemented

if __name__ == "__main__":
    str1 = RealString(input("введите первую строку: "))
    str2 = input("введите вторую строку: ")

    if str1 > str2:
        print(f"{str1.value} длиннее, чем {str2}")
    elif str1 < str2:
        print(f"{str1.value} короче, чем {str2}")
    else:
        print(f"{str1.value} и {str2} одинаковой длины")