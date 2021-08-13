# ==========================================================================================================
# ТИПЫ ПОЛЕЙ
# ==========================================================================================================
from django.db import models


class Foo(models.Model):

    # Атрибуты модели содержат объекты Python
    # Классы полей преобразуют значения атрибутов в данные сохраняемые в БД или передаваемые в сериализатор
    name = models.CharField(max_length=70)
    age = models.PositiveIntegerField()


   # ===== AUTOINCREMENT FIELDS =================================================================
    id = models.AutoField()                       
    id = models.SmallAutoField()                  
    id = models.BigAutoField(primary_key = True)  
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # ===== ЧИСЛОВЫЕ ПОЛЯ =======================================================================
    num = models.SmallIntegerField()            
    num = models.IntegerField()                 
    num = models.BigIntegerField() 
    num = models.PositiveIntegerField()
    num = models.PositiveSmallIntegerField()
    num = models.PositiveBigIntegerField()
    num = models.DecimalField(max_digits=None, decimal_places=None, **options)
    num = models.FloatField()
 
    # ===== ТЕКСТОВЫЕ ПОЛЯ =================================================================
    text = models.CharField(max_length = 255)
    text = models.TextField()
    text = models.SlugField(max_length=50, **options)
    text = models.EmailField(max_length=255, **options)
    text = models.URLField(max_length=200, **options)
    text = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY, blank=True, match=None, recursive=False, max_length=100, **options)
    text = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, **options)

    # ===== ПОЛЯ ДАТ И ВРЕМЕНИ ===================================================================================
    dt = models.DateField(auto_now=False, auto_now_add=False, **options) 
    dt = models.TimeField(auto_now=False, auto_now_add=False, **options)
    dt = models.DateTimeField(auto_now=False, auto_now_add=False, **options)
    dt = models.DurationField()

    # ===== ЛОГИЧЕСКИЕ ПОЛЯ ======================================================================================
    boolean = models.BooleanField(default=None)
    boolean = models.NullBooleanField()

    # ===== ФАЙЛОВЫЕ ПОЛЯ ========================================================================================
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', max_length=100, **options)
    file = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
    file = models.BinaryField()



# ==========================================================================================================
# СОЗДАНИЕ СОБСТВЕННОГО ТИПА ПОЛЯ
# ==========================================================================================================
Значение поля модели должно быть преобразовано в 1 из доступных типов полей БД. Например, в строку.
Все поля джанги наследуются от Field и переопределяют поведение этого класса.

Подкласс Field предоставляет несколько способов преобразования объектов Python в значение для базы/сериализации - скорее всего вам придется создавать два класса:
 - класс1 будет использоваться пользователями для отображения, работы с данными, при изменении значения поля модели.
 - класс2 – подкласс Field для преобразование первого класса в значение для хранения в БД и обратно в объект Python.


# Пример класса1
class Hand:
    """A hand of cards (bridge style)"""

    def __init__(self, north, east, south, west):
        # Input parameters are lists of cards ('Ah', '9s', etc.)
        self.north = north
        self.east = east
        self.south = south
        self.west = west

# Пример класса2
class MytypeField(models.Field):

    description = _("Документирование собственного поля")

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 104
        super().__init__(*args, **kwargs)







# TODO ======================================================================================================
# choices = models.Choices()
# integer_choices = models.IntegerChoices()
# text_choices = models.TextChoices()
# comma_separated_integer_field = models.CommaSeparatedIntegerField()
# empty_field = models.Empty()
# ip_adress_field = models.IPAddressField()
# json_field = models.JSONField()