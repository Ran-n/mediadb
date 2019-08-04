#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	21/07/2019 18:35:49
#+ Editado:	02/08/2019 15:02:01
#------------------------------------------------------------------------------------------------
import utils as u
from khronos import khronos as kh
from base36 import base36 as b36
# ----------------------------
import gettext
import sys
from functools import partial
#------------------------------------------------------------------------------------------------
# función que dados todos os valores dunha función devolve un elemento completo
def engadir(nome, tipo, epi, lugar, video, ano, anof, audio, subs, calidade, peso, xenero, creador):
	global __indice
	elto={}

	elto['nome'] = nome
	elto['epi'] = epi
	elto['tipo'] = tipo
	elto['lugar'] = lugar
	elto['video'] = video
	elto['ano'] = ano
	elto['ano_fin'] = anof
	elto['audio'] = audio
	elto['subs'] = subs
	elto['calidade'] = calidade
	elto['peso'] = peso
	elto['xenero'] = xenero
	elto['creador'] = creador

	# metemos o elemento con chave a data de metida en codigo 36
	__indice[b36.code(kh.getAgora())] = elto
#------------------------------------------------------------------------------------------------
# función que devolve verdadeiro ou falso dependendo de se o nome introducido é valido ou non
def nomeValido(nome):
	if nome == '':
		return False
	else:
		for valor in __indice.values():
			if nome == valor['nome']:
				return False
	return True
#------------------------------------------------------------------------------------------------
# función que devolve verdadeiro ou falso dependendo de se o tipo de contido introducido é valido ou non
def tipoValido(tipo):
	if tipo in __codes:
		tipo = __codes[tipo]
		return True, tipo
	elif tipo in __codes.values():
		return True, tipo
	else:
		return False, None
#------------------------------------------------------------------------------------------------
# función que indica se o idioma indicado por entrada está dentro da lista de idiomas na carpeta media
def idiomasValidos(array):
	# se nos pide axuda será sempre no primeiro, así evitamos comparacións no bucle for
	if array[0] == '.':
		u.pJson(__codsIdiomas, True)
		return False
	elif array[0] == '':
		return True
	else:
		# recorremos o array
		for obx in array:
			if obx not in __codsIdiomas:
				# se calquera dos obx non corresponde co código preciso devolve falso
				return False
	# se non sae por ningún dos outros lados e que esta todo ok
	return True
#------------------------------------------------------------------------------------------------
# función que se encarga de de interactuar co usuario para conseguir un nome
def dialogNome():
	while True:
		nome = input(_(' > Nome: ')).lower()
		if nomeValido(nome):
			break
	return nome
#------------------------------------------------------------------------------------------------
# dialogo para engadir episodios a unha serie
def dialogEpi():
	valido = False
	while True:
		epis = input(_(' > Números dos episodios separados por coma: ')).split(',')

		for ele in epis:
			if u.epi_valido(ele) == False:
				valido = False
				break
			else:
				valido = True

		if valido: break
	# se non o facemos así neste orde pois non mos ordea ben
	epis = list(set(epis))
	epis.sort()
	return epis
#------------------------------------------------------------------------------------------------
# función que se encarga de de interactuar co usuario para conseguir un tipo
def dialogTipo():
	while True:
		tipo = input(_(' > Tipo (serie, peli, docu, video, libro, musica): ')).lower()
		valido, tipo = tipoValido(tipo)
		if valido:
			break
	return tipo
#------------------------------------------------------------------------------------------------
# función que se encarga de de interactuar co usuario para conseguir un lugar
def dialogLugar():
	return input(_(' > Di onde está: ')).lower()
#------------------------------------------------------------------------------------------------
# función que se encarga de de interactuar co usuario para conseguir se ten video ou non
def dialogVideo():
	while True:
		valido, video = u.snValido(input(_(' > Ten video? (s/n): ')).lower())
		if valido:
			break
	return video
#------------------------------------------------------------------------------------------------
# función que se encarga de de interactuar co usuario para conseguir un ano de saida
def dialogAno():
	while True:
		ano = input(_(' > Ano de inicio: '))
		if u.anoValido(ano):
			break
	return ano
#------------------------------------------------------------------------------------------------
# función que se encarga de de interactuar co usuario para conseguir un ano de fin
def dialogAnoF():
	while True:
		anof = input(_(' > Ano de fin: '))
		if u.anoValido(anof):
			break
	return anof
#------------------------------------------------------------------------------------------------
# función que se encarga de de interactuar co usuario para conseguir os audios se os ten
def dialogAudio():
	while True:
		audio = input(_(' > Audios separados por coma (. para info): ')).split(',')
		if idiomasValidos(audio):
			break
	return audio
#------------------------------------------------------------------------------------------------
# función que se encarga de de interactuar co usuario para conseguir os subtítulos se os ten
def dialogSubs():
	while True:
		subs = input(_(' > Subtitulos separados por coma (. para info): ')).split(',')
		if idiomasValidos(subs):
			break
	return subs
