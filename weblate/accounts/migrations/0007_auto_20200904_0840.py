# Generated by Django 3.0.7 on 2020-09-04 08:40

from django.db import migrations, models

import weblate.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_auto_20200903_0817"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="company",
            field=models.CharField(blank=True, max_length=100, verbose_name="Company"),
        ),
        migrations.AddField(
            model_name="profile",
            name="github",
            field=models.SlugField(blank=True, verbose_name="GitHub username"),
        ),
        migrations.AddField(
            model_name="profile",
            name="linkedin",
            field=models.SlugField(
                blank=True,
                help_text="Your LinkedIn profile name from linkedin.com/in/profilename",
                verbose_name="LinkedIn profile name",
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="location",
            field=models.CharField(blank=True, max_length=100, verbose_name="Location"),
        ),
        migrations.AddField(
            model_name="profile",
            name="public_email",
            field=weblate.utils.fields.EmailField(
                blank=True, max_length=190, verbose_name="Public email"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="twitter",
            field=models.SlugField(blank=True, verbose_name="Twitter username"),
        ),
        migrations.AddField(
            model_name="profile",
            name="website",
            field=models.URLField(blank=True, verbose_name="Website URL"),
        ),
        migrations.AlterField(
            model_name="verifiedemail",
            name="email",
            field=models.EmailField(max_length=190),
        ),
    ]