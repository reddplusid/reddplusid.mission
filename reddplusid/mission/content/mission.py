from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText
from plone.z3cform.textlines.textlines import TextLinesFieldWidget
from collective.z3cform.widgets.enhancedtextlines import \
EnhancedTextLinesFieldWidget
from plone.formwidget.autocomplete import AutocompleteFieldWidget
from plone.formwidget.autocomplete import AutocompleteMultiFieldWidget

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

import p01.vocabulary.country

from reddplusid.mission import MessageFactory as _


# Interface class; used to define content-type schema.

streams = SimpleVocabulary(
        [SimpleTerm(value=u'Conservation of Biodiversity', 
            title=_(u'Conservation of Biodiversity')),
         SimpleTerm(value=u'Reduction in Carbon Emissions', 
            title=_(u'Reduction in Cargon Emissions')),
         SimpleTerm(value=u'Community Forest Management', 
            title=_(u'Community Forest Management')),
         SimpleTerm(value=u'Participatory Mapping', 
            title=_(u'Participatory Mapping')),
         SimpleTerm(value=u'Restoration of Degraded Land', 
            title=_(u'Restoration of Degraded Land')),
            ]
        ) 

mission_funding_sources = SimpleVocabulary(
        [SimpleTerm(value=u'Multilateral', 

            title=_(u'Multilateral')),
         SimpleTerm(value=u'Bilateral', 
            title=_(u'Bilateral')),
         SimpleTerm(value=u'Private Sector', 
            title=_(u'Private Sector')),
         SimpleTerm(value=u'Financial Instituition', 
            title=_(u'Financial Instituition')),
         SimpleTerm(value=u'Government', 
            title=_(u'Government')),
         SimpleTerm(value=u'CSO', 
            title=_(u'CSO')),
         SimpleTerm(value=u'Non-Profit Foundation', 
            title=_(u'Non-Profit Foundation')),
         ])

mission_scope_type = SimpleVocabulary(
        [SimpleTerm(value=u'International', 
            title=_(u'International')),
         SimpleTerm(value=u'National', 
            title=_(u'National')),
         SimpleTerm(value=u'Regional', 
            title=_(u'Regional')),
         ])

#Probably better to be parsed from a CSV
id_provinces = SimpleVocabulary(
            [
                SimpleTerm(value=u'ID-AC', title=_(u'Aceh')),
                SimpleTerm(value=u'ID-BA', title=_(u'Bali')),
                SimpleTerm(value=u'ID-BB', title=_(u'Bangka Belitung')),
                SimpleTerm(value=u'ID-BT', title=_(u'Banten')),
                SimpleTerm(value=u'ID-BE', title=_(u'Bengkulu')),
                SimpleTerm(value=u'ID-GO', title=_(u'Gorontal')),
                SimpleTerm(value=u'ID-JA', title=_(u'Jambi')),
                SimpleTerm(value=u'ID-JB', title=_(u'Jawa Barat')),
                SimpleTerm(value=u'ID-JT', title=_(u'Jawa Tengah')),
                SimpleTerm(value=u'ID-JI', title=_(u'Jawa Timur')),
                SimpleTerm(value=u'ID-KB', title=_(u'Kalimantan Barat')),
                SimpleTerm(value=u'ID-KS', title=_(u'Kalimantan Selatan')),
                SimpleTerm(value=u'ID-KT', title=_(u'Kalimantan Tengah')),
                SimpleTerm(value=u'ID-KI', title=_(u'Kalimantan Timur')),
                SimpleTerm(value=u'ID-KU', title=_(u'Kalimantan Utara')),
                SimpleTerm(value=u'ID-KR', title=_(u'Kepulauan Riau')),
                SimpleTerm(value=u'ID-LA', title=_(u'Lampung')),
                SimpleTerm(value=u'ID-MA', title=_(u'Maluku')),
                SimpleTerm(value=u'ID-MU', title=_(u'Maluku Utara')),
                SimpleTerm(value=u'ID-NB', title=_(u'Nusa Tenggara Barat')),
                SimpleTerm(value=u'ID-NT', title=_(u'Nusa Tenggara Timur')),
                SimpleTerm(value=u'ID-PA', title=_(u'Papua')),
                SimpleTerm(value=u'ID-PB', title=_(u'Papua Barat')),
                SimpleTerm(value=u'ID-RI', title=_(u'Riau')),
                SimpleTerm(value=u'ID-SR', title=_(u'Sulawesi Barat')),
                SimpleTerm(value=u'ID-SN', title=_(u'Sulawesi Selatan')),
                SimpleTerm(value=u'ID-ST', title=_(u'Sulawesi Tengah')),
                SimpleTerm(value=u'ID-SG', title=_(u'Sulawesi Tenggara')),
                SimpleTerm(value=u'ID-SA', title=_(u'Sulawesi Utara')),
                SimpleTerm(value=u'ID-SB', title=_(u'Sumatera Barat')),
                SimpleTerm(value=u'ID-SS', title=_(u'Sumatera Selatan')),
                SimpleTerm(value=u'ID-SU', title=_(u'Sumatera Utara')),
                SimpleTerm(value=u'ID-JK', title=_(u'Jakarta Raya')),
                SimpleTerm(value=u'ID-YO', title=_(u'Yogyakarta')),
            ]

            )   
class IMission(form.Schema, IImageScaleTraversable):
    """
    REDD+ Indonesia Mission
    """

    title = schema.TextLine(title=u'Mission', 
                         description=u'Brief title of mission. eg. '
                         'Public Consultation for REDD+ Workshop.')

    description = schema.Text(title=u'Overall Objective', 
                         description=u'Briefly describe the objectives '
                         'of the mission.')

    start = schema.Datetime(
            title=_(u'Start date'),
            )

    end  = schema.Datetime(
            title=_(u'End date'),
            )
    
    output_stream = schema.Choice(
                vocabulary=streams,
                title=_(u'Output Stream'),
                description=_(u'Select Streams'),
                required=True,
                )

    output_contribution = RichText(
                title=_(u'Contribution to selected output stream'),
                description=_(u'Please describe briefly how your '
                    'mission has contributed to realizing the '
                    'relevant stream outcome'),
                )

    mission_funding_source = schema.Choice(
            title=_(u'Source of Mission Funding'),
            vocabulary=mission_funding_sources,
            required=True,
            )

    form.widget(mission_members=AutocompleteMultiFieldWidget)
    mission_members= schema.List(
            title=_(u'Mission Members'),
            description=_(u'List of Mission Members. Enter '
                'name to search, select and press Enter to add. Repeat to '
                'to add additional members.'),
            value_type=schema.Choice(vocabulary=u"plone.principalsource.Users",),
            missing_value=(),
            required=True,
            )

    form.widget(mission_author=AutocompleteMultiFieldWidget)
    mission_author= schema.List(
            title=_(u'Author'),
            description=_(u'List of Authors. Enter '
                'name to search, select and press Enter to add. Repeat to '
                'to add additional members with principal author first.'),
            value_type=schema.Choice(vocabulary=u"plone.principalsource.Users"),
            missing_value=(),
            required=True,
            )

    form.widget(mission_support_staff=AutocompleteMultiFieldWidget)
    mission_support_staff= schema.List(
            title=_(u'Support Staff'),
            description=_(u'List of support staff '
                'that have made a contribution to the success '
                'of the mission. Enter name to search. Select and '
                'press enter to add. Repeat to add additional staff.'),
            value_type=schema.Choice(vocabulary=u"plone.principalsource.Users"),
            missing_value=(),
            required=True,
            )

    mission_scope= schema.Choice(
            title=_(u'Mission Scope'),
            vocabulary=mission_scope_type,
            )

    id_province = schema.Choice(
            title=_(u'Province'),
            description=_(u'If Mission Scope is National, please select '
            'a province.'),
            vocabulary=id_provinces,
            required=False,
            missing_value=(),
            )

    country = schema.Choice(
            title=_(u'Country'),
            description=_(u'If Mission Scope is International, please select '
            'a country.'),
            source=p01.vocabulary.country.ISO3166Alpha2CountryVocabulary(None),
            required=False,
            )

    form.widget(mission_location=EnhancedTextLinesFieldWidget)
    mission_location= schema.Tuple(
            title=_(u'City / Location (One per line)'),
            description=_(u'Fill in city or location name and click Add button.'),
            value_type=schema.TextLine(),
            missing_value=(),
            required=True,
            )
