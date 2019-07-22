#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	21/07/2019 18:35:49
#+ Editado:	21/07/2019 18:35:49
#------------------------------------------------------------------------------------------------
import utils as u
import base36 as b36
import cronos as c
import gettext
import sys
from functools import partial
#------------------------------------------------------------------------------------------------
def engadir(nome, tipo, lugar, video, ano, anof, audio, subs, calidade, peso, xenero, creador):
	global __indice
	elto={}

	elto['nome'] = nome
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
	__indice[b36.code(c.getAgora())] = elto
#------------------------------------------------------------------------------------------------
def nomeValido(nome):
	if nome == '':
		return False
	else:
		for valor in __indice.values():
			if nome == valor['nome']:
				return False
	return True
#------------------------------------------------------------------------------------------------
def tipoValido(tipo):
	if tipo in __codes:
		tipo = __codes[tipo]
		return True, tipo
	elif tipo in __codes.values():
		return True, tipo
	else:
		return False, None

#------------------------------------------------------------------------------------------------
def snValido(resposta):
	if resposta in __sis:
		# valido e resposta
		return True, True
	# non poñer nada conta como dicir non
	elif resposta in __nons or resposta == '':
		return True, False
	else:
		return False, False
#------------------------------------------------------------------------------------------------
def anoValido(ano):
	if ano == '':
		return True
	elif ano.isdigit():
		return True
	else:
		return False
#------------------------------------------------------------------------------------------------
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
def dialogNome():
	while True:
		nome = input(_(' > Nome: ')).lower()
		if nomeValido(nome):
			break
	return nome
#------------------------------------------------------------------------------------------------
def dialogTipo():
	while True:
		tipo = input(_(' > Tipo (serie, peli, docu, video, libro): ')).lower()
		valido, tipo = tipoValido(tipo)
		if valido:
			break
	return tipo
#------------------------------------------------------------------------------------------------
def dialogLugar():
	return input(_(' > Di onde está: ')).lower()
#------------------------------------------------------------------------------------------------
def dialogVideo():
	while True:
		valido, video = snValido(input(_(' > Ten video? (s/n): ')).lower())
		if valido:
			break
	return video
#------------------------------------------------------------------------------------------------
def dialogAno():
	while True:
		ano = input(_(' > Ano de inicio: '))
		if anoValido(ano):
			break
	return ano
#------------------------------------------------------------------------------------------------
def dialogAnoF():
	while True:
		anof = input(_(' > Ano de fin: '))
		if anoValido(anof):
			break
	return anof
#------------------------------------------------------------------------------------------------
def dialogAudio():
	while True:
		audio = input(_(' > Audios separados por coma (. para info): ')).split(',')
		if idiomasValidos(audio):
			break
	return audio
#------------------------------------------------------------------------------------------------
def dialogSubs():
	while True:
		subs = input(_(' > Subtitulos separados por coma (. para info): ')).split(',')
		if idiomasValidos(subs):
			break
	return subs
#------------------------------------------------------------------------------------------------
def dialogCalidade():
	return input(_(' > Calidades separados por coma: ')).split(',')
#------------------------------------------------------------------------------------------------
def dialogPeso():
	return input(_(' > Pesos separados por coma: ')).split(',')
#------------------------------------------------------------------------------------------------
def dialogXenero():
	return input(_(' > Xéneros separados por coma: ')).split(',')
#------------------------------------------------------------------------------------------------
def dialogCreador():
	return input(_(' > Creadores separados por coma: ')).split(',')
#------------------------------------------------------------------------------------------------
def dialogEngadir():
	print('\n-----------------------')
	print(_('*> Pantalla de engadir:'))
	print('-----------------------')

	engadir(dialogNome(), dialogTipo(), dialogLugar(), dialogVideo(), dialogAno(), dialogAnoF(),
	dialogAudio(), dialogSubs(), dialogCalidade(), dialogPeso(), dialogXenero(), dialogCreador())
#------------------------------------------------------------------------------------------------
def editar(chave, campo, valor):
	# é mellor editar directamente no array ca copiar e logo meter no array porque
	# da máis carga e acabase precisando o global igual
	global __indice

	__indice[chave][campo] = valor
