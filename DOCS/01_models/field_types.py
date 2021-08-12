# ==========================================================================================================
# ТИПЫ ПОЛЕЙ
# ==========================================================================================================

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