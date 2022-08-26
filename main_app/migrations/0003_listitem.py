# Generated by Django 4.1 on 2022-08-26 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_list_type_list_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('details', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('I', 'Item'), ('T', 'Task')], default='I', max_length=3)),
                ('time_estimate', models.CharField(choices=[('0', ''), ('2', '2 Mins'), ('5', '5 Mins'), ('10', '10 Mins'), ('15', '15 Mins'), ('20', '20 Mins'), ('30', '30 Mins'), ('45', '45 Mins'), ('60', '1 Hr'), ('120', '2 Hrs'), ('180', '3 Hrs'), ('240', '4 Hrs'), ('300', '5 Hrs'), ('360', '6 Hrs')], default='0', max_length=14)),
                ('priority', models.CharField(choices=[('N/A', ''), ('L', 'Low'), ('M', 'Medium'), ('H', 'High'), ('HH', 'Highest')], default='N/A', max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='main_app.list')),
            ],
        ),
    ]