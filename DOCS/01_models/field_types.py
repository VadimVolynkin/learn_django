# ==========================================================================================================
# ТИПЫ ПОЛЕЙ
# ==========================================================================================================
from django.db import models


class Foo(models.Model):

    # Атрибуты модели содержат объекты Python класса models. ...
    # Атрибуты объектов модели содержат данные.
    # Классы полей преобразуют значения атрибутов в данные сохраняемые в БД или передаваемые в сериализатор
    name = models.CharField(max_length=70)
    age = models.PositiveSmallIntegerField()


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




# TODO ======================================================================================================
# choices = models.Choices()
# integer_choices = models.IntegerChoices()
# text_choices = models.TextChoices()
# comma_separated_integer_field = models.CommaSeparatedIntegerField()
# empty_field = models.Empty()
# ip_adress_field = models.IPAddressField()
# json_field = models.JSONField()


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



# ==========================================================================================================
# ТИПЫ ПОЛЕЙ С ОПИСАНИЕМ
# ==========================================================================================================

class ModelTypes(models.Model):
    
    # ===== AUTOINCREMENT FIELDS =================================================================
    
    id = models.AutoField()                       
    # используется по умолчанию как pk

    id = models.SmallAutoField()                  
    # от 1 до 32767

    id = models.BigAutoField(primary_key = True)  
    # от 1 до 9223372036854775807 (19 знаков)
    # primary_key = True - делает поле первичным ключом, стандартный pk не будет создан, только 1 поле может быть pk

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # UUID - альтернатива AutoField с primary_key, выдаст
    # PostgreSQL использует тип uuid, иначе char(32)
    # default=uuid.uuid4 - функция генерации uuid без скобок - вернет 953dd7ecd82e465cb9e66e131ce4408e


    # ===== ЧИСЛОВЫЕ ПОЛЯ =====================================================================

    # Чтобы сохранить форму с незаполненным значением нужно ставить null=True, blank=True. 
    # Числа могут сохранять значения больше, чем диапазон их определения.
    # Диапазон зависит от БД

    num = models.SmallIntegerField()            
    # Целое от -32768 до 32767 (32 тысячи, 2 байта)

    num = models.IntegerField()                 
    # Целое от -2147483648 до 2147483647 (2 миллиарда, 4 байта)
    # Валидаторы MinValueValidator и MaxValueValidator 
    # Виджет по умолчанию в форме - NumberInput, если localize равен False, иначе TextInput.

    num = models.BigIntegerField() 
    # Целое от -9223372036854775808 до 9223372036854775807 (19 знаков, 8 байт).

    num = models.PositiveIntegerField()
    # Целое от 0 до 2147483647 (2 миллиарда). 
    # При попытке сохранить отрицатльное значение выдаст ошибку.

    num = models.PositiveSmallIntegerField()
    # Целое от 0 до 32767.

    num = models.PositiveBigIntegerField()
    # Целое от 0 до 9223372036854775807

    num = models.DecimalField(max_digits=None, decimal_places=None, **options)
    # Десятичное число с фиксированной точностью, в Python  - экземпляр Decimal. 
    # Всегда используйте DecimalField для денег. 
    # Валидатор - DecimalValidator. При попытке ввести число точнее чем в decimal_places - выдаст ошибку.
    # Виджет по умолчанию в форме - NumberInput, если localize равен False, иначе TextInput. 
    # Имеет 2 обязательных аргумента:
    # - max_digits - максимальное количество цифр в числе, которое больше или равно decimal_places.
    # - decimal_places - количество знаков после запятой.

    num = models.FloatField()
    # Число с плавающей точкой - объект float. 
    # Виджет по умолчанию в форме - NumberInput, если localize равен False, иначе TextInput.
    # Недостаток поля - некорректное округление при операциях.

    # ===== ТЕКСТОВЫЕ ПОЛЯ =================================================================

    text = models.CharField(max_length = 255)
    # Поле для хранения коротких или длинных строк. Для больших текстов лучше использовать TextField.
    # max_length - максимальная длина строки, проверяется Django с помощью MaxLengthValidator.
    # Виджет по умолчанию для этого поля TextInput.

    text = models.TextField()
    # Большое текстовое поле. 
    # Форма использует виджет Textarea.
    # Если указать max_length, это повлияет на поле, создаваемое виджетом Textarea, но не учитывается на уровне модели или базы данных. Для max_length используйте CharField.

    text = models.SlugField(max_length=50, **options)
    # Slug  - название-метка, содержит только буквы, числа, подчеркивание или дефис. Используются в URL. 
    # По умолчанию max_length=50, db_index=True. 
    # В админке генерируется обычно на основе поля указанного в prepopulated_fields. 
    # Валидаторы validate_slug или validate_unicode_slug. 
    # Доп параметры: allow_unicode - при True может принимать Unicode символы кроме ASCII. Значение по умолчанию – False.

    text = models.EmailField(max_length=255, **options)
    # CharField + проверка EmailValidator.

    text = models.URLField(max_length=200, **options)
    # CharField + валидатор URLValidator. 
    # Виджет по умолчанию - TextInput.

    text = models.FilePathField(path=settings.FILE_PATH_FIELD_DIRECTORY, blank=True, match=None, recursive=False, max_length=100, **options)
    # CharField для ввода пути конкретного файла с сервера.(предоставляет пользователям выбор пути на сервере)
    # Принимает аргументы, первый обязателен: 
    # - path - абсолютный путь к каталогу. Например: "/home/images". Может быть вызываемым, например return os.path.join(settings.LOCAL_FILE_DIR, 'images')
    # - match - регулярное выражение как строка, которое FilePathField использует как фильтр названий. Применяется к названию файла, а не к полному пути. Например: "foo.*\.txt$", соответствует foo23.txt но отфильтрует bar.txt или foo23.gif.
    # - recursive - определяет, должны ли быть включены подкаталоги path. По-умолчанию False.
    # - allow_files - должны ли быть соответствующими подкаталоги. По-умолчанию True. Этот параметр или allow_folders должен быть True.
    # - allow_folders - определяет, должны ли быть включены указанные подкаталоги. По-умолчанию False. Этот параметр или allow_files должен быть True.

    text = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, **options)
    # Адрес IPv4 или IPv6 в виде строки (например, 192.0.2.30 или 2a02:42fe::4).
    # protocol - формат IP адреса: 'both' (по умолчанию), 'IPv4' или 'IPv6'. Значение не чувствительно регистру.
    # unpack_ipv4=False(по умолчанию). При True преобразует адрес в IPv4. 
    # Форма использует виджет TextInput. 


    # ===== ПОЛЯ ДАТ И ВРЕМЕНИ ===================================================================================

    dt = models.DateField(auto_now=False, auto_now_add=False, **options) 
    # Дата в виде default=date.today из datetime.date.today().
    # Поля с auto не выводятся в админке даже с параметром editable=True.
    # auto_now=True - установливает текущую дату при каждом save (), если не указан другой метод. Используют для хранения времени последнего изменения.
    # auto_now_add=True - устанавливает текущую дату при создании объекта. Используют для хранения времени создания.
    # Если нужно не auto_now и auto_now_add, то можно использовать свое переопределение save ().

    dt = models.TimeField(auto_now=False, auto_now_add=False, **options)
    # Время в виде datetime.time Python. Принимает те же аргументы, что и DateField.
    # Использует виджет TextInput. Интерфейс администратора также использует немного JavaScript.

    dt = models.DateTimeField(auto_now=False, auto_now_add=False, **options)
    # Дата и время в виде default=timezone.now из django.utils.timezone.now(). Принимает те же аргументы, что и DateField.
    # Виджет по умолчанию в форме для этого поля - TextInput. 
    # Интерфейс администратора использует два виджета TextInput и JavaScript.

    dt = models.DurationField()
    # Хранит период времени - используется объект Python timedelta. 
    # Для PostgreSQL используется тип interval, а в Oracle – INTERVAL DAY(9) TO SECOND(6). Иначе используется bigint, в котором хранится количество микросекунд.
    # Принимает данные в виде 10:12:08


    # ===== ЛОГИЧЕСКИЕ ПОЛЯ ======================================================================================

    boolean = models.BooleanField(default=None)
    # Поле True / False. По умолчанию None, если default не указан. 
    # Виджет формы по умолчанию - CheckboxInput или NullBooleanSelect, если null = True.

    boolean = models.NullBooleanField()
    # BooleanField с null = True. 
    # Используйте BooleanField вместо его, в будущей версии Django скорее всего будет устаревшим.


    # ===== ФАЙЛОВЫЕ ПОЛЯ ========================================================================================

    # Для использования FileField и ImageField нужно определить в конфиге:
    # - MEDIA_ROOT - полный путь к каталогу для загружаемых файлов
    # - MEDIA_URL  - базовый общедоступный URL-адрес этого каталога
    # БД будет хранить путь к файлам относительно MEDIA_ROOT
    # Получить url файла в шаблоне можно так {{object.photo.url}}, где photo - название поля ImageField
    # ВАЖНО! Проверяйте все загружаемые файлы для безопасности!
    # В БД файловые поля создаются как varchar.


    file = models.FileField(upload_to='uploads/%Y/%m/%d/', max_length=100, **options)
    # Поле для загрузки файла.

        FileField.upload_to
        # Способ установки каталога для загрузки файла и определении его имени. 
        # Может быть установлен 2 способами, в обоих случаях значение передается методу Storage.save ().
        # Если строковое значение или путь, то может содержать strftime (), которое будет заменено датой / временем загрузки файла
        # Если использовать FileSystemStorage по умолчанию, то строковое значение будет добавлено к пути MEDIA_ROOT.

        # upload_to может быть вызываемым объектом, который принимает instance и filename и возвращает путь в стиле Unix(с прямыми слэшами).
        # Например return 'user_{0}/{1}'.format(instance.user.id, filename). Значение будет передано в метод Storage.save()
        # - instance - сохраняемый объект(экземпляр модели)
        # - filename - оригинальное имя файла

        # Виджет форма для поля - ClearableFileInput. В базе данных будет сохранен путь к файлу относительно MEDIA_ROOT. В шаблоне можно использовать {{ object.my_file_name.url }}
        # Пример: MEDIA_ROOT = '/media', и upload_to = 'photos/%Y/%m/%d'. Путь будет /media/photos/2007/01/15
        

        FileField.storage
        # Объект хранения или вызываемый объект, который возвращает объект хранения. 
        # Управляет хранением и поиском ваших файлов. 

        # Виджет форма для поля - ClearableFileInput.
        
        FieldFile.name
        # имя файла, включая относительный путь от корня хранилища.

        FieldFile.size
        # результат базового метода Storage.size().

        FieldFile.url
        # свойство только для чтения для получения URL-вызова метода url () класса Storage.
        
        FieldFile.url
        # свойство только для чтения для получения URL-вызова метода url () класса Storage.
        
        FieldFile.open(mode='rb') 
        # Открывает или повторно открывает файл, связанный с этим экземпляром, в указанном режиме. 
        # В отличие от стандартного метода Python open() не возвращает дескриптор файла.
        # Может использоваться для изменения режима открытия.
        
        FieldFile.close ()          
        # как и метод file.close() в Python закрывает файл с объектом.
        
        FieldFile.save(name, content, save=True) 
        # Принимает имя и содержимое и передает в экземпляр storage, потом добавляет файл в FileField. 
        # name – название файла
        # content – содержимое файла, должен быть экземпляром django.core.files.File, а не встроенным объектом файла в Python.
        # save  –  указывает сохранять ли объект после изменения поля.

        FieldFile.delete(save=True)
        # Удаляет файл связанный с объектом и очищает все атрибуты поля.
        # save указывает сохранять ли модель после удаления файла. По-умолчанию True.
        # Заметка: метод закрывает файл, если он был открыт во время вызова delete(). 
        # Когда объект модели удаляется, связанные файлы не удаляются. Если необходимо удалять их, делайте это через cron.


    file = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
    # Наследует все атрибуты и методы FileField + свои атрибуты height и width, проверяет является ли файл изображением.
    # Требует Pillow.  
    # varchar в базе данных, можно менять max_length. 
    # Виджет форма для поля - ClearableFileInput.

        file.height_field
        # имя поля автоматически = высоте изображения при каждом сохранении объекта.

        file.width_field
        # имя поля автоматически = ширине изображения при каждом сохранении объекта.


    file = models.BinaryField()
    # Поле для хранения необработанных двоичных данных. 
    # Ему могут быть назначены байты, массив байтов или вид памяти. Поле хранит объект питона и его нельзя вводить вручную
    # Необязательный аргумент: max_length. По умолчанию editable=False. 
    # Хранение файлов в базе данных в 99% случаях - это плохой подход. Это поле не замена статическим файлам.
    # Пример binary_field = models.BinaryField(default=bytes('hello world', 'utf-8')) # convert string hello world in bytes
