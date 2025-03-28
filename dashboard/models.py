from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title



class Subject(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    lesson = models.TextField()
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateField(auto_now_add=True)
