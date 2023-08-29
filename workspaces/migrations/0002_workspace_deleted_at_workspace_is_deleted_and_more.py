
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='workspace',
            name='is_deleted',
            field=models.BooleanField(blank=True, db_index=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='workspacesmembership',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='workspacesmembership',
            name='is_deleted',
            field=models.BooleanField(blank=True, db_index=True, editable=False, null=True),
        ),
    ]
