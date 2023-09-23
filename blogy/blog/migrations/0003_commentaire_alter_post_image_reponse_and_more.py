# Generated by Django 4.2.5 on 2023-09-21 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_comm', models.CharField(blank=True, max_length=100)),
                ('corps', models.TextField(max_length=150)),
                ('data_added', models.DateTimeField(auto_now=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['data_added'],
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='image'),
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corps', models.TextField(max_length=150)),
                ('data_added', models.DateTimeField(auto_now=True)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nom_comm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reponses', to='blog.commentaire')),
            ],
        ),
        migrations.AddField(
            model_name='commentaire',
            name='nom_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]
