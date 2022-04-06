# Generated by Django 4.0.1 on 2022-01-14 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='null', upload_to='')),
                ('public', models.BooleanField()),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('uppdate_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
