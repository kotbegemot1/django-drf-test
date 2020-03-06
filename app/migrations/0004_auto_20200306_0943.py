# Generated by Django 3.0 on 2020-03-06 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categorys',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='app.Category'),
        ),
    ]