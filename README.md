#  Звіт до роботи Lab5

##  Тема: Тестування

---

###  Виконання роботи:

###  Перевірка assert

- Я зробив простеньку програму з тестами assert:

```py
year =  input ( ' Введіть свій рік народження -> ' )
assert year.isdigit(), f ' Ви впевнені, що це " { year } " число ?) '
вік =  2022  -  int (рік)
pib =  вхід (
    ' Введіть Прізвище Ім'я по Батькові (через пробіл, з великої літери) -> ' )
список  = pib.split()
для елемента в  списку :
    assert item.istitle(), f ' Хоче ви допустили помилки у слові " { item } " '
print ( f ' Вітаю { pib } , цього року вам буде (або вже є) { age } років ))) ' )
```

Ось що буде виводитись, якщо написати все правильно:

```
Введіть свій рік народження -> 2003
Введіть Прізвище Ім'я по Батькові (через пробіл, з великої літери) -> Михайлович Андрій Васильович
Вітаю Михайлович Андрій Васильович, цього року вам буде (або вже є) 19 років )))
```

Якщо ввести не число (типу int) до першої перевірки видасть таку помилку:

```
Введіть свій рік народження -> текст)
AssertionError: Ви впевнені, що це "текст)" число ?)
```

Якщо ввести правильне число, але ввести слово з маленької літери:

```
Введіть свій рік народження -> 1999
Введіть Прізвище Ім'я по Батькові (через пробіл, з великої літери) -> дашуля
AssertionError: Хоче ви допустили помилки у слові "дашуля"
```

<span style='color: rgba(255, 255, 255, 0.2)'>Дашуля пишеться з великої<span>


```
малюнок класу:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник",
                        "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = тип
        self.length = довжина
    def print_figure(self):
        return f'Фігура {self.type} з cтороною {self.length}'
спробуйте:
    figure1 = Figure("квадрат", 2)
    print(f'Фігура 1 - {figure1.print_figure()}')
крім AssertionError як err:
    print(f'Фігура 1 - {err}')
спробуйте:
    figure2 = Figure("прямокутник", 0)
    print(f'Фігура 2 - {figure2.print_figure()}')
крім AssertionError як err:
    print(f'Фігура 2 - {err}')
спробуйте:
    figure3 = Figure("трикутник", -42)
    print(f'Фігура 3 - {figure3.print_figure()}')
крім AssertionError як err:
    print(f'Фігура 3 - {err}')
спробуйте:
    figure4 = Figure("трикутник", 15)
    print(f'Фігура 4 - {figure4.print_figure()}')
крім AssertionError як err:
    print(f'Фігура 4 - {err}')
спробуйте:
    figure5 = Figure("трапеція", 100)
    print(f'Фігура 5 - {figure5.print_figure()}')
крім AssertionError як err:
    print(f'Фігура 5 - {err}')
```

Ось що виводить:

```
Фігура 1 - Фігура квадрат з cтороною 2
Фігура 2 - Довжина має бути більшою за 0!
Фігура 3 - Довжина має бути більшою за 0!
Фігура 4 - Фігура трикутник з cторoною 15
Фігура 5 - Дозволені фігури: квадрат, прямокутник, трикутник
```


```
Назва класу:
    def __init__(self, name, hobby='') -> None:
        якщо ім’я не на ["Дашуля", "Стасік", "Анонім"]:
            raise ValueError("Дозволені імена: Дашуля, Анонім")
        якщо хобі == '':
            raise ValueError("Хобі не можна бути пустим")
        self.name = ім'я
        self.hobby = хобі
a = Name("Стасік", "Спорт, Їсти, Серіали, Маму і Тата")
b = Ім'я("Стасік")
```

тут видно, що при ініціалізації `а` все норм, але при анаціалізації `b` видає помилку, бо хобі не зазначено

```
Traceback (останній останній виклик):
  Файл "D:\Labs\Labs 3.1\ООП\github\OOP\Lab5\testing3.py", рядок 13, у <module>
    b = Ім'я("Юрій")
  Файл "D:\Labs\Labs 3.1\ООП\github\OOP\Lab5\testing3.py", рядок 6, в __init__
    raise ValueError("Хобі не можна бути пустим")
ValueError: Хобі не можна бути пустим
```

##  Юніт тести

- Я ввів код і запустив, ось що получилось:

```
==================================================== =====================
ПОМИЛКА: setUpClass (__main__.TestFigure)
-------------------------------------------------- --------------------
TypeError: у TestFigure.setUpClass() відсутній 1 обов’язковий позиційний аргумент: 'cls'
-------------------------------------------------- --------------------
Виконано 0 тестів за 0,000 с
ПОМИЛКА (помилки=1)
```



app.py

```py
 малюнок класу :
    FIGURES  = [ " квадрат " , " прямокутник " , " трикутник " ]
    КОЛЬОРИ  = [ " червоний " , " зелений " , " синій " ]
    def  __init__ ( self , type , length , color = ' 0 ' ) -> None :
        assert length >  0 , " Довжина має бути більшою за 0! "
        стверджувати  тип  у  собі . FIGURES , " Дозволені фігури: квадрат, прямокутник, трикутник "
        стверджувати колір у  собі . COLORS , " Дозволені кольори: червоний, зелений, синій "
        self .type =  тип
        self .length = довжина
        self .color = колір
    @ властивість
    def  get_figure_type ( self ):
        return  self .type
    @ властивість
    def  get_figure_length ( self ):
        return  self .type   # робимо помилку
    @ властивість
    def  get_figure_color ( self ):
        повернути  self .color
```

