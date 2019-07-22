#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	19/07/2019 16:45:18
#+ Editado:	22/07/2019 14:04:21
#------------------------------------------------------------------------------------------------
import json
from pathlib import Path
#------------------------------------------------------------------------------------------------
texto_config = '''# NON ALTERAR O ORDE DAS LIÑAS CON ELEMENTOS DE CONFIGURACIÓN
# selecionar carpeta raiz, . significa carpeta actual
raiz=.

# selecionar o idioma para a versión interactiva
# galego (gl), inglés (en), castelán (es)
lang=gl
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
		# lemos todas as liñas do ficheiro e quitamoslle os \n e de todas as liñas só nos quedamos coas que non comezan por un comentario
		return [x.strip().split('=')[1] for x in open(fich) if not x.strip().startswith('#') and x.strip() != '']

	else:
		open(fich, 'w').write(texto_config)
		return read_config()
#------------------------------------------------------------------------------------------------
