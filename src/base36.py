#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	19/07/2019 23:31:19
#+ Editado:	20/07/2019 13:18:04
#------------------------------------------------------------------------------------------------
import sys
#------------------------------------------------------------------------------------------------
def code(integer):
	chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	integer = int(integer)

	sign = '-' if integer < 0 else ''
	integer = abs(integer)
	result = ''

	while integer > 0:
		integer, remainder = divmod(integer, 36)
		result = chars[remainder]+result

	return sign+result
#------------------------------------------------------------------------------------------------
def decode(number):
	return int(number, 36)
#------------------------------------------------------------------------------------------------