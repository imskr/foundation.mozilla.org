# Generated by Django 2.2.10 on 2020-03-11 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0092_auto_20200220_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('indexpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailpages.IndexPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailpages.indexpage',),
        ),
    ]
