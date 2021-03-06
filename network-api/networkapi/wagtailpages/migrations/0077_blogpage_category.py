# Generated by Django 2.2.4 on 2019-08-30 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0076_merge_20190830_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='category',
            field=models.ManyToManyField(blank=True, help_text='Which blog categories is this blog page associated with?', to='wagtailpages.BlogPageCategory', verbose_name='Categories'),
        ),
    ]
