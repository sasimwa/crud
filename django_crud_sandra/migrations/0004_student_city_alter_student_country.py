# Generated by Django 4.1.7 on 2023-03-02 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_crud_sandra', '0003_alter_student_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(default='nairobi', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(default='kenya', max_length=50),
        ),
    ]