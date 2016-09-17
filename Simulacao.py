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
		


def executa(replicacao):
	numReplicacao = int(replicacao)
	medias = range(numReplicacao)
	
	
	
	
	for i in xrange(0,numReplicacao):
		
		media = 5.0
		desvio_padrao = 2.2
		tempo = numpy.random.normal(media, desvio_padrao, 1)
		print "i :% ; tempo %",i,tempo
		
		#while (tempo < 690):
			
	
	return "aaa"

numReplicacao = 10
desvio = executa(numReplicacao)