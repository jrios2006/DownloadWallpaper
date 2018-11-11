#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wallpaper-limpieza.py
#  
#  
import glob
import os

def BorrarFichero(archivo):
	'''
	Borrro el archivo
	'''
	import os
	Aux = os.remove(archivo)
	return Aux

def main(args):
	Ruta = '/Fotos/wallpaperswide/'
	'''
	ListadeFicheros = os.listdir(path=Ruta)
	NumeroFicheros = len(ListadeFicheros)
	print(NumeroFicheros)
	'''
	TotalFicheros = 500
	# Filtramos los ficheros jpg
	files = filter(os.path.isfile, glob.glob(Ruta + "*.jpg"))
	ListaOrdenada=sorted(
				files, key=lambda x: os.path.getmtime(x)
						) # Primero los ficheros mas viejos	
	NroFicheros = len(ListaOrdenada)
	if (NroFicheros > TotalFicheros):
		print('Tengo que borrar los más ficheros viejos')
		i = TotalFicheros
		j = 0
		while (i<=NroFicheros):
			print('Borro el fichero ' + str(j) + ' más viejo: ' + ListaOrdenada[j])
			BorrarFichero(ListaOrdenada[j])
			i = i + 1
			j = j + 1
	else:
		print('NO hago nada no hay muchos ficheros (' + str(NroFicheros)+')')
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
