# Generated by Django 4.2.7 on 2023-12-16 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_title_brands_name_rename_title_product_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='categories',
            name='list_of_brands',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='list_of_products',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('list_of_brands', models.ManyToManyField(to='products.brand')),
                ('list_of_products', models.ManyToManyField(related_name='Category', to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='list_of_categories',
            field=models.ManyToManyField(to='products.category'),
        ),
        migrations.AddField(
            model_name='brand',
            name='list_of_products',
            field=models.ManyToManyField(related_name='Brand', to='products.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='list_of_brands',
            field=models.ManyToManyField(to='products.brand'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='list_of_categories',
            field=models.ManyToManyField(to='products.category'),
        ),
        migrations.DeleteModel(
            name='Brands',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
