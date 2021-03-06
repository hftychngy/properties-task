# Generated by Django 3.1 on 2020-08-17 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_unit', models.CharField(choices=[('SqFt', 'Square Feet')], default='SqFt', help_text='unit used to define measurements.', max_length=32)),
                ('home_type', models.CharField(choices=[('SingleFamily', 'Single Family'), ('VacantResidentialLand', 'Vacant Residential Land'), ('Miscellaneous', 'Miscellaneous'), ('Apartment', 'Condominium'), ('Condominium', 'Condominium'), ('Duplex', 'Duplex'), ('MultiFamily2To4', 'Multi-Family 2 to 4')], default='SingleFamily', help_text='Home Type', max_length=32)),
                ('bathrooms', models.DecimalField(blank=True, decimal_places=2, help_text='Number of bathrooms', max_digits=6, null=True)),
                ('bedrooms', models.IntegerField(blank=True, help_text='Number of bedrooms', null=True)),
                ('home_size', models.IntegerField(blank=True, help_text='Home Size', null=True)),
                ('property_size', models.IntegerField(blank=True, help_text='Property Size', null=True)),
                ('link', models.URLField(blank=True, help_text='URL for listing', null=True)),
                ('last_sold_date', models.DateField(blank=True, help_text='Last Sold Date', null=True)),
                ('last_sold_price', models.DecimalField(blank=True, decimal_places=4, help_text='Last Sold Price', max_digits=13, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=4, help_text='Current Property Price', max_digits=13, null=True)),
                ('rent_price', models.DecimalField(blank=True, decimal_places=4, help_text='Rent Price', max_digits=10, null=True)),
                ('rentzestimate_amount', models.DecimalField(blank=True, decimal_places=4, help_text='Estimated Rent Price', max_digits=13, null=True)),
                ('rentzestimate_last_updated', models.DateField(blank=True, help_text='Estimated Rent Price Last Update', null=True)),
                ('tax_value', models.DecimalField(blank=True, decimal_places=4, help_text='Tax Value', max_digits=13, null=True)),
                ('tax_year', models.IntegerField(blank=True, help_text='Tax Year', null=True)),
                ('year_built', models.IntegerField(blank=True, help_text='Year Built', null=True)),
                ('zillow_id', models.IntegerField(blank=True, help_text='Zillow ID', null=True)),
                ('zestimate_amount', models.DecimalField(blank=True, decimal_places=4, help_text='Zillow Estimate', max_digits=13, null=True)),
                ('zestimate_last_updated', models.DateField(blank=True, help_text='Zillow Estimate', null=True)),
                ('address', models.CharField(help_text='Street Address', max_length=255)),
                ('city', models.CharField(help_text='City', max_length=128)),
                ('state', models.CharField(help_text='State', max_length=8)),
                ('zipcode', models.IntegerField(help_text='Zip Code')),
            ],
        ),
    ]
