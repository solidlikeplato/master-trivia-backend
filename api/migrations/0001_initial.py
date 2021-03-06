# Generated by Django 2.2.7 on 2019-11-19 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(9, 'General Knowledge'), (10, 'Entertainment: Books'), (11, 'Entertainment: Film'), (12, 'Entertainment: Music'), (13, 'Entertainment: Musicals & Theatres'), (14, 'Entertainment: Television'), (15, 'Entertainment: Video Games'), (16, 'Entertainment: Board Games'), (17, 'Science & Nature'), (18, 'Science: Computers'), (19, 'Science: Mathematics'), (20, 'Mythology'), (21, 'Sports'), (22, 'Geography'), (23, 'History'), (24, 'Politics'), (25, 'Art'), (26, 'Celebrities'), (27, 'Animals'), (28, 'Vehicles'), (29, 'Entertainment: Comics'), (30, 'Science: Gadgets'), (31, 'Entertainment: Japanese Anime & Manga'), (32, 'Entertainment: Cartoon & Animations')])),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=6)),
                ('didGetRight', models.BooleanField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='api.Quiz')),
            ],
        ),
    ]
