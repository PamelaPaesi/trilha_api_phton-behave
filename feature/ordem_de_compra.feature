# language: pt
Funcionalidade: Efetuar ordem de compra

Esquema do Cenário: Efetuar uma ordem de compra na petstore
Dado que o usuário selecionou o animal com o id correspondente a "<id>" desejado na petstore
Então o sistema valida se a ordem de pedido foi armazenada corretamente
Exemplos: Dados
| id |
| 1  |
| 2  |
| 3  |
| 4  |