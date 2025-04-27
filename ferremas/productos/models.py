from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Gestor personalizado para Usuario
class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre_usuario, contrasena=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un email')
        email = self.normalize_email(email)
        usuario = self.model(email=email, nombre_usuario=nombre_usuario, **extra_fields)
        usuario.set_password(contrasena)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nombre_usuario, contrasena=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nombre_usuario, contrasena, **extra_fields)

# Modelo base Usuario
class Usuario(AbstractBaseUser, PermissionsMixin):
    PERFIL_CHOICES = [
        ('Cliente', 'Cliente'),
        ('Trabajador', 'Trabajador'),
    ]

    nombre_usuario = models.CharField(max_length=100)
    rut = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    usuario = models.CharField(max_length=100)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre_usuario', 'usuario']

    def __str__(self):
        return self.nombre_usuario


# Create your models here.
class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    class Meta:
        managed = False  # No crear ni modificar esta tabla
        db_table = 'categoria'

    def __str__(self):
        return self.nombre_categoria
    
class Marca(models.Model):
    marca_id = models.AutoField(primary_key=True)
    nombre_marca = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'marca'

    def __str__(self):
        return self.nombre_marca


class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100, verbose_name='Producto')
    categoria = models.ForeignKey('Categoria', on_delete=models.DO_NOTHING, db_column='categoria_id', verbose_name='Categoría')
    marca = models.ForeignKey('Marca', on_delete=models.DO_NOTHING, db_column='marca_id', verbose_name='Marca')
    modelo = models.CharField(max_length=200, verbose_name='Modelo')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio') 
    codigo_sku = models.CharField(max_length=50, verbose_name='Código SKU')

    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        return self.nombre_producto

