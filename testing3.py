class Name:
    def __init__(self, name, hobby='') -> None:
        if name not in ["Дашуля", "Андрій", "Анонім"]:
            raise ValueError("Дозволені імена: Богдан, Анонім")
        if hobby == '':
            raise ValueError("Хобі не може бути пустим")

        self.name = name
        self.hobby = hobby


a = Name("Андрій", "Спорт, Їсти, Серіали, Маму і Тата")
b = Name("Андрій")