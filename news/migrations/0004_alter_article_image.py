# Generated by Django 5.1.3 on 2024-12-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_article_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(upload_to="news/images/article/"),
        ),
    ]
