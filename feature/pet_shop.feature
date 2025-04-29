#language: pt
#encoding: UTF8

@CriacaoCenario
Funcionalidade: Realizar todos o desafio 1 da trilha de API Python + Behave

Contexto: Realizar todos o desafio 1 da trilha de API Python + Behave
Dado que sera identificado os dados para o login na petshop

@prioridade1
Esquema do Cenário: Cadastrar um usuario
Quando enviado requisição com os dados <usuario>, <nome>, <sobrenome>, <email>, <senha>, <telefone>, <status> para cadastrar usuario
Exemplos:
| usuario          | nome    | sobrenome | email            | senha    | telefone        | status|
| pamela.bieger    | Pamela  | Bieger    | pamela@gmail.com | 123456   | 51985765342     |   0   |
Então usuario sera cadastrado com sucesso

@prioridade1
Esquema do Cenário: Verificar o cadastro de usuario
Quando enviado requisição com os dados <usuario> para consultar usuario
Exemplos:
| usuario          |
| pamela.bieger    |
Então usuario sera validado com sucesso

@prioridade1
Esquema do Cenário: Atualizar o cadastro de usuario
Dado que eu tenha os dados <usuario> para consultar
Quando enviado requisição com os dados  <usuario>, <nome>, <sobrenome>,  <email>, <senha>, <telefone>, <status> para atualizar usuario
Exemplos:
| usuario          | nome    | sobrenome | email             | senha   | telefone    | status|
| pamela.bieger    | Pamela  | Bieger    |  pamela@gmail.com | 12      | 51985765342 |   0   |
Então usuario sera atualizado com sucesso

@prioridade1
Esquema do Cenário: Deletar um usuario
Quando enviado requisição com os dados <usuario> para deletar usuario
Exemplos:
| usuario          |
| pamela.bieger    |
Então usuario sera deletado com sucesso