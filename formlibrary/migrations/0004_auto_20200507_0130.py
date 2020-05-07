# Generated by Django 2.2.10 on 2020-05-07 08:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('workflow', '0027_auto_20200428_0711'),
        ('formlibrary', '0003_auto_20200409_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                # ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=550, null=True)),
                ('form_verified_by', models.CharField(blank=True, max_length=255, null=True)),
                ('form_filled_by', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.IntegerField(help_text='Number of days? Sessions?')),
                ('cases', models.ManyToManyField(blank=True, to='formlibrary.Case')),
                ('contacts', models.ManyToManyField(blank=True, to='workflow.Contact')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='workflow.ActivityUser', verbose_name='Created by')),
                ('implementer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Stakeholder')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='workflow.ActivityUser', verbose_name='Modified by')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Office')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Program')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.Site')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainer_of', to='workflow.Contact')),
            ],
            options={
                'abstract': False,
            },
        ),
        # ! Fix for the id of Training model: https://stackoverflow.com/a/46295704/4017403
        # ? Was the training table already existent in the DB?
        migrations.AlterField(
            model_name='training',
            name='id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='training',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        # migrations.RemoveField(
        #     model_name='training',
        #     name='id'
        # ),
        # migrations.AddField(
        #     model_name='training',
        #     name='id',
        #     field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        # ),
        migrations.AlterModelOptions(
            name='distribution',
            options={'ordering': ('name',)},
        ),
        migrations.RenameField(
            model_name='distribution',
            old_name='distribution_indicator',
            new_name='indicator',
        ),
        migrations.RenameField(
            model_name='distribution',
            old_name='distribution_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='distribution',
            old_name='office_code',
            new_name='office',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='distribution_implementer',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='distributor_contact_number',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='distributor_name_and_affiliation',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='form_filled_by_contact_num',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='form_filled_by_position',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='form_filled_date',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='form_verified_by_contact_num',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='form_verified_by_position',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='form_verified_date',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='total_age_0_14_female',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='total_age_0_14_male',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='total_age_15_24_female',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='total_age_15_24_male',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='total_age_25_59_female',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='total_age_25_59_male',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='total_female',
        ),
        migrations.RemoveField(
            model_name='distribution',
            name='total_male',
        ),
        migrations.AddField(
            model_name='distribution',
            name='contacts',
            field=models.ManyToManyField(blank=True, to='workflow.Contact'),
        ),
        migrations.AddField(
            model_name='distribution',
            name='created_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='workflow.ActivityUser', verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='distribution',
            name='description',
            field=models.TextField(blank=True, max_length=550, null=True),
        ),
        migrations.AddField(
            model_name='distribution',
            name='implementer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Stakeholder'),
        ),
        migrations.AddField(
            model_name='distribution',
            name='modified_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='workflow.ActivityUser', verbose_name='Modified by'),
        ),
        migrations.AddField(
            model_name='distribution',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.Site'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        # ! Fix of the above commented code: https://stackoverflow.com/a/30985282/4017403
        migrations.RemoveField(
            model_name='distribution',
            name='id'
        ),
        migrations.AddField(
            model_name='distribution',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Program'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='individual',
            name='training',
            field=models.ManyToManyField(blank=True, to='formlibrary.Training'),
        ),
        migrations.AlterField(
            model_name='trainingattendance',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trainingattendance',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('case_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='formlibrary.Case')),
                ('name', models.CharField(max_length=255)),
            ],
            bases=('formlibrary.case',),
        ),
        migrations.CreateModel(
            name='Construction',
            fields=[
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=550, null=True)),
                ('form_verified_by', models.CharField(blank=True, max_length=255, null=True)),
                ('form_filled_by', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(max_length=255)),
                ('cases', models.ManyToManyField(blank=True, to='formlibrary.Case')),
                ('contacts', models.ManyToManyField(blank=True, to='workflow.Contact')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='workflow.ActivityUser', verbose_name='Created by')),
                ('implementer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Stakeholder')),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='workflow.ActivityUser', verbose_name='Modified by')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Office')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Program')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='distribution',
            name='cases',
            field=models.ManyToManyField(blank=True, to='formlibrary.Case'),
        ),
        migrations.AddField(
            model_name='individual',
            name='household',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='formlibrary.Household'),
        ),
    ]