#------------------------------------------------------------------------------------------------
# función que se encarga de de interactuar co usuario para conseguir as calidades se as ten
def dialogCalidade():
	return input(_(' > Calidades separados por coma: ')).split(',')
#------------------------------------------------------------------------------------------------
# función que se encarga de de interactuar co usuario para conseguir os pesos se os ten
def dialogPeso():
	return input(_(' > Pesos separados por coma: ')).split(',')
#------------------------------------------------------------------------------------------------
# función que se encarga de de interactuar co usuario para conseguir os xéneros se os ten
def dialogXenero():
	return input(_(' > Xéneros separados por coma: ')).split(',')
#------------------------------------------------------------------------------------------------
# función que se encarga de de interactuar co usuario para conseguir os creadores se os ten
def dialogCreador():
	return input(_(' > Creadores separados por coma: ')).split(',')
#------------------------------------------------------------------------------------------------
# función que se encarga de indicar a operación é chamar a tódolos diálogos para mandar o valor á función de engadir
def dialogEngadir():
	print('\n-----------------------')
	print(_('*> Pantalla de engadir:'))
	print('-----------------------')

	nome = dialogNome()
	tipo = dialogTipo()
	if tipo == 's':
		epi = dialogEpi()
	else:
		epi = 'NA'

	engadir(nome,  tipo, epi, dialogLugar(), dialogVideo(), dialogAno(), dialogAnoF(),
	dialogAudio(), dialogSubs(), dialogCalidade(), dialogPeso(), dialogXenero(), dialogCreador())
#------------------------------------------------------------------------------------------------
# función que colle e cambia un campo da variable que garda tódolos
def editar(chave, campo, valor):
	# é mellor editar directamente no array ca copiar e logo meter no array porque
	# da máis carga e acabase precisando o global igual
	global __indice
	__indice[chave][campo] = valor
