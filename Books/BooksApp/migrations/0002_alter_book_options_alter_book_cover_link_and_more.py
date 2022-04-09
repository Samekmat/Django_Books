# Generated by Django 4.0.3 on 2022-04-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='page_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(null=True),
        ),
    ]
