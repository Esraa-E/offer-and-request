# Generated by Django 4.2.3 on 2024-03-11 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_addoffermodel_commentmodel_requestmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='offerImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('offerimg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.offermodel')),
            ],
        ),
    ]
