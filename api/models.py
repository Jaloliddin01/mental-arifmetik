from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    has_image = models.BooleanField(default=False)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=20)
    a = models.CharField(max_length=20)
    b = models.CharField(max_length=20)
    c = models.CharField(max_length=20)
    d = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

# class MathQuestion(models.Model):
#     CATEGORY = (
#         ('addition', 'Addition'),
#         ('subtraction', 'Subtraction'),
#         ('multiplication', 'Multiplication'),
#         ('division', 'Division'),
#     )
#     question = models.CharField(max_length=200)
#     answer = models.CharField()
#     a = models.CharField()
#     b = models.CharField()
#     c = models.CharField()
#     d = models.CharField()
#     category = models.CharField(max_length=20, choices=CATEGORY)

#     def __str__(self):
#         return self.question

# class InterestionQuestion(models.Model):
#     CATEGORY = (
#         ('firstnumber', 'FirstNumber'),
#         ('findnumber', 'FindNumber'),
#         ('secondnumber', 'SecondNumber'),
#     )
#     question = models.CharField(max_length=200)
#     answer = models.CharField()
#     a = models.CharField()
#     b = models.CharField()
#     c = models.CharField()
#     d = models.CharField()
#     category = models.CharField(max_length=20, choices=CATEGORY)

#     def __str__(self):
#         return self.question

# class PictureQuestion(models.Model):
#     CATEGORY = (
#         ('logic', 'Logic'),
#         ('mind', 'Mind'),
#     )
#     picture = models.ImageField(upload_to='images/')
#     answer = models.CharField()
#     a = models.CharField()
#     b = models.CharField()
#     c = models.CharField()
#     d = models.CharField()
#     category = models.CharField(max_length=20, choices=CATEGORY)

#     def __str__(self):
#         return self.question


