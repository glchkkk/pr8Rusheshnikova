class Nikola:
    def __init__(self, name, age):
        if name == "Николай":
            self._name = name
        else:
            self._name = f"Я не {name}, а Николай"

        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def __setattr__(self, key, value):
        if key in ('_name', '_age'):
            super().__setattr__(key, value)
        else:
            raise AttributeError(f"нельзя добавлять новый атрибут '{key}'")

    def __repr__(self):
        return f"Nikola(name='{self._name}', age={self._age})"

if __name__ == "__main__":

    user_name = input("введите ваше имя: ")
    user_age = int(input("введите ваш возраст: "))

    person = Nikola(user_name, user_age)
    print(person) 

    try:
        person.patronymic = "Иванович" 
    except AttributeError as e:
        print(e)