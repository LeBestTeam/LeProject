# Коментування та назви

### Базові вимоги
* Назви змінних, класів та функцій мають бути без скорочень
* Ітераційні змінні можуть бути у форматі i, ii, iii... та приймати лише цілі значення.
* У класах та функціях використовувати docstring
* Напроти кожного "великого" рядка має бути коментар про те що робить цей рядок

### Приклади до базових вимог
##### Назви змінних, класів та функцій мають бути без скорочень
```python
n = 0 # не ок
number_of_pixels = 0 # ок
n_of_pixels = 0 # не дуже ок, але можна використати якщо інакше виходить дуже громіздко
```
##### Ітераційні змінні
```python
iterable = 0
while iterable in range(10):
    pass # do something
# ок


i = 0
while i in range(10):
    ii = 0
    while ii in range(10):
        pass # do something
# ок
```

##### Коментарі до функцій та класів (docstring)
```python
class Apple():
    pass # тут щось є
# не ок


class Apple():
    """Клас яблука що зберігає його властивості та містить функції зміни самого себе"""
    pass # тут щось є
# ок


def pile_an_apple(Apple):
    Apple.pile()
# не дуже ок


def pile_an_apple(Apple):
    Person.get_a_knife()
    Cuttingboard.place_on(Table)
    # ... продовжується ще на два екрани
# не ок


# 
# повертає очищене Apple
def pile_an_apple(Apple):
    """Функція що знімає кожуру з Apple. Для цього залучається Person, Cuttingboard і Table."""
    Person.get_a_knife()
    Cuttingboard.place_on(Table)
    # ... продовжується ще на два екрани
# ок
```