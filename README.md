# Simulador #

Este simulador tem como objetivo analisar o tempo m�dio que um cliente gasta no sistema de atendimento em uma loja de departamentos:

## O problema ##

Em uma central de financiamento de uma loja de departamentos, o tempo entre chegadas sucessivas de clientes � normalmente distribu�do com m�dia de cinco minutos e desvio-padr�o de 2,2 minutos. Existem tr�s atendentes que realizam a pr�-an�lise. O tempo de pr�-an�lise � exponencialmente distribu�do com m�dia de oito minutos. Enquanto a atendente est� realizando a pr�-an�lise do cliente, ela n�o pode atender a outro cliente.

Os clientes que chegam quando todas as atendentes est�o ocupadas aguardam em fila �nica. Ap�s a pr�-an�lise, 70% dos clientes s�o encaminhados ao gerente, que finaliza o processo de financiamento. Os outros 30% n�o t�m financiamento aceito. O gerente leva 2,5 minutos, na maior parte das vezes, para atender aos clientes, segundo uma distribui��o triangular em que o menor valor � de 0,5 minutos e o maior valor � de cinco minutos. A central funciona diariamente das 10h30 �s 22h. A loja pretende estudar o tempo m�dio que um cliente gasta no sistema. (Livro: Modelagem e Simula��o de Eventos discretos, IV Edi��o. p.122 )

## Informa��es para opera��o ##

A dura��o da simula��o � determinada pela dura��o do per�odo de opera��o do pr�prio sistema real.
O n�mero de replica��o depende do grau de confian�a com que desejamos trabalhar.
A an�lise de dados de sistemas terminais pode ser dividida em 7 etapas:
- Estabelecer as medidas de desempenho;
	- Tempo m�dio que um pedido aceito permanece no sistema;
- Escolher a confian�a estat�sticas e a precis�o com que se pretende trabalhar;
	- Confian�a de 95% (a=0.05) e uma precis�o tal que h* seja de no m�ximo 0.5 minuto.
- Definir, a partir da observa��o do sistema real, o tempo de simula��o;
	![ACD do exemplo de sistema terminal](https://raw.githubusercontent.com/leolima/Simulator/master/imagens/ACD-do-exemplo.jpg)
- Construir a "amostra piloto";
	- Obtemos a "amostra piloto" ao rodar o modelo com poucas replica��es (10);
	![Amostra piloto](https://raw.githubusercontent.com/leolima/Simulator/master/imagens/tabela-amostra.jpg)
- Determinar o n�mero de replica��es necess�rias;
	- i) Atrav�s da amostra piloto podemos construir um intervalo de confian�a para a m�dia obtida. Com (a=0.05 e n=10) temos da tabela da distribui��o de t de Student:
	
	![Resultado da tabela T de Student](https://raw.githubusercontent.com/leolima/Simulator/master/imagens/res-t-student.jpg)
	- ii) O tamanho da metade do intervalo fica:
	
	![Precis�o](https://raw.githubusercontent.com/leolima/Simulator/master/imagens/precisao.jpg)
	- iii) O valor obtido � maior que a precis�o definida 0.5 minuto. A partir deste podemos construir o seguinte intervalo de confian�a para a m�dia:
	
	![Intervalo de precis�o](https://raw.githubusercontent.com/leolima/Simulator/master/imagens/intervalo-confianca.jpg)
	- Se o valor obtido for maior que a precis�o desejada, devemos aumentar o n�mero de replica��es, com a express�o:
	
	![Intervalo de precis�o](https://raw.githubusercontent.com/leolima/Simulator/master/imagens/numero-de-replicacoes.jpg)
- Rodar o modelo novamente com o n�mero de replica��es encontrado;
- Calcular o novo intervalo de confian�a, precis�o e etc...;

# LISTA A FAZER #

1 . Pseudo c�digo em portugol

# Requerimentos #

[Python 2.7.12](https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi) 

[Numpy 1.11.1 x86 python 2.7](http://www.lfd.uci.edu/~gohlke/pythonlibs/dp2ng7en/numpy-1.11.1+mkl-cp27-cp27m-win32.whl)

[Scipy 0.18.0 x86 python 2.7](http://www.lfd.uci.edu/~gohlke/pythonlibs/dp2ng7en/scipy-0.18.0-cp27-cp27m-win32.whl)

upgrade pip:

	python -m pip install --upgrade pip
	
instale a numpy
	
	pip install numpy-1.11.1+mkl-cp27-cp27m-win32.whl
	
instale a scipy
	
	pip install scipy-0.18.0-cp27-cp27m-win32.whl
	
instale a matplot
	
	python -m pip install -U pip setuptools
	
	python -m pip install matplotlib
