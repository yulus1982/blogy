from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(default='', blank=True, upload_to='image')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Commentaire(models.Model):
    nom_post = models.ForeignKey(
        Post, null=True, on_delete=models.CASCADE, related_name='comments')
    nom_comm = models.CharField(max_length=100, blank=True)
    # reponse = models.ForeignKey('Commentaire', null=True, blank=True, on_delete=models.CASCADE, related_name='reponse')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    corps = models.TextField(max_length=150)
    data_added = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.nom_comm = slugify(
            "commente par"+str(self.auteur) + "a"+str(self.data_added))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom_comm

    class Meta:
        ordering = ['data_added']


class Reponse(models.Model):
    nom_comm = models.ForeignKey(
        Commentaire, on_delete=models.CASCADE, related_name='reponses')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    corps = models.TextField(max_length=150)
    data_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "reponse a " + str(self.nom_comm.nom_comm)
