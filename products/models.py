from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Product(BaseModel): 
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)
    product_demo_price = models.IntegerField(default=0)
    quantity = models.CharField(null=True, blank=True, max_length=100)

class ProductMetaInformation(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.CharField(null=True, blank=True)
    
    

class ProductImages(BaseModel):
    product_images = models.ImageField(upload_to="products")
    
    