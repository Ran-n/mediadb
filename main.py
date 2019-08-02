#! /usr/bin/python3
#+ Autor:	Ran#
#+ Creado:	02/08/2019 14:21:04
#+ Editado:	02/08/2019 15:01:49
## do ficheiro mediadb.py
#------------------------------------------------------------------------------------------------
import os
import subprocess
import sys
#------------------------------------------------------------------------------------------------
# cambiamos ao subdirectorio
os.chdir('src')
valores = sys.argv[1:]
valores.insert(0,'mediadb.py')
valores.insert(0,'python3')
# facemos a chamada á función
subprocess.call(valores)
#------------------------------------------------------------------------------------------------
