# Generated by Django 4.1.7 on 2023-04-06 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriya',
            options={'verbose_name_plural': 'categorys'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='newsimage',
            options={'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name_plural': 'Regions'},
        ),
        migrations.AlterField(
            model_name='newsimage',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.news'),
        ),
        migrations.CreateModel(
            name='StatuxNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('dis_like', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.news')),
            ],
        ),
    ]
