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

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

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
 
class IMission(form.Schema, IImageScaleTraversable):
    """
    REDD+ Indonesia Mission
    """

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
                    'relevant country/regional outcome'),
                )

    mission_funding_source = schema.Choice(
            title=_(u'Source of Mission Funding'),
            vocabulary=mission_funding_sources,
            required=True,
            )

    form.widget(mission_members=EnhancedTextLinesFieldWidget)
    mission_members= schema.Tuple(
            title=_(u'Mission Members'),
            description=_(u'List of Mission Members. One name '
                'per line with principle member first.'),
            value_type=schema.TextLine(),
            missing_value=(),
            required=True,
            )

    form.widget(mission_author=EnhancedTextLinesFieldWidget)
    mission_author= schema.Tuple(
            title=_(u'Author'),
            description=_(u'List of authors. One name '
                'per line with principle author first.'),
            value_type=schema.TextLine(),
            missing_value=(),
            required=True,
            )

    form.widget(mission_support_staff=EnhancedTextLinesFieldWidget)
    mission_support_staff= schema.Tuple(
            title=_(u'Support Staff'),
            description=_(u'List of support staff '
                'that have made a contribution to the success'
                ' of the mission'),
            value_type=schema.TextLine(),
            missing_value=(),
            required=True,
            )

    form.widget(mission_location=EnhancedTextLinesFieldWidget)
    mission_location= schema.Tuple(
            title=_(u'City / Location (One per line)'),
            value_type=schema.TextLine(),
            missing_value=(),
            required=True,
            )

    mission_scope= schema.Choice(
            title=_(u'Mission Scope'),
            vocabulary=mission_scope_type,
            )
