# Generated by Django 4.0.2 on 2022-02-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_alter_project_polymorphic_ctype"),
    ]

    operations = [
        migrations.AddField(
            model_name="sequencelabelingproject",
            name="use_relation",
            field=models.BooleanField(default=False),
        ),
    ]
