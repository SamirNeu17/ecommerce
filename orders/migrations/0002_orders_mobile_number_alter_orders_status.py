# Generated by Django 4.2.7 on 2023-12-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="mobile_number",
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="orders",
            name="status",
            field=models.CharField(
                choices=[
                    ("shipped", "shipped"),
                    ("cancelled", "cancelled"),
                    ("pending", "pending"),
                    ("delivered", "delivered"),
                ],
                default="pending",
                max_length=50,
            ),
        ),
    ]
