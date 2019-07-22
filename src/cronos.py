#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	20/07/2019 12:38:02
#+ Editado:	20/07/2019 13:16:18
#------------------------------------------------------------------------------------------------
from datetime import datetime as dt
#------------------------------------------------------------------------------------------------
def getAgora():
	tempo = dt.now()
	ano = str(tempo.year)
	# axustámolo aos 5 díxitos que usamos no formateo
	ano = '0'+ano if len(ano) < 5 else ano

	mes = str(tempo.month)
	# igual ca ano formatamos o mes
	mes = '0'+mes if len(mes) < 2 else mes
	
	dia = str(tempo.day)
	# mesmo rollete
	dia = '0'+dia if len(dia) < 2 else dia
	
	hora = str(tempo.hour)
	# mesmo rollete
	hora = '0'+hora if len(hora) < 2 else hora
	
	minuto = str(tempo.minute)
	# mesmo rollete
	minuto = '0'+minuto if len(minuto) < 2 else minuto
	
	segundo = str(tempo.second)
	# mesmo rollete
	segundo = '0'+segundo if len(segundo) < 2 else segundo
	
	microsegundo = str(tempo.microsecond)[:2]

	return '1'+ano+mes+dia+hora+minuto+segundo+microsegundo
#------------------------------------------------------------------------------------------------
