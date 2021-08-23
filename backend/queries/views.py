from django.shortcuts import render, HttpResponse
from . models import Product, Car, Manufacturer
from django.views.generic import ListView
from django.db import connection


# class QuerySet(model=None, query=None, using=None, hints=None)


def runquery(request):

    # ===== all()
    # получить все

    # q = Car.objects.all()
    # вернет 1 объект если есть, DoesNotExist если нет или MultipleObjectsReturned если много
    # q = Car.objects.get(pk=1)


    # ===== filter(**kwargs)
    # проверка на соответствие одному или нескольким условиям

    # одно условие
    # q = Car.objects.filter(price=100)

    # соответствие одновременно нескольким условиям
    # q = Car.objects.filter(price=100, name='b5')
    # q = Car.objects.filter(price=100).filter(name='b5')


    # ===== exclude(**kwargs)
    # несоответствие условию
    # q = Car.objects.exclude(price=100)

    # ===== order_by(*fields)
    # переопределяет сортировку для запроса
    # по умолчанию сортировка = ordering в классе Meta модели
    # q = Car.objects.order_by('-price')        # минус - указывает на обратный порядок
    # q = Car.objects.order_by('?')             # случайный порядок, дорогая операция
    # q = Car.objects.order_by('name', '-price')# 2 сортировки одна за другой



    # ===== reverse()
    # вернет обратный порядок элементов в запросе
    # q = Car.objects.ordered_by('name')
    # q.reverse()


    # ===== distinct(*fields)
    # исключает повторяющиеся строки из результатов запроса
    # в Постгрес может быть вызван для определенных полей, при этом 
    # поля в order_by() должны начинаться с полей в distinct() в том же порядке.
    q = Car.objects.ordered_by('name').distinct('name')
    q = Car.objects.distinct()

    # ===== values(*fields, **expressions)
    # вернет запрос, который возвращает словари, а не объекты
    # можно забрать только определенные поля
    # поле foo с ForeignKey по умолчанию вернет ключ словаря с именем foo_id
    q = Car.objects.values()
    q = Car.objects.values('name', 'price')
    q = Car.objects.values(lower_name=Lower('name'))


    # ===== values_list(*fields, flat=False, named=False)
    # вернет список кортежей из значений всех объектов модели
    # flat=True рабоает если поле одно, вернет список значений не в кортежах [1, 2, 3, ...]
    # named=True вернет результат в виде collection.namedtuple
    q = Car.objects.values_list('name', 'price')
    q = Car.objects.values_list('name', 'price').get(pk=1)
    q = Car.objects.values_list(Lower('name'), 'price')
    q = Car.objects.values_list('id', flat=True)




    # ===== dates(field, kind, order='ASC')
    # field должно быть полем DateField
    # kind должен быть либо "year", "month", "week", либо "day".
    # - "year" возвращает список всех различных значений года.
    # - "month" возвращает список всех различных значений года/месяца.
    # - "week" возвращает список всех различных значений года/недели. Все даты будут понедельником.
    # - "day" возвращает список всех различных значений года/месяца/дня.
    # order должен быть 'ASC'(по умолчанию) или 'DESC'
    Entry.objects.dates('pub_date', 'day', order='DESC') 
    # [datetime.date(2005, 3, 20), datetime.date(2005, 2, 20)]


    # ===== datetimes(field_name, kind, order='ASC', tzinfo=None, is_dst=None)
    # field_name должно быть DateTimeField
    # kind должен быть одним из: "year", "month", "week", "day", "hour", "minute", "second"
    # tzinfo=None - текущий часовой пояс. Можно задать другой = объекту datetime.tzinfo
    # is_dst=None указывает должен ли pytz интерпретировать несуществующие и неоднозначные даты в летнее время


    # ===== none()
    # набор запросов, который никогда не возвращает объекты
    # является экземпляром EmptyQuerySet.
    q = Car.objects.none()


    # ===== union(*other_qs, all=False)
    # SQL UNION для объединения результатов 2 или более QuerySet’ов
    # all=True разрешает повторяющиеся значения
    q = qs1.union(qs2, qs3)

    # ===== intersection(*other_qs)
    # SQL INTERSECT вернет общие элементы
    q = intersection(*other_qs)

    # ===== difference(*other_qs)
    # SQL EXCEPT вернет элементы, которые есть только в qs1
    q = qs1.difference(qs2, qs3)


    # ===== select_related(*fields)
    # работает только с однозначными отношениями 1 к 1
    # создает более  сложный запрос с подгрузкой данных из связанной модели
    # создает join с включением полей связанного объекта в SELECT
    q = Car.objects.select_related('manufacturer').get(pk=1)
    q = Car.objects.select_related('manufacturer__name').get(pk=1)


    # ===== prefetch_related(*lookups).
    # работает с отношениями многие ко многим и многие к 1
    # предварительно заполненный кеш с даными связанных полей
    # автоматически подгружает в одном запросе связанные объекты для каждого из указанных полей
    # Дополнительные запросы в prefetch_related() выполняются после того, как QuerySet начал оцениваться и был выполнен первичный запрос
    Pizza.objects.all().prefetch_related('toppings')


    # ===== defer(*fields)
    # имена полей, которые не загружаются
    q = Car.objects.defer('price')


    # ===== only(*fields)
    # загрузит только нужные поля
    q = Car.objects.only('name')



    # ===== using(alias)
    # какую базу данных QuerySet будет использовать, принимает псевдоним базы
    q = Car.objects.using('backup')




    # ===== select_for_update(nowait=False, skip_locked=False, of=())
    # блокирует строки до конца транзакции, генерируя оператор SQL SELECT ... FOR UPDATE
    # nowait=True сделает вызов неблокирующим. Если какая то строка в БД уже залокирована другой транзакцией, то этот запрос не будет ждать разблокровки, а вернет  DatabaseError.
    # skip_locked=True - игнорировать заблокированные строки, нельзя использовать вместе с nowait=True
    # of=(...)

    from django.db import transaction

    entries = Entry.objects.select_for_update().filter(author=request.user)
    with transaction.atomic():
        for entry in entries:
            ...

    # ===== raw(raw_query, params=None, translations=None)
    # Принимает необработанный SQL-запрос, выполняет его и возвращает экземпляр
    # поддерживает индексацию
    # индексация и срезы не выполняются на уровне базы данных, большое число объектов можно ограничить через LIMIT
    # может принимать параетрыы в виде списка или словаря через %s
    q = Car.objects.raw('SELECT * FROM myapp_car')
    q = Car.objects.raw('SELECT * FROM myapp_car')[0]
    q = Car.objects.raw('SELECT * FROM myapp_car LIMIT 1')
    name = 'a1'
    q = Car.objects.raw('SELECT * FROM myapp_car WHERE name = %s', [name])


    # ===== annotate(*args, **kwargs)

    # ===== extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)




    print(q)









    return render(request, 'queries/product_list.html', {'product_list': q})
    # return HttpResponse('ok')