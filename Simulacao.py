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
		self.tempoInicioPre = 0
		self.tempoPre = 0
		self.tempoFinalPre = 0
		self.tempoInicioAnalise = 0
		self.tempoDeAnalise = 0
		self.tempoFinalAnalise = 0
		
	def mostra(self):
		print ("tempoChegada: ",self.tempoChegada)
		print ("tempoInicioPre: ",self.tempoInicioPre)
		print (" tempoFinalPre: ",self.tempoFinalPre)
		print ("tempoInicioAnalise: ",self.tempoInicioAnalise)
		print ("tempoFinalAnalise: ",self.tempoFinalAnalise)
		print ("---------------")
		
	def tempoPreAnalise(self):
		self.tempoPre = random.expovariate(1.0/8.0)
		self.tempoFinalPre = self.tempoInicioPre + self.tempoPre
		
	def tempoAnalise(self):
		self.tempoDeAnalise = numpy.random.triangular(0.5, 2.5, 5, size=None)
		self.tempoFinalAnalise = self.tempoInicioAnalise + self.tempoDeAnalise
		
	def tempoInicioPre(self,tempo):
		self.tempoInicioPre = tempo
		
		
class Gerente(object):
	def __init__(self):
		self.ocupado = False
		self.clienteSendoAnalisado = None
		
	def analisando(self, client):
		self.ocupado = True
		self.clienteSendoAnalisado = client
		
	def terminouAtendimento(self):
		self.ocupada = False
		self.clienteSendoAnalisado = None

class Atendente(object):
	def __init__(self):
		self.ocupada = False
		self.clienteSendoPreAnalisado = None
	
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
		listaAnalisados = []
				
		print "i :% ; tempo %",i,tempoCadaChegada
		#for i in xrange(len(filaPreAnalise)):
		#	print "tempo:",filaPreAnalise[i].tempoChegada
		
		#enquanto proximo item da timeline nao for maior ou igual a 690
		while (tempo < 690):
		
			#Se tiver gente na fila de preanalise, atendente desocupada
			if(len(filaPreAnalise) > 0 and existeDesocupado(atendentes)):
				if(filaPreAnalise[0].tempoChegada < tempo):
					filaPreAnalise[0].tempoInicioPre = tempo
					atendente = primeiraDesocupada(atendentes)
					cliente = filaPreAnalise.pop(0)
					cliente.tempoPreAnalise()
					atendente.preAnalisando(cliente)
				
			#Se tiver cliente sendo preanalisado
			if(clienteSendoPreAnalisado(atendentes)):
				for i in xrange(len(atendentes)):
					if (atendentes[i].ocupada== True and atendentes[i].clienteSendoPreAnalisado.tempoFinalPre < tempo):
						filaAnalise.append(atendentes[i].clienteSendoPreAnalisado)
						atendentes[i].terminouDeAtender()
			
			#Se tiver fila de cliente pro gerente analisar e ele estiver desocupado
			if(len(filaAnalise)> 0 and gerente.ocupado == False):
				if(filaAnalise[0].tempoFinalPre < tempo):
					filaAnalise[0].tempoInicioAnalise = tempo
					cliente = filaAnalise.pop(0)
					cliente.tempoAnalise()
					cliente.mostra()
					gerente.analisando(cliente)
				
			#Se gerente tiver atendendo
			if(gerente.ocupado == True):
				print "entrou"
				if(gerente.clienteSendoAnalisado.tempoFinalAnalise < tempo):
					listaAnalisados.append(gerente.clienteSendoAnalisado)
					gerente.terminouAtendimento()
				
				
			tempo = tempo + 0.1
		
		print listaAnalisados
		
	return "aaa"
	
	
def organizaCrescente(array,atributo):
	return sorted(array, key=lambda elem:elem.atributo)

def iniciaFilaClientes(tempo,tempoCadaChegada):
	qtClientes = int (tempo/tempoCadaChegada)
	listaClientes = []
	for i in xrange(qtClientes):
		listaClientes.append(Cliente((i+1)*tempoCadaChegada))
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