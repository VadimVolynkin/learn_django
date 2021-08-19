# ============================================================================
# НАСЛЕДОВАНИЕ В МОДЕЛЯХ ДЖАНГО
# ============================================================================
Базовый класс должен наследоваться от django.db.models.Model.
Есть 3 вида наследования моделей в Django:
- абстрактная модель
- multi-table наследование
- proxy-model


# ============================================================================
# АБСТРАКТНАЯ МОДЕЛЬ
# ============================================================================
Родительская модель для хранения общих полей дочерних моделей.
Определяется в метаклассе через abstract = True.
Не создает свои экземпляры, таблицу в БД, нет менеджера.
Поля абстрактной модели могут быть переопределены в дочерней или удалены с помощью None.
Если дочерний класс не определяет свой класс Meta, он унаследует родительский класс Meta с abstract=False  
Дочерняя модель может расширить родительский Meta класс с атрибутом abstract=False.

В абстрактной модели поля отношений могут включать параметр related_name="%(app_label)s_%(class)s_related" - чтобы избежать дублирования уникальных имен. 
В абстрактной модели без указания related_name будет использовано название 'childmodel_set'.


class Person(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ['name']


class Author(Person):
    salary = models.PositiveIntegerField()


# ============================================================================
# MULTI-TABLE НАСЛЕДОВАНИЕ
# ============================================================================
Родительская не абстрактная модель имеет собственную таблицу в БД и может быть использована независимо.
Такая родительская модель может быть взята например из другого приложения.
Мультитейбл наследование часто используется в миксинах.

Связь между родительской и дочерней моделью происходит через автоматически созданное поле OneToOneField.
Используется название по умолчанию для атрибута related_name в ForeignKey и ManyToManyField.
Переопределить related_name можно создав собственное поле OneToOneField с parent_link=True чтобы указать, что это поле является связью с родительской моделью.

Если вы используете такие связи на дочернюю модель с аналогичным предком, вы должны определить related_name для каждого такого поля. Иначе Django вызовет исключение.

Дочерняя модель не имеет доступа к родительскому классу Meta, кроме случаев, когда дочерняя модель не определяет атрибут ordering или get_latest_by, они будут унаследованы.

# ===== ВАРИАНТ 1: явное указание полей pk в родительских моделях
# Будут созданы 3 таблицы: 
# - model_inheritance_person
# - model_inheritance_account
# - model_inheritance_author
# Поля person_id и account_id нужны чтобы избежать конфликт полей id в дочерней модели.

class Person(models.Model):
    name = models.CharField(max_length=100)
    person_id = models.AutoField(primary_key=True)


class Account(models.Model):
    address = models.CharField(max_length=100)
    account_id = models.AutoField(primary_key=True)


class Author(Person, Account):
    salary = models.PositiveIntegerField()

# ===== ВАРИАНТ 2: использование в качестве pk общего предка
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
    # в таблице будут созданы поля для связи
    # person_ptr_id
    # account_ptr_id
    salary = models.PositiveIntegerField()


# ============================================================================
# PROXY-MODEL НАСЛЕДОВАНИЕ
# ============================================================================
Proxy-модель - дочерняя модель, в метаклассе которой есть proxy = True.
Прокси модель не создает таблицу, а использует родительскую.
Прокси модель не имеет своих полей, но может иметь свои методы и метапараметры.
Прокси модель используют для изменения поведения модели без изменения струкуры БД и ее самой.

Проски модели наследуют все поля, менеджеров и метапараметры родительской модели.
Объекты proxy модели можно создать, изменять и все изменения будут сохранены как в родительской модели.
Если определить для прокси свой менеджер - он станет менеджером по умолчанию, при этом менеджеры родительской модели будут также доступны.

Прокси-модель должна наследоваться ровно от одного неабстрактного класса модели. 
Прокси-модель может наследоваться от любого количества прокси-моделей, которые имеют общий неабстрактный родительский класс.


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



















