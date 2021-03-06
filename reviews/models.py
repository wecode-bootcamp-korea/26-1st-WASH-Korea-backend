from django.db import models

class Review(models.Model):
    user       = models.ForeignKey('users.User',on_delete=models.CASCADE)
    product    = models.ForeignKey('products.Product',on_delete=models.CASCADE)
    image      = models.CharField(max_length=2000,null=True)
    rating     = models.IntegerField(default=1)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'reviews'
