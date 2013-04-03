from plone.indexer import indexer
from reddplusid.mission.content.mission import IMission
from reddplusid.mission.content.mission import id_provinces
import p01.vocabulary.country 
from five import grok

#searchable text index
@indexer(IMission)
def index_searchable(obj):

    results = []

    results.append(obj.mission_funding_source)
    results.append(getattr(obj, 'output_stream', ''))
    results.append(getattr(obj, 'obj.mission_scope', ''))
    results.append(getattr (obj, 'obj.mission_funding_source', ''))

    if obj.id_province:
        results.append(id_provinces.getTerm(obj.id_province).title)

    if obj.country:
        results.append(p01.vocabulary.country.ISO3166Alpha2CountryVocabulary(obj).getTerm(obj.country).title)

    results.append(obj.output_contribution.output)
    results.append(obj.title)
    results.append(obj.description)

    membership = obj.portal_membership

    if obj.mission_members:
        for memberId in obj.mission_members:
            member = membership.getMemberById(memberId)
            results.append(member.getProperty('fullname'))
    
   
    if obj.mission_support_staff:
        for memberId in obj.mission_support_staff:
            member = membership.getMemberById(memberId)
            results.append(member.getProperty('fullname'))

    return " ".join(results)

grok.global_adapter(index_searchable, name='SearchableText')
