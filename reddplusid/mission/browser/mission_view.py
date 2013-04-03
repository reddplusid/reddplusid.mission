from five import grok
from plone.directives import dexterity, form
from reddplusid.mission.content.mission import IMission

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IMission)
    grok.require('zope2.View')
    grok.template('mission_view')
    grok.name('view')

    
    def contains_missionreport(self):
        #Checks for existance of Mission Report in current Mission

        context = self.context

        cur_path = '/'.join(context.getPhysicalPath())
        path = {}

        path['query'] = cur_path
        path['depth'] = 1

        contentFilter = {}
        contentFilter['path'] = path
        contentFilter['portal_type'] = 'reddplusid.missionreport.missionreport'

        return bool(context.portal_catalog.queryCatalog(contentFilter))
