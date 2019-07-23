#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	19/07/2019 16:45:18
#+ Editado:	22/07/2019 14:04:21
## do ficheiro mediadb.py
#------------------------------------------------------------------------------------------------
import json
from pathlib import Path
#------------------------------------------------------------------------------------------------
texto_config = '''
# selecionar carpeta raiz, . significa carpeta actual
raiz=.

# selecionar o idioma para a versión interactiva
# galego (gl), inglés (en), castelán (es)
lang=gl

# nome da base de datos
nome=indice.json
'''
#------------------------------------------------------------------------------------------------
# función encargada de cargar ficheiros tipo json
def cargar_json(fich):
	if Path(fich).is_file():
		return json.loads(open(fich).read())
	else:
		open(fich, 'w').write('{}')
		return json.loads(open(fich).read())
#------------------------------------------------------------------------------------------------
# función de gardado de ficheiros tipo json
def gardar_json(fich, contido, sort=False):
	open(fich, 'w').write(json.dumps(contido, indent=4, sort_keys=sort, ensure_ascii=False))
#------------------------------------------------------------------------------------------------
def crear_carp(carp):
	if Path(carp).is_dir() == False:
		Path(carp).mkdir(parents=True, exist_ok=True)
#------------------------------------------------------------------------------------------------
def pJson(diccionario, sort=False):
	print(json.dumps(diccionario, indent=4, sort_keys=sort))
#------------------------------------------------------------------------------------------------
# función para ler o ficheiro de configuración e devolver as variables adecuadas
def read_config():
	fich = '../.config'
	if Path(fich).is_file():
		config = {}
		'''
		lemos todas as liñas do ficheiro e quitamoslle os \n
		de todas as liñas só nos quedamos coas que non comezan por un comentario
		Das liñas de configuración o que facemos e separalas por igual e quedarnos
		co segundo elemento, co cal a orde dos elementos non debe ser alterada.
		Poderíase facer que mirase o nome da variable pero da pereza e non ten sentido.
		'''
		for x in open(fich):
			''' facemos isto porque debe ser máis eficiente ca facer senón strip
			cada vez que chamemos a x'''
			x = x.strip()
			if not x.startswith('#') and x != '':
				config[x.split('=')[0].strip()] = x.split('=')[1].strip()
		return config

		# vello método dependente da orde
		# return [x.strip().split('=')[1] for x in open(fich) if not x.strip().startswith('#') and x.strip() != '']

	else:
		open(fich, 'w').write(texto_config)
		return read_config()
#------------------------------------------------------------------------------------------------
