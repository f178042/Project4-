# Generated by Django 3.2.5 on 2021-07-17 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Courses', '0001_initial'),
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Students.student')),
            ],
        ),
    ]
