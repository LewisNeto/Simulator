# Simulador #

Este simulador tem como objetivo analisar o tempo médio que um cliente gasta no sistema de atendimento em uma loja de departamentos:

## O problema ##

Em uma central de financiamento de uma loja de departamentos, o tempo entre chegadas sucessivas de clientes é normalmente distribuído com média de cinco minutos e desvio-padrão de 2,2 minutos. Existem três atendentes que realizam a pré-análise. O tempo de pré-análise é exponencialmente distribuído com média de oito minutos. Enquanto a atendente está realizando a pré-análise do cliente, ela não pode atender a outro cliente.

Os clientes que chegam quando todas as atendentes estão ocupadas aguardam em fila única. Após a pré-análise, 70% dos clientes são encaminhados ao gerente, que finaliza o processo de financiamento. Os outros 30% não têm financiamento aceito. O gerente leva 2,5 minutos, na maior parte das vezes, para atender aos clientes, segundo uma distribuição triangular em que o menor valor é de 0,5 minutos e o maior valor é de cinco minutos. A central funciona diariamente das 10h30 às 22h. A loja pretende estudar o tempo médio que um cliente gasta no sistema.