# Generated by Django 4.2.7 on 2023-11-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_student_add_date_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='add_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=6, null=True),
        ),
    ]