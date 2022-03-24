# Generated by Django 4.0.3 on 2022-03-24 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateTimeField()),
                ('isbn', models.CharField(max_length=16)),
                ('slug', models.SlugField()),
                ('cover', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
                ('authors', models.ManyToManyField(to='books.author')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_number', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_number', models.IntegerField()),
                ('page_number', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.exercise')),
            ],
        ),
    ]
