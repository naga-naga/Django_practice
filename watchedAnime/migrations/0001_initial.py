# Generated by Django 3.1.1 on 2020-09-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='放送年')),
                ('updated_date', models.DateField(auto_now=True, verbose_name='登録日')),
            ],
        ),
    ]
