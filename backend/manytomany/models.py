from django.db import models

"""
# ============================================================================
# MANY-TO-MANY: Способ 1 - автоматический
# ============================================================================
# В базе будут созданы следующие таблицы:
# manytomany_group
# manytomany_person
# manytomany_person_group

class Person(models.Model):
    name = models.CharField(max_length=255)
    groupes = models.ManyToManyField('Group')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
"""
# ============================================================================
# MANY-TO-MANY: Способ 2 - через создание своей связующей таблицы
# ============================================================================

class Person(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)

    # поле ManyToManyField указывает на связующую таблицу в параметре through
    # в какой именно из основных таблиц будет указано поле - неважно
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    # в связующей модели нужно явно указать внешние ключи на обе модели
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    # дополнительные данные
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.person} {self.invite_reason}'

    class Meta:
        # исключает повтороное добавление одиноковых записей
        unique_together = [['person', 'group']]

"""

# ===== QUERIES with MANY TO MANY ===============
# try it in ./manage.py shell

# получить объект человека
obj = Person.objects.get(pk=1)

# получить все группы человека
obj.group_set.all()

# создать человека
obj = Person(name = 'Vadim')
obj.save()

# добавить в группу человека
obj = Person(name = 'Vadim')
managers = Group.objects.get(name='Managers')
managers.members.add(
    obj, through_defaults = {
        'date_joined' : '2020-03-31',
        'invite_reason': 'some reason'
        })

# добавить к человеку группу
vadim = Person.objects.get(name='Vadim')
programmers = Group.objects.get(name='Programmers')
vadim.group_set.add(
    programmers, through_defaults = {
        'date_joined' : '2020-05-25',
        'invite_reason': 'some reason2'
        })


# создание нового пользователя с добавлением его в группу одной командой
# нужно передать все аргументы для конструктора в виде ключ-значение
managers = Group.objects.get(name='Managers')
managers.members.create(
    name='Bob', through_defaults = {
        'date_joined' : '2018-02-20',
        'invite_reason': 'some reason3'
        })

"""