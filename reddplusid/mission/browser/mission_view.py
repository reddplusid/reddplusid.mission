from five import grok
from plone.directives import dexterity, form
from reddplusid.mission.content.mission import IMission

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IMission)
    grok.require('zope2.View')
    grok.template('mission_view')
    grok.name('view')

