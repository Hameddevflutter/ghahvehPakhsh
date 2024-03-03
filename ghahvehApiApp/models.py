from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200,default='')
    content = models.TextField()
    amount1 = models.CharField(max_length=50,default='')
    amount2 = models.CharField(max_length=50,default='')
    amount3 = models.CharField(max_length=50,default='')
    price1 = models.CharField(max_length=50,default='')
    price2 = models.CharField(max_length=50,default='')
    price3 = models.CharField(max_length=50,default='')
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  # Add this line

    def __str__(self):
        return self.title
