# Generated by Django 4.1.7 on 2023-03-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0003_alter_quote_author_alter_tag_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='tags',
            field=models.ManyToManyField(to='quotes_app.tag'),
        ),
    ]