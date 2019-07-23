#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	19/07/2019 16:45:18
#+ Editado:	23/07/2019 16:02:35
## do ficheiro mediadb.py
#------------------------------------------------------------------------------------------------
import json
from pathlib import Path
#------------------------------------------------------------------------------------------------
texto_config = '''
# selecionar carpeta raiz, . significa carpeta actual
ruta = .

# selecionar o idioma para a versión interactiva
# galego (gl), inglés (en), castelán (es)
lang=gl

# nome do ficheiro da base de datos, se non pos extensión non terá
nomeFich=indice.json
'''
#------------------------------------------------------------------------------------------------
# función encargada de cargar ficheiros tipo json sen a extensión
def cargar_json(fich):
	if Path(fich).is_file():
		return json.loads(open(fich).read())
	else:
		open(fich, 'w').write('{}')
		return json.loads(open(fich).read())
#------------------------------------------------------------------------------------------------
# función de gardado de ficheiros tipo json sen a extensión
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
# función que devolve verdadeiro ou falso dependendo de se a entrada está dentro
# das respostas positivas ou negativas válidas e verdadeiro ou falso para o tipo
# de resposta que deu nun principio si verdadeiro non falso
def snValido(resposta):
	sis = ('si', 's', 'yes', 'y')
	nons = ('non', 'no', 'n')

	if resposta in sis:
		# valido e resposta
		return True, True
	# non poñer nada conta como dicir non
	elif resposta in nons or resposta == '':
		return True, False
	else:
		return False, False
#------------------------------------------------------------------------------------------------
# función que dado un ano devolve verdadeiro u falso dependendo de se é un valor correcto
def anoValido(ano):
	if ano == '':
		return True
	# non facemos que sexa positivo tamén porque pode ser un libro de antes de cristo por exemplo
	elif ano.isdigit():
		return True
	else:
		return False
#------------------------------------------------------------------------------------------------
# función para ler o ficheiro de configuración e devolver as variables adecuadas
def read_config():
	fich = '../.config'
	# se o ficheiro xa existe
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
	# se non existe o que facemos e crealo cos valores por defecto postos na variable e recargar a operacion
	else:
		open(fich, 'w').write(texto_config)
		return read_config()
#------------------------------------------------------------------------------------------------
