# Generated by Django 3.0.4 on 2020-03-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('TC', 'Technology'), ('CR', 'Curiositys'), ('GR', 'General')], default='GR', max_length=2),
        ),
    ]