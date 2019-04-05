# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='StyledLink',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', primary_key=True, auto_created=True, related_name='djangocms_styledlink_styledlink', parent_link=True, serialize=False, on_delete=models.CASCADE)),
                ('label', models.CharField(help_text='Required. The text that is linked.', verbose_name='link text', default='', blank=True, max_length=255)),
                ('title', models.CharField(help_text='Optional. If provided, will provide a tooltip for the link.', verbose_name='title', default='', blank=True, max_length=255)),
                ('int_destination_id', models.PositiveIntegerField(null=True, blank=True)),
                ('page_destination', models.CharField(help_text='Use this to specify an intra-page link. Can be used for the <em>current page</em> or with a specific internal destination. Do <strong>not</strong> include a leading “#”.', verbose_name='intra-page destination', blank=True, max_length=64)),
                ('int_hash', models.BooleanField(default=False)),
                ('ext_destination', models.TextField(verbose_name='external destination', default='', blank=True)),
                ('ext_follow', models.BooleanField(verbose_name='follow external link?', default=True, help_text='Let search engines follow this hyperlink?')),
                ('mailto', models.EmailField(null=True, verbose_name='email address', help_text='An email address. This will override an external url.', blank=True, max_length=254)),
                ('target', models.CharField(verbose_name='target', default='', blank=True, max_length=100, choices=[('', 'same window'), ('_blank', 'new window'), ('_parent', 'parent window'), ('_top', 'topmost frame')], help_text='Optional. Specify if this link should open in a new tab or window.')),
                ('int_destination_type', models.ForeignKey(null=True, to='contenttypes.ContentType', blank=True, on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='StyledLinkStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('label', models.CharField(help_text='The internal name of this link style.', verbose_name='label', default='', max_length=32)),
                ('link_class', models.CharField(help_text='The class to add to this link (do NOT preceed with a ".").', verbose_name='link class', default='', max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='styledlink',
            name='styles',
            field=models.ManyToManyField(to='djangocms_styledlink.StyledLinkStyle', verbose_name='link style', default=None, blank=True, related_name='styled_link_style', help_text='Optional. Choose one or more styles for this link.'),
        ),
    ]
