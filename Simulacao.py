#@autor: Leonardo Costa
#@autor: Marcelo Araujo
#@autor: Luis Santos

import random
import numpy
import math
import matplotlib.pyplot as plt


class Atendente(object):
	def __init__(self):
		self.ocupada = False
	
	def calculaTempoAtendimento(self):
		print('Se ferrou, 10 minutos')
		

a = Atendente()

print(a.calculaTempoAtendimento())