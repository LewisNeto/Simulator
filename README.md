# Simulador #

Este simulador tem como objetivo analisar o tempo médio que um cliente gasta no sistema de atendimento em uma loja de departamentos:

## O problema ##

Em uma central de financiamento de uma loja de departamentos, o tempo entre chegadas sucessivas de clientes é normalmente distribuído com média de cinco minutos e desvio-padrão de 2,2 minutos. Existem três atendentes que realizam a pré-análise. O tempo de pré-análise é exponencialmente distribuído com média de oito minutos. Enquanto a atendente está realizando a pré-análise do cliente, ela não pode atender a outro cliente.

Os clientes que chegam quando todas as atendentes estão ocupadas aguardam em fila única. Após a pré-análise, 70% dos clientes são encaminhados ao gerente, que finaliza o processo de financiamento. Os outros 30% não têm financiamento aceito. O gerente leva 2,5 minutos, na maior parte das vezes, para atender aos clientes, segundo uma distribuição triangular em que o menor valor é de 0,5 minutos e o maior valor é de cinco minutos. A central funciona diariamente das 10h30 às 22h. A loja pretende estudar o tempo médio que um cliente gasta no sistema. (Livro: Modelagem e Simulação de Eventos discretos, IV Edição. p.122 )

## Informações para operação ##

A duração da simulação é determinada pela duração do período de operação do próprio sistema real.
O número de replicação depende do grau de confiança com que desejamos trabalhar.
A análise de dados de sistemas terminais pode ser dividida em 7 etapas:
- Estabelecer as medidas de desempenho;
	- Tempo médio que um pedido aceito permanece no sistema;
- Escolher a confiança estatísticas e a precisão com que se pretende trabalhar;
	- Confiança de 95% (a=0.05) e uma precisão tal que h* seja de no máximo 0.5 minuto.
- Definir, a partir da observação do sistema real, o tempo de simulação;
	![ACD do exemplo de sistema terminal](https://raw.githubusercontent.com/leolima/Simulator/master/imagens/ACD-do-exemplo.jpg)
- Construir a "amostra piloto";
	- Obtemos a "amostra piloto" ao rodar o modelo com poucas replicações (10);
- Determinar o número de replicações necessárias;
	- i) Através da amostra piloto podemos construir um intervalo de confiança para a média obtida. Com (a=0.05 e n=10) temos da tabela da distribuição de t de Student:
	
- Rodar o modelo novamente;
- Calcular o novo intervalo de confiança;

# LISTA À FAZER #

1 . Pseudo código em portugol

# Requerimentos #

[Python 2.7.12](https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi) 
[Numpy 1.11.1 x86 python 2.7](http://www.lfd.uci.edu/~gohlke/pythonlibs/dp2ng7en/numpy-1.11.1+mkl-cp27-cp27m-win32.whl)
[Scipy 0.18.0 x86 python 2.7](http://www.lfd.uci.edu/~gohlke/pythonlibs/dp2ng7en/scipy-0.18.0-cp27-cp27m-win32.whl)