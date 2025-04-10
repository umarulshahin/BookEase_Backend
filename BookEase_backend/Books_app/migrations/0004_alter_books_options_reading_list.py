# Generated by Django 4.2.6 on 2025-04-09 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Books_app', '0003_alter_books_book_image_alter_books_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='Reading_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books_app.books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
