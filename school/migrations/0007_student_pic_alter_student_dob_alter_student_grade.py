# Generated by Django 4.2.7 on 2023-11-12 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_student_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='pic',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateTimeField(null=True, verbose_name='Date of Birth(mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(),
        ),
    ]