Test_app.py

```py
імпорт unittest
з випадкового вибору імпорту , randint
from app import Figure   # назва файлу з нашим класом повинна бути app.py
клас  TestFigure ( unittest . TestCase ):
    def  setUpClass ():
        """ Виконується лише раз на початкових тестах
        """
        пропуск
    def  setUp ( self ) -> None :
        """ Виконується кожен раз, коли запускається тест
        """
        self .figure = вибір(Малюнок. FIGURES )
        self .length = randint( 1 , 10 )
        self .color = choice(Малюнок. КОЛЬОРИ )
        self .obj = Figure( self .figure, self .length, self .color)
        повернути  супер ().setUp()
    def  tearDown ( self ) -> Немає :
        del  self .obj
        повернути  супер ().tearDown()
    def  test_figure_type ( self ):
        друкувати (
            f " Тестуємо вивід, має бути: { self .figure } == { self .obj.get_figure_type } " )
        self .assertEqual( self .figure, self .obj.get_figure_type,
                         " Властивість get_figure_type повертає непривильну фігуру! " )
    def  test_figure_lengh ( self ):
        self .assertEqual( self .length, self .obj.get_figure_length,
                         " Властивість get_figure_length повертає непривильну довжину! " )
    def  test_figure_color ( self ):
        self .assertEqual( self .color, self .obj.get_figure_color,
                         " Властивість get_figure_length повертає непривильний колір! " )
    def  test_obj ( self ):
        з  self .assertRaises( AssertionError ) :
            # Спробуйте створити об'єкт із недозволеними параметрами, у нас має бути помилка AssertionError
            Рисунок( " коло " , 1 )
if  __name__  ==  ' __main__ ' :
    # unittest.main(verbosity=2) для більш детального відображення
    unittest.main( багатослівність = 2 )
```

при запуску тестів вивело це:

```
test_figure_color (__main__.TestFigure) ... добре
test_figure_lengh (__main__.TestFigure) ... ПОМИЛКА
test_figure_type (__main__.TestFigure) ... Тестуємо вивід, має бути: прямокутник == прямокутник
в порядку
test_obj (__main__.TestFigure) ... добре
==================================================== =====================
ПОМИЛКА: test_figure_lengh (__main__.TestFigure)
-------------------------------------------------- --------------------
Traceback (останній останній виклик):
  Файл "D:\Labs\Labs 3.1\ООП\github\OOP\Lab5\Test_app.py", рядок 33, у test_figure_lengh
    self.assertEqual(self.length, self.obj.get_figure_length,
AssertionError: 5 != 'прямокутник' : Властивість get_figure_length повертає непривильну довжину!
-------------------------------------------------- --------------------
Пройшов 4 тести за 0,002 с
ПОМИЛКА (збої=1)
```

##  Юніт тестів з використанням бібліотеки PyTest

- Я створив віртуальне середовище та встановив туди бібліотеку `PyTest`
  До арр.ру додав таку функцію:

```py
def  test_app_triangle ():
    """ Перевірте, чи ми створюємо трикутну фігуру.
    """
    fig =  " трикутник "
    довжина  =  4
    col =  ' синій '
    triangle = Figure(fig, len , col)
    assert triangle.type == fig, f " Фігура має бути { fig } "
```

Ось що вивів `PyTest` :

```
================== починається тестова сесія ===================
платформа win32 -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
кореневий каталог: D:\Labs\Labs 3.1\ООП\github\OOP\Lab5
зібрано 1 шт
app.py . [100%]
================== 1 пройдено за 0,02 с ===================
```

А це вивід вісля запуску `Test_app.py` :

```
================== починається тестова сесія ===================
платформа win32 -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
кореневий каталог: D:\Labs\Labs 3.1\ООП\github\OOP\Lab5
зібрано 4 шт
Test_app.py .F.. [100%]
================== НЕВДАЧІ ===================
__________________ TestFigure.test_figure_lengh __________________
self = <Test_app.TestFigure testMethod=test_figure_lengh>
    def test_figure_lengh(self):
> self.assertEqual(self.length, self.obj.get_figure_length,
                         "Властивість get_figure_length повертає непривильну довжину!")
E AssertionError: 4 != 'квадрат' : Властивість get_figure_length повертає непривильну довжину!
Test_app.py:33: AssertionError
================== короткий підсумок тесту ===================
FAILED Test_app.py::TestFigure::test_figure_lengh - AssertionError: 4 != 'квадрат' : Властивість get_figure_length повертає непривильну довжину!
================== 1 помилка, 3 пройдено за 0,10 с ===================
```

##  Візуалізація результатів та покриття коду Coverage (pytest-cov)




- Я ввів команду `pipenv run python -m coverage html` та виглядає краще )

###  Висновок:

-  : question : Що зроблено в роботі; : wavy_dash : Я навчався проводити тести
-  : question : Чи досягнуто мети роботи; : wavy_dash : ну простенькі тести навчився робити, думаю досягнуто
-  : question : Які нові знання отримано; : wavy_dash : та який отримав)
-  : question : Чи вдалось відповісти на всі питання завдання в ході роботи; : wavy_dash : так )
-  : question : Чи успішно виконувати всі завдання; : wavy_dash : незнаю
-  : question : Чи виникли складності у виконанні завдання; : wavy_dash : ні
-  : question : Чи подобається такий формат здачі роботи (Feedback); : wavy_dash :  : сонцезахисні окуляри : : +1 :
-  : question : Побажання для покращення (Suggestions); : wavy_dash : все добре )