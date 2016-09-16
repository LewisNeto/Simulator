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
- Determinar o n�mero de replica��es necess�rias;
- Rodar o modelo novamente;
- Calcular o novo intervalo de confiana�a;



