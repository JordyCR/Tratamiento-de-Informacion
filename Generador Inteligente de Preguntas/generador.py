# -*- encoding: utf-8 -*-
from AlchemyAPI import AlchemyAPI
import json
import os
from os.path import isfile, join


RAIZ = './Bio/'
EXTENSION = ".txt"
str_cuestionario = 'Cuestionario_'

archivos_txt = []
for base, dirs, files in os.walk(RAIZ): # Escaneamos el arbol de ficheros
    for file in files:
        fich = join(base, file)
        if fich.endswith(EXTENSION) and not str_cuestionario in fich:
            archivos_txt.append(fich)


alchemyapi = AlchemyAPI()

s_what = 'What did'
s_where = 'Where did'

demo_text = ''
sub = verb = verb_lemma = res = p = r = ''

for archivo in archivos_txt:

    f = open(archivo, 'r')

    cuestionario = ''
    fc = open( RAIZ + 'Cuestionario_' + archivo[len(RAIZ):], 'w')

    demo_text = f.read()
    demo_text_list = filter(None, demo_text.split('\n'))

    for _text in demo_text_list:
        response = alchemyapi.relations('text', _text)

        if response['status'] == 'OK':

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

        else:
            print('Error in relation extaction call: ', response['statusInfo'])

    f.close()
    fc.write(cuestionario)
    fc.close()