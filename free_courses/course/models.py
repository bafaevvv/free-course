from django.db import models

class Course(models.Model):
      title = models.CharField(max_length=50)
      desc = models.TextField(max_length=300)
      img = models.ImageField(blank=True)
      url = models.URLField(max_length=200)

      def __str__(self):
            return self.title

class Category(models.Model):
      title = models.CharField(max_length=50)
      course = models.ManyToManyField(Course)

      def __str__(self):
            return self.title