# Generated by Django 3.1.5 on 2021-01-13 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsLetterRecients',
            new_name='NewsLetterRecipients',
        ),
    ]
