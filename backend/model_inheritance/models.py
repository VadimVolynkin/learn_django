from django.db import models

# =====================================================
# ТИПЫ НАСЛЕДОВАНИЯ В ДЖАНГО
# =====================================================
# - abstract-model
# - multi-table
# - proxy-model

# =====================================================
# АБСТРАКТНАЯ МОДЕЛЬ
# =====================================================
# будет создана только 1 таблица: model_inheritance_author

"""
class Person(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ['name']


class Author(Person):
    salary = models.PositiveIntegerField()


# ===== QUERIES with ONE TO ONE ===============
from model_inheritance.models import Person, Author

# создание экземпляра дочерней модели
a = Author.objects.create(name='ivan', salary=123)
a.save()

# получение данных
a.name
a.salary


"""



# =====================================================
# MULTI-TABLE
# =====================================================
# Будут созданы 3 таблицы: 
# - model_inheritance_person
# - model_inheritance_account
# - model_inheritance_author
# Поля person_id и account_id нужны чтобы избежать конфликт полей id в дочерней модели.
# Все 3 таблицы могут быть использованы для хранения данных

"""

class Person(models.Model):
    name = models.CharField(max_length=100)
    person_id = models.AutoField(primary_key=True)


class Account(models.Model):
    address = models.CharField(max_length=100)
    account_id = models.AutoField(primary_key=True)


class Author(Person, Account):
    salary = models.PositiveIntegerField()

"""
"""
# ===== QUERIES with MULTITABLE ===============

from model_inheritance.models import Author

# создание объекта автора
a = Author.objects.create(name='ivan', address='moscow', salary=123)
"""


"""
# ===== Использование в качестве pk общего предка
# person_someparent и account_someparent устанавливают в качестве своего pk поле pk родителя
# таким образом модель Author получит такой pk по наследству

class SomeParent(models.Model):
    pass

class Person(SomeParent):
    name = models.CharField(max_length=100)
    person_someparent = models.OneToOneField(SomeParent, on_delete=models.CASCADE, parent_link=True)

class Account(SomeParent):
    address = models.CharField(max_length=100)
    account_someparent = models.OneToOneField(SomeParent, on_delete=models.CASCADE, parent_link=True)

class Author(Person, Account):
    salary = models.PositiveIntegerField()
"""

# =====================================================
# PROXY MODEL
# =====================================================
# будет создана только 1 таблица: model_inheritance_person
# в примере прокси меняет сортировку и добавляет новый метод

class Person(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        ordering = ['name']

class PersonProxy(Person):

    def say_hello(self):
        return self.name + ', hello!'
    class Meta:
        proxy = True
        ordering = ['-name']


"""
# ===== QUERIES with MULTITABLE ===============
from model_inheritance.models import Person, PersonProxy

# создание объекта через прокси-модель
p = PersonProxy.objects.create(name='ivan')
"""








