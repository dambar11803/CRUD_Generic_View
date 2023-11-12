# Generated by Django 4.2.7 on 2023-11-12 05:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_student_gender_alter_student_roll'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='add_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
