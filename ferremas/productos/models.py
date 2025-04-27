from django.db import models


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

