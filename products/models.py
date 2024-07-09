import uuid
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    created_At = models.DateField(auto_now_add=True)

    #def save(self, *args, **kwargs):
    #    self.slug = slugify(self.title)
    #    super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


def set_slug(sender, instance, *args, **kwargs): # Callback
    """
    Esta función es una función de retorno de llamada que se activa automáticamente 
    antes de guardar un objeto `Producto`.
    Asegura que cada producto tenga un slug único generado a partir de su título.
    """
    if instance.title and not instance.slug:
        """
        - Comprueba si el producto tiene un título y no tiene un slug.
        - Si se cumplen ambas condiciones, procede a generar un slug.
        """
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists():
            """
            - Crea un slug inicial utilizando `slugify(instance.title)`.
            - Comprueba si ya existe un producto con este slug en la base de datos.
            - Si existe un duplicado, crea un nuevo slug:
                1. Combinando el título con un guión (-)
                2. Añadiendo una cadena aleatoria de 8 caracteres generada a partir de `uuid.uuid4()`
                3. Convirtiendo el UUID en una cadena y cortando los 8 primeros caracteres
            """
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8])
            )

        instance.slug = slug    

pre_save.connect(set_slug, sender=Product)
