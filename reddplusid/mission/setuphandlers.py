from collective.grok import gs
from reddplusid.mission import MessageFactory as _

@gs.importstep(
    name=u'reddplusid.mission', 
    title=_('reddplusid.mission import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('reddplusid.mission.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
