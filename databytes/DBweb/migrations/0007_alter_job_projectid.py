# Generated by Django 4.0.4 on 2022-05-25 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DBweb', '0006_alter_job_jobdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='ProjectID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DBweb.project'),
        ),
    ]
