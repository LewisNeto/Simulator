#@autor: Leonardo Costa
#@autor: Marcelo Araujo
#@autor: Luis Santos

import random
import numpy
import math
import matplotlib.pyplot as plt

		
class Cliente(object):
	def __init__(self,tempo):
		self.tempoChegada = tempo
		
	def tempoPreAnalise():
		self.tempoPre = self.tempoChegada + random.expovariate(1.0/8.0)
		
	def tempoAnalise():
		self.tempoPre = numpy.random.triangular(0.5, 2.5, 5, size=None)
		
		
class Gerente(object):
	def __init__(self,tempo):
		self.ocupado = False
		
	def analisando(self, client):
		self.clienteSendoAnalisado = client

class Atendente(object):
	def __init__(self):
		self.ocupada = False
	
	def preAnalisando(self,client):
		self.ocupada = True
		self.clienteSendoPreAnalisado = client
		
	def terminouDeAtender(self):
		self.ocupada = False
		self.clienteSendoPreAnalisado = None
		

def executa(replicacao):
	numReplicacao = int(replicacao)
	medias = range(numReplicacao)
	
	
	for i in xrange(0,numReplicacao):
		tempo = 0
		media = 5.0
		desvio_padrao = 2.2
		tempoCadaChegada = numpy.random.normal(media, desvio_padrao, 1)
		
		atendentes = iniciaAtendentes(3)
		gerente = Gerente()
		
		filaPreAnalise = iniciaFilaClientes(690,tempoCadaChegada)
		filaAnalise = []
		
		#inicialmente a timeline tem o tempo de chegada de todos clientes
		timeLine = iniciaTimeLine(filaPreAnalise)
		
		print "i :% ; tempo %",i,tempoCadaChegada
		
		#enquanto proximo item da timeline nao for maior ou igual a 690
		while (timeLine[0] < 690):
			
			#Se tiver gente na fila de preanalise, atendente desocupada
			if(len(filaPreAnalise) > 0 and existeDesocupado(atendentes)):
				atendente = primeiraDesocupada(atendentes)
				cliente = filaPreAnalise.pop(0)
				cliente.tempoPreAnalise()
				atendente.preAnalisando(cliente)
				timeLine = adicionaEvento(timeLine,cliente.tempoPre)
				
			#Se tiver cliente sendo preanalisado
			if(clienteSendoPreAnalisado(atendentes)):
				for i in xrange(len(atendentes)):
					if( atendentes[i].clienteSendoPreAnalisado.tempoPre == timeLine[0] ):
						filaAnalise.append(atendentes[i].clienteSendoPreAnalisado)
						atendentes[i].terminouDeAtender()
			
			#Se tiver fila de cliente pro gerente analisar e ele estiver desocupado
			if(len(filaAnalise)> 0 and gerente.ocupado == False):
				cliente = filaAnalise.pop(0)
				gerente.clienteSendoAnalisado(cliente)
				
			
			tempo+=1
	
	return "aaa"
	
def iniciaTimeLine(filaPreAnalise):
	timeLine=[]
	for i in xrange(len(filaPreAnalise)):
		timeLine.append(filaPreAnalise[i].tempoChegada)

def adicionaEvento(timeline,tempoPreAnalise):
	timeline.append(tempoPreAnalise)
	timeline.sort()
	return timeline
	
def organizaCrescente(array,atributo):
	return sorted(array, key=lambda elem:elem.atributo)

def iniciaFilaClientes(tempo,tempoCadaChegada):
	qtClientes = int (tempo/tempoCadaChegada)
	listaClientes = []
	for i in xrange(qtClientes):
		listaClientes.append(Cliente(i*tempoCadaChegada))
	return listaClientes
		
def iniciaAtendentes(numAtendentes):
	listaAtendentes = []
	for i in xrange(numAtendentes):
		listaAtendentes.append(Atendente())
	return listaAtendentes

def existeDesocupado(listaAtendentes):
	for i in listaAtendentes:
		if (i.ocupada == False):
			return True
	return False
	
def clienteSendoPreAnalisado(listaAtendentes):
	for i in listaAtendentes:
		if (i.ocupada == True):
			return True
	return False

def primeiraDesocupada(listaAtendentes):
	for i in xrange(len(listaAtendentes)):
		if (listaAtendentes[i].ocupada == False):
			return listaAtendentes[i];
	return None
	
numReplicacao = 10
desvio = executa(numReplicacao)