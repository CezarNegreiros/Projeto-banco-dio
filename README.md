# Projeto-banco-dio

## Descrição do projeto

- O projeto tem como objetivo permitir que o usuário realize 3 operações básicas dentro de uma conta bancária.
- O usuário poderá realizar:
  - Depósito: Podendo adicionar qualquer valor, contanto que este seja positivo.
  - Saque: Podendo sacar valores menores ou iguais a R$ 500.00 e com um limite de 3 saques por dia. Além de que só pode sacar valores inferiores ou iguais ao total da conta.
  - Consulta do Extrato: Podendo visualizar o valor total depositado, o valor total sacado e o saldo total restante na conta.
 
## Recursos utilizados

- A lógica base do projeto foi feito com um laço while que verifica se o usuário selecionou uma opção diferente de *Q* (Quit/Sair).
- Caso o usuário digite um valor diferente de *Q*, é verificado se ele digitou um valor válido *D, E ou S*.
- Após isso, é verificado o valor da respectiva operação que o usuário deseja fazer.
  
