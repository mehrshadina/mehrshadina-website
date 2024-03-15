# Generated by Django 4.2.9 on 2024-03-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_time_required'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/img/')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, to='blog.image'),
        ),
    ]