#------------------------------------------------------------------------------------------------
# función que se encarga de axudar á interacción co usuario na edición dun elemento
def dialogEditarAux(chave):
	print(_('*> Dime que queres editar:, o que cala non otorga :'))
	if '?' == input(_('*> O que cala non otorga, para ver tódolos valores anteriores pulsa "?":')):
		u.pJson(__indice[chave])

	# nome
	while True:
		valido, edicion = u.snValido(input(_(' > Editar nome? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'nome', dialogNome())

	# tipo
	while True:
		valido, edicion = u.snValido(input(_(' > Editar tipo? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'tipo', dialogTipo())

	# só o mostramos se tratamos cunha serie
	if __indice[chave]['tipo'] == 's':
		# epi
		while True:
			valido, edicion = u.snValido(input(_(' > Editar episodios? (s/n): ')).lower())
			if valido: break
		if edicion:
			while True:
				opcion = input(_(' > Engadir(+), eliminar(-) ou substituir(*)?: '))
				if opcion == '+':
					suma = __indice[chave]['epi'] + dialogEpi()
					# se non se fai nesta orde erro
					suma = list(set(suma))
					suma.sort()
					editar(chave, 'epi', suma)
					break
				elif opcion == '-':
					u.pJson(__indice[chave]['epi'])
					eliminar = list(set(input(_(' > Episodios a eliminar separados por coma(,): ')).split(',')))
					for ele in eliminar:
						if ele in __indice[chave]['epi']:
							__indice[chave]['epi'].remove(ele)
					break
				elif opcion == '*':
					editar(chave, 'epi', dialogEpi())
					break

	# lugar
	while True:
		valido, edicion = u.snValido(input(_(' > Editar lugar? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'lugar', dialogLugar())

	# video
	while True:
		valido, edicion = u.snValido(input(_(' > Editar video? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'video', dialogVideo())

	# ano
	while True:
		valido, edicion = u.snValido(input(_(' > Editar ano de estrea? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'ano', dialogAno())

	# anof
	while True:
		valido, edicion = u.snValido(input(_(' > Editar ano fin? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'ano_fin', dialogAnoF())

	# audio
	while True:
		valido, edicion = u.snValido(input(_(' > Editar audio? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'audio', dialogAudio())

	# subs
	while True:
		valido, edicion = u.snValido(input(_(' > Editar subtítulos? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'subs', dialogSubs())

	# calidade
	while True:
		valido, edicion = u.snValido(input(_(' > Editar calidade? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'calidade', dialogCalidade())


	# peso
	while True:
		valido, edicion = u.snValido(input(_(' > Editar peso? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'peso', dialogPeso())

	# xenero
	while True:
		valido, edicion = u.snValido(input(_(' > Editar xenero? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'xenero', dialogXenero())

	# creador
	while True:
		valido, edicion = u.snValido(input(_(' > Editar creador? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'creador', dialogCreador())
#------------------------------------------------------------------------------------------------
# función que marca a operación de editar e vai chamando á función auxiliar de edición por cada
# elemento con ese nome
def dialogEditar():
	print('\n-----------------------')
	print(_('*> Pantalla de edición:'))
	print('-----------------------')
	#i# poñoo aqui e non na propia comparación porque senón tería que meter o valor
	## por cada elemento do diccionario
	nome = input(_('Nome da serie a editar: ')).lower()
	for chave, valor in __indice.items():
		if nome == valor['nome']:
			dialogEditarAux(chave)
#------------------------------------------------------------------------------------------------
def dialogBuscar():
	buscar_titulo(input(_('*> Título do elemento a buscar ou palabra clave: ')))
#------------------------------------------------------------------------------------------------
# operación que dado un string mostra as coincidencias da bd
def buscar_titulo(titulo):
	if titulo == '':
		for elto in __indice.values():
				print('---------------------------------------')
				print('> Resultados:')
				u.pJson(elto)
				print('---------------------------------------')
	else:
		for elto in __indice.values():
			if titulo in elto['nome']:
				print('---------------------------------------')
				print('> Resultados:')
				u.pJson(elto)
				print('---------------------------------------')
#------------------------------------------------------------------------------------------------
# función base que se encarga de mostrar o menú de opcións ao usuario e chamar á opción seleccionada
def menu(operacions):
	while True:
		print('\n-----------------------')
		print(_('*> Elixe a opción:'))
		print('-----------------------')
		print(_('0 - Sair (0. para non gardar)'))
		print(_('1 - Engadir'))
		print(_('2 - Editar'))
		print(_('3 - Buscar por título'))

		op = input(_('Opción: '))
		print('-----------------------')

		if op in operacions:
			return op
		else:
			print(_('Selecciona unha das posibles.\n'))

#------------------------------------------------------------------------------------------------
# función que se encarga de gardar todo en memoria e sair da execución
def sair():
	# garda o ficheiro co indice de tódolos elementos
	u.gardar_json(__config['ruta']+__config['nomeFich'], __indice, True)
	exit()
#------------------------------------------------------------------------------------------------
# función controladora do modo manual da ap
def manual():
	# diccionario con todas as opcións posibles
	ops = {'0.': exit,
			'0': sair,
			'1': dialogEngadir,
			'2': dialogEditar,
			'3': dialogBuscar
			}

	while True:
		ops[menu(ops)]()
#------------------------------------------------------------------------------------------------
# función controladora do modo automático da ap
def auto():
	print('auto')
#------------------------------------------------------------------------------------------------
# función que lee o ficheiro de configuración e devolve os valores
def config():
	return u.read_config()
#------------------------------------------------------------------------------------------------
# función main do programa e onde se fan as declaracións e toma de valores iniciais
if __name__=="__main__":
	## Declaracións ----------------------
	_ = gettext.gettext

	# nome do ficheiro e variable onde se gardarán todos os idiomas coas súas claves
	__fcodsIdiomas = '../media/codesIdiomas'
	__codsIdiomas = {}

	'''
	Grupos que serven para saber que responde unha persoa. Temos os sis e os
	nons, se calquer cousa do que responde non está dentro dos grupos non se
	acepta. Isto faise así en lugar de comparacións directas en previsión
	de poder ampliar para distintos idiomas.
	'''

	# variable de configuración
	__config = {
			# ruta na que se atopa o ficheiro indice e todo o que se cree da app pero non o código base
			'ruta': '../proba',
			# idioma por defecto da app
			'idioma': 'gl',
			# ficheiro onde, por defecto, se gardarán todas as pelis. Na config cambiarase
			'nomeFich': 'indice.json'
	}

	'''
	Códigos dados aos distintos tipos de ficheiros posibles.
	Server o doble propósito de comprobar que se responde algo dentro das claves
	ou valores das mesmas e sempre gardar no ficheiro as entradas co valor das claves
	para reducir o gasto de memoria.
	'''
	__codes = {'serie': 's',
				'peli': 'p',
				'docu': 'd',
				'video': 'v',
				'libro': 'l',
				'musica': 'm'}

	# variable onde se gardarán todas as pelis
	__indice = {}

	## Asignacións ----------------------
	# caragamos o idioma e a configuración do ficheiro de configuración
	__config = config()
	__config['ruta'] = __config['ruta']+'/'

	# unha vez temos a ruta podemos cargar o ficheiro cos datos
	__indice = u.cargar_json(__config['ruta']+__config['nomeFich'])

	# diccionario coas linguas aceptadas
	__codsIdiomas = u.cargar_json(__fcodsIdiomas)

	if len(sys.argv)>1:
		if sys.argv[1]=='-?':
			print('axuda')
		elif sys.argv[1]=='-h':
			print('axuda')
		elif len(sys.argv)>3:
			auto(sys.argv[1:])
		else:
			print("Dame máis argumentos ou separa os que xa tes")
	else:
		manual()
#------------------------------------------------------------------------------------------------
