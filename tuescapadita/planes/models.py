from django.db import models

# Create your models here.
class ProductCard (models.Model):
    image = models.ImageField(verbose_name = 'Imágen', upload_to="plans")
    name = models.CharField(max_length=20, verbose_name = 'Nombre Plan')
    time = models.CharField(max_length=30, verbose_name = 'Estadía', null=True, blank=True)
    building = models.CharField(max_length=30, verbose_name = 'Tipo de Residencia', null=True, blank=True)
    buffet = models.CharField(max_length=30, verbose_name = 'Buffet', null=True, blank=True)
    pets = models.CharField(max_length=30, verbose_name = 'Mascotas', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de modificación", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'