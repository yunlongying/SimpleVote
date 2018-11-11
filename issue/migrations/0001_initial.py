# Generated by Django 2.1.3 on 2018-11-11 09:39

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IssueModel',
            fields=[
                ('issue_id', models.CharField(db_column='ISSUE_ID', max_length=200, primary_key=True, serialize=False)),
                ('issue_name', models.CharField(db_column='ISSUE_NAME', max_length=200)),
                ('choice', jsonfield.fields.JSONField(db_column='choice', default=[])),
                ('create_date', models.DateTimeField(db_column='CREATE_DATE')),
            ],
            options={
                'db_table': 'ISSUE',
            },
        ),
    ]
