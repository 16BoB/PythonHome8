# 1) Написать программу, где создадим класс Soup (для определения типа супа), принимающий 1 аргумент - который отвечает за основной продукт к выбираемому супу.
# В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки
# Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»

ingredients = {'Капуста': 'Щи', 'Свекла': 'Борщ'}

class Soup:
    def __init__(self, ingredient = ''):
        self.ingredient = ingredient

    def show_my_soup(self):
        if self.ingredient == '': print('Обычный кипяток')
        else:
            print(f'Ваш суп - {ingredients[self.ingredient]}, Основной продукт - {self.ingredient}')

my_soup = Soup('Капуста')
my_soup.show_my_soup()

my_soup = Soup()
my_soup.show_my_soup()