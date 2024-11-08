class KgToPounds:
    def __init__(self, kg):
        self._kg = kg

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self._kg = new_kg
        else:
            raise ValueError('килограммы задаются только числами')

    def to_pounds(self):
        return self._kg * 2.205

try:
    weight = float(input("введите вес в килограммах: "))
    converter = KgToPounds(weight)
    print(f"вес в фунтах: {converter.to_pounds()}")
except ValueError as e:
    print(e)