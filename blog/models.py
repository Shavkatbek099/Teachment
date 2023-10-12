from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from .validator import validator

# Create your models here.


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    DoesNotExist = None

    class PostManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=True)

    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=250)
    publish = models.DateTimeField(default=timezone.now())
    phone = models.CharField(max_length=13, validators=[validator])
    email = models.EmailField()
    content = '.serializer.PostSerializer.content'
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    statuss = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    status = models.BooleanField(default=False)
    teacher_manager = PostManager()

    objects = models.Manager()
    published = PublishManager()


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish']


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name="Ismi")
    surname = models.CharField(max_length=30, verbose_name="Familiya")
    phone = models.CharField(max_length=13, validators=[validator], verbose_name="Telefon raqam")
    age = models.IntegerField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["age"]
