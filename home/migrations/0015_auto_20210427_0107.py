# Generated by Django 3.1.6 on 2021-04-26 22:07

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_luckycoupon_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='luckycoupon',
            options={'verbose_name_plural': 'Kazanan Kupon Numaralar─▒'},
        ),
        migrations.RemoveField(
            model_name='luckycoupon',
            name='luckynumber1',
        ),
        migrations.RemoveField(
            model_name='luckycoupon',
            name='luckynumber2',
        ),
        migrations.RemoveField(
            model_name='luckycoupon',
            name='luckynumber3',
        ),
        migrations.RemoveField(
            model_name='luckycoupon',
            name='luckynumber4',
        ),
        migrations.RemoveField(
            model_name='luckycoupon',
            name='luckynumber5',
        ),
        migrations.RemoveField(
            model_name='luckycoupon',
            name='luckynumber6',
        ),
        migrations.AddField(
            model_name='luckycoupon',
            name='luckynumbers',
            field=models.CharField(default=home.models.lucky, max_length=40, null=True, verbose_name='Kazanan Kupon'),
        ),
    ]