#------------------------------------------------------------------------------------------------
def dialogEditarAux(chave):
	print(_('*> Dime que queres editar, o que cala non otorga:'))

	# nome
	while True:
		valido, edicion = snValido(input(_(' > Editar nome? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		#global __indice
		#__indice[chave]['nome'] = dialogNome()
		editar(chave, 'nome', dialogNome())

	# tipo
	while True:
		valido, edicion = snValido(input(_(' > Editar tipo? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'tipo', dialogTipo())

	# lugar
	while True:
		valido, edicion = snValido(input(_(' > Editar lugar? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'lugar', dialogLugar())

	# video
	while True:
		valido, edicion = snValido(input(_(' > Editar video? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'video', dialogVideo())

	# ano
	while True:
		valido, edicion = snValido(input(_(' > Editar ano de estrea? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'ano', dialogAno())

	# anof
	while True:
		valido, edicion = snValido(input(_(' > Editar ano fin? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'ano_fin', dialogAnoF())

	# audio
	while True:
		valido, edicion = snValido(input(_(' > Editar audio? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'audio', dialogAudio())

	# subs
	while True:
		valido, edicion = snValido(input(_(' > Editar subtítulos? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'subs', dialogSubs())

	# calidade
	while True:
		valido, edicion = snValido(input(_(' > Editar calidade? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'calidade', dialogCalidade())

	# peso
	while True:
		valido, edicion = snValido(input(_(' > Editar peso? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'peso', dialogPeso())

	# xenero
	while True:
		valido, edicion = snValido(input(_(' > Editar xenero? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'xenero', dialogXenero())

	# creador
	while True:
		valido, edicion = snValido(input(_(' > Editar creador? (s/n): ')).lower())
		if valido:
			break
	if edicion:
		editar(chave, 'creador', dialogCreador())
#------------------------------------------------------------------------------------------------
def dialogEditar():
	print('\n-----------------------')
	print(_('*> Pantalla de edición:'))
	print('-----------------------')
	nome = input(_('Nome da serie a editar: ')).lower()
	for chave, valor in __indice.items():
		if nome == valor['nome']:
			dialogEditarAux(chave)
#------------------------------------------------------------------------------------------------
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
			break
		else:
			print(_('Selecciona unha das posibles.\n'))

	return op
#------------------------------------------------------------------------------------------------
# función que se encarga de gardar todo en memoria e sair da execución
def sair():
	u.gardar_json(__ruta+__findice, __indice, True)
	exit()
#------------------------------------------------------------------------------------------------
# función controladora do modo manual da ap
def manual():
	ops = {'0.': exit,
			'0': sair,
			'1': dialogEngadir,
			'2': dialogEditar
			}

	while True:
		ops[menu(ops)]()
#------------------------------------------------------------------------------------------------
# función controladora do modo automático da ap
def auto():
	print('auto')
#------------------------------------------------------------------------------------------------
def config():
	raiz = '../'
	config = u.read_config()

	for index, value in enumerate(config):
		if value != '':
			if index==0:
				raiz=value+'/'
			if index==1:
				lang=value
		else:
			print('a')

	return str(raiz), str(lang)
#------------------------------------------------------------------------------------------------
if __name__=="__main__":
	_ = gettext.gettext

	# ruta na que se atopa o ficheiro indice e todo o que se cree da app pero non o código base
	__ruta = '../proba'
	# idioma por defecto da app
	__idioma = 'gl'

	# ficheiro e variable onde se gardarán todas as pelis
	__findice = 'indice.json'
	__indice = {}

	# nome do ficheiro e variable onde se gardarán todos os idiomas coas súas claves
	__fcodsIdiomas = 'media/codesIdiomas'
	__codsIdiomas = {}

	__codes = {'serie': 's',
				'peli': 'p',
				'docu': 'd',
				'video': 'v',
				'libro': 'l'}

	__sis = ('si', 's', 'yes', 'y')
	__nons = ('non', 'no', 'n')

	# caragamos o idioma e a configuración do ficheiro de configuración
	__ruta, __idioma = config()

	# unha vez temos a ruta podemos cargar o ficheiro cos datos
	__indice = u.cargar_json(__ruta+__findice)

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
