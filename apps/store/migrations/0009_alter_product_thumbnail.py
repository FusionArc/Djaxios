# Generated by Django 3.2 on 2021-05-05 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads'),
        ),
    ]
