# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Garage'
        db.create_table('gsk_garage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=5)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('second_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('passport_data', self.gf('django.db.models.fields.TextField')()),
            ('length', self.gf('django.db.models.fields.FloatField')()),
            ('width', self.gf('django.db.models.fields.FloatField')()),
            ('electric_meter_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('gsk', ['Garage'])

        # Adding model 'Pass'
        db.create_table('gsk_pass', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pass_holder_last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cars_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_until', self.gf('django.db.models.fields.DateField')()),
            ('garage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gsk.Garage'])),
        ))
        db.send_create_signal('gsk', ['Pass'])

        # Adding model 'ElectricMeterReading'
        db.create_table('gsk_electricmeterreading', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reading_date', self.gf('django.db.models.fields.DateField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('garage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gsk.Garage'])),
        ))
        db.send_create_signal('gsk', ['ElectricMeterReading'])

        # Adding model 'Payment'
        db.create_table('gsk_payment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('check_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('amount', self.gf('django.db.models.fields.FloatField')()),
            ('payment_date', self.gf('django.db.models.fields.DateField')()),
            ('tariff', self.gf('django.db.models.fields.FloatField')()),
            ('garage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gsk.Garage'])),
        ))
        db.send_create_signal('gsk', ['Payment'])


    def backwards(self, orm):
        # Deleting model 'Garage'
        db.delete_table('gsk_garage')

        # Deleting model 'Pass'
        db.delete_table('gsk_pass')

        # Deleting model 'ElectricMeterReading'
        db.delete_table('gsk_electricmeterreading')

        # Deleting model 'Payment'
        db.delete_table('gsk_payment')


    models = {
        'gsk.electricmeterreading': {
            'Meta': {'object_name': 'ElectricMeterReading'},
            'garage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gsk.Garage']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reading_date': ('django.db.models.fields.DateField', [], {}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'gsk.garage': {
            'Meta': {'object_name': 'Garage'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'electric_meter_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5'}),
            'passport_data': ('django.db.models.fields.TextField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'width': ('django.db.models.fields.FloatField', [], {})
        },
        'gsk.pass': {
            'Meta': {'object_name': 'Pass'},
            'application': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cars_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_until': ('django.db.models.fields.DateField', [], {}),
            'garage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gsk.Garage']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pass_holder_last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'gsk.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'check_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'garage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gsk.Garage']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_date': ('django.db.models.fields.DateField', [], {}),
            'tariff': ('django.db.models.fields.FloatField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['gsk']