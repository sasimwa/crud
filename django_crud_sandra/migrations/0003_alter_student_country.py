# Generated by Django 4.1.7 on 2023-03-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_crud_sandra', '0002_student_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(default='nairobi', max_length=50),
        ),
    ]
