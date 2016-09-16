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
- Determinar o número de replicações necessárias;
- Rodar o modelo novamente;
- Calcular o novo intervalo de confianaça;



