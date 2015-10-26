# -*- encoding: utf-8 -*-
from AlchemyAPI import AlchemyAPI
import json

demo_text = 'Beethoven was the grandson of Ludwig van Beethoven (de) (1712–73), a musician from the town of Mechelen in the Duchy of Brabant in the Flemish region of what is now Belgium, who at the age of twenty moved to Bonn.[2][3] Ludwig (he adopted the German cognate of the Dutch Lodewijk) was employed as a bass singer at the court of the Elector of Cologne, eventually rising to become Kapellmeister (music director). Ludwig had one son, Johann (1740–1792), who worked as a tenor in the same musical establishment and gave lessons on piano and violin to supplement his income.[2] Johann married Maria Magdalena Keverich in 1767; she was the daughter of Johann Heinrich Keverich, who had been the head chef at the court of the Archbishopric of Trier.[4]'


# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()


print('')
print('')
print('############################################')
print('#   Entity Extraction Example              #')
print('############################################')
print('')
print('')

#print('Processing text: ', demo_text)
print('')

response = alchemyapi.entities('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Entities ##')
    for entity in response['entities']:
        print('text: ', entity['text'].encode('utf-8'))
        print('type: ', entity['type'])
        print('relevance: ', entity['relevance'])
        print('sentiment: ', entity['sentiment']['type'])
        if 'score' in entity['sentiment']:
            print('sentiment score: ' + entity['sentiment']['score'])
        print('')
else:
    print('Error in entity extraction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Relation Extraction Example            #')
print('############################################')
print('')
print('')

#print('Processing text: ', demo_text)
print('')

response = alchemyapi.relations('text', demo_text)

if response['status'] == 'OK':
    print('## Object ##')
    print(json.dumps(response, indent=4))

    print('')
    print('## Relations ##')
    for relation in response['relations']:
        if 'subject' in relation:
            print('Subject: ', relation['subject']['text'].encode('utf-8'))

        if 'action' in relation:
            print('Action: ', relation['action']['text'].encode('utf-8'))

        if 'object' in relation:
            print('Object: ', relation['object']['text'].encode('utf-8'))

        print('')
else:
    print('Error in relation extaction call: ', response['statusInfo'])


