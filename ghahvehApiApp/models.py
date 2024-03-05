from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField( upload_to='category_images/', null=True, blank=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
class Product(models.Model):
    title = models.CharField(max_length=200,default='')
    content = models.TextField()
    amount1 = models.CharField(max_length=50,default='')
    amount2 = models.CharField(max_length=50,default='')
    amount3 = models.CharField(max_length=50,default='')
    price1 = models.CharField(max_length=50,default='')
    price2 = models.CharField(max_length=50,default='')
    price3 = models.CharField(max_length=50,default='')
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  # Add this line
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
