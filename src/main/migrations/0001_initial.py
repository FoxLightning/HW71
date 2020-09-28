import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=128)),
                ('text', models.TextField(max_length=1024)),
                ('sends', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoogleLead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=4, verbose_name='Method')),
                ('path', models.CharField(max_length=100, verbose_name='Path')),
                ('response_time', models.CharField(max_length=100, verbose_name='Response time')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('l_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('b_date', models.DateField(verbose_name='Date of birth')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone', models.CharField(default=None, max_length=30, verbose_name='Phone number')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('p_date', models.CharField(max_length=100, verbose_name='Publication date')),
                ('authors', models.ManyToManyField(to='main.User')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                               to='main.category')),
            ],
        ),
    ]
