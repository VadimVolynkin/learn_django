from django.db import models

# =====================================================
# ONE-TO-ONE
# =====================================================

# базовая модель
class Person(models.Model):
    # неявно создается еще одно свойство с именем зависимой модели - author,
    # оно указывает на связанный с этим объектом объект автора
    name = models.CharField(max_length=100)


# расширяющая модель
class Author(models.Model):
    # первый параметр определяет с какой моделью ассоциировать сущность
    # on_delete = models.CASCADE - объект этой модели будет удален, если будет удален связанный объект Person
    # primary_key = True - внешний ключ через который идет связь с главной моделью будет также pk. Соответственно поле pk для этой модели не будет создано.
    person = models.OneToOneField('Person', on_delete = models.CASCADE, parent_link=True)
    salary = models.PositiveIntegerField()


"""

# ===== QUERIES with ONE TO ONE ===============
# try it in ./manage.py shell

from onetoone.models import Person, Author

# создать объект автора
from onetoone.models import Person, Author
p = Person.objects.create(name = 'ivan')
p.save()
a = Author.objects.create(person=p, salary=123)
a.save()

# получение данных
obj = Person.objects.get(name='ivan')
obj.name
obj.author.salary

"""
