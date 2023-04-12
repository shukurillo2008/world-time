from django.db import models
from django.contrib.auth.models import User


class Categoriya(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "categorys"

class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Regions"
    

class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categoriya, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "News"

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="news/")

    def __str__(self) -> str:
        return self.news.title
    
    class Meta:
        verbose_name_plural = "Images"    

class CommentNews(models.Model):
     body =models.CharField(max_length=255)
     created = models.DateTimeField(auto_now_add=True)
     news = models.ForeignKey(News, on_delete=models.CASCADE)
     author = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self) -> str:
         return self.news.title
        

class StatuxNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dis_like = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.news} {self.author}"
    

