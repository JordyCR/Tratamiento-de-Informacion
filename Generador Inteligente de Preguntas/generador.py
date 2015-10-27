# -*- encoding: utf-8 -*-
from AlchemyAPI import AlchemyAPI
import json
import os
from os.path import isfile, join

demo_text = 'Beethoven was the grandson of Ludwig van Beethoven (de) (1712–73), a musician from the town of Mechelen in the Duchy of Brabant in the Flemish region of what is now Belgium, who at the age of twenty moved to Bonn.[2][3] Ludwig (he adopted the German cognate of the Dutch Lodewijk) was employed as a bass singer at the court of the Elector of Cologne, eventually rising to become Kapellmeister (music director). Ludwig had one son, Johann (1740–1792), who worked as a tenor in the same musical establishment and gave lessons on piano and violin to supplement his income.[2] Johann married Maria Magdalena Keverich in 1767; she was the daughter of Johann Heinrich Keverich, who had been the head chef at the court of the Archbishopric of Trier.[4]'


RAIZ = './Bio/'
EXTENSION = ".txt"

archivos_txt = []
for base, dirs, files in os.walk(RAIZ): # Escaneamos el arbol de ficheros
    for file in files:
        fich = join(base, file)
        if fich.endswith(EXTENSION):
            archivos_txt.append(fich)

# demo_text = ''
# for archivo in archivos_txt:
#     f = open(archivo, 'r')
#     demo_text += f.read() + '\n'
#     f.close()

# demo_text_list = filter(None, demo_text.split('\n'))

# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()


# print('')
# print('')
# print('############################################')
# print('#   Entity Extraction Example              #')
# print('############################################')
# print('')
# print('')

# #print('Processing text: ', demo_text)
# print('')

# response = alchemyapi.entities('text', demo_text, {'sentiment': 1})

# if response['status'] == 'OK':
#     print('## Response Object ##')
#     print(json.dumps(response, indent=4))

#     print('')
#     print('## Entities ##')
#     for entity in response['entities']:
#         print('text: ', entity['text'].encode('utf-8'))
#         print('type: ', entity['type'])
#         print('relevance: ', entity['relevance'])
#         print('sentiment: ', entity['sentiment']['type'])
#         if 'score' in entity['sentiment']:
#             print('sentiment score: ' + entity['sentiment']['score'])
#         print('')
# else:
#     print('Error in entity extraction call: ', response['statusInfo'])



# print('')
# print('')
# print('')
# print('############################################')
# print('#   Relation Extraction Example            #')
# print('############################################')
# print('')
# print('')

#print('Processing text: ', demo_text)
#print('')


s_what = 'What did'
s_where = 'Where did'
fc = open('./Bio/Cuestionario.txt', 'w')
cuestionario = ''
demo_text = ''
sub = verb = verb_lemma = res = p = r = ''

for archivo in archivos_txt:

    f = open(archivo, 'r')
    demo_text = f.read()
    demo_text_list = filter(None, demo_text.split('\n'))

    for _text in demo_text_list:
        response = alchemyapi.relations('text', _text)

        if response['status'] == 'OK':
            # print(json.dumps(response, indent=4))

            for relation in response['relations']:
                if not 'object' in relation and not 'location' in relation: 
                    continue


                elif 'subject' in relation and 'action' in relation and 'object' in relation:
                        sub = relation['subject']['text'].encode('utf-8') 
                        verb = relation['action']['text'].encode('utf-8')
                        verb_lemma = relation['action']['lemmatized'].encode('utf-8')
                        res = relation['object']['text'].encode('utf-8')
                        p = "%s %s %s%s" % (s_what, sub, verb_lemma, '?')
                        r = "%s %s %s" % (sub, verb, res)
                        w = p + '\nR = ' + r.capitalize() + '\n\n' 
                        cuestionario += w


                elif 'subject' in relation and 'action' in relation and 'location' in relation:
                        sub = relation['subject']['text'].encode('utf-8') 
                        verb = relation['action']['text'].encode('utf-8')
                        verb_lemma = relation['action']['lemmatized'].encode('utf-8')
                        res = relation['location']['text'].encode('utf-8')
                        p = "%s %s %s%s" % (s_where, sub, verb_lemma, '?')
                        r = "%s %s %s" % (sub, verb, res)
                        w = p + '\nR = ' + r.capitalize() + '\n\n' 
                        cuestionario += w 

                elif 'location' in relation and 'object' in relation:
                    sub = relation['subject']['text'].encode('utf-8') 
                    verb = relation['action']['text'].encode('utf-8')
                    verb_lemma = relation['action']['lemmatized'].encode('utf-8')
                    res = relation['object']['text'].encode('utf-8')
                    p = "%s %s %s%s" % (s_what, sub, verb_lemma, '?')
                    r = "%s %s %s" % (sub, verb, res)
                    w = p + '\nR = ' + r.capitalize() + '\n\n' 
                    cuestionario += w

                    sub = relation['subject']['text'].encode('utf-8') 
                    verb = relation['action']['text'].encode('utf-8')
                    verb_lemma = relation['action']['lemmatized'].encode('utf-8')
                    res = relation['location']['text'].encode('utf-8')
                    p = "%s %s %s%s" % (s_where, sub, verb_lemma, '?')
                    r = "%s %s %s" % (sub, verb, res)
                    w = p + '\nR = ' + r.capitalize() + '\n\n' 
                    cuestionario += w


                # if 'subject' in relation:
                #     print('Subject: ', relation['subject']['text'].encode('utf-8'))
                # if 'action' in relation:
                #     print('Action: ', relation['action']['text'].encode('utf-8'))
                # if 'object' in relation:
                #     print('Object: ', relation['object']['text'].encode('utf-8'))
                # if 'location' in relation:
                #     print('Location: ', relation['location']['text'].encode('utf-8'))

        else:
            print('Error in relation extaction call: ', response['statusInfo'])

    f.close()

fc.write(cuestionario)
fc.close()
