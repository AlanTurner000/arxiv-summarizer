# Generated by Django 4.1.6 on 2023-02-22 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer', '0008_alter_pickleddata_docstore_pickle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickleddata',
            name='buffer',
            field=models.BinaryField(editable=True),
        ),
        migrations.AlterField(
            model_name='pickleddata',
            name='index_to_docstore_id_pickle',
            field=models.BinaryField(editable=True),
        ),
    ]