#language: pt
#encoding: UTF8

@CriacaoCenario
Funcionalidade: Realizar todos o desafio 1 da trilha de API Python + Behave

Contexto: Realizar todos o desafio 1 da trilha de API Python + Behave
Dado que sera identificado os dados para a criacao de usuario

@prioridade1
Esquema do Cenário: Cadastrar um usuario
Quando enviado requisição com os dados necessários <usuario>, <nome>, <sobrenome>, <email>, <senha>, <telefone>, <status> para cadastrar um usuario
Exemplos:
| usuario          | nome    | sobrenome   | email            | senha  | telefone        | status|
| amanda.mendes    | Amanda  | Mendes      | amanda@gmail.com | 1234   | 51985765342     |   0   |
Então o usuario sera cadastrado com sucesso

@prioridade1
Esquema do Cenário: Verificar o cadastro de usuario
Quando enviado requisição com os dados necessários <usuario> para consultar um usuario
Exemplos:
| usuario          |
| amanda.mendes    |
Então o usuario sera validado com sucesso

@prioridade1
Esquema do Cenário: Atualizar o cadastro de usuario
Quando enviado requisição com os dados necessários <usuario>, <nome>, <sobrenome>, <email>, <senha>, <telefone>, <status> para atualizar o usuario
Exemplos:
| usuario          | nome  | sobrenome | email | senha       | telefone  | status  |
| amanda.mendes    | null  | null      | null  | amanda123   | null      |  null   |
Então o usuario sera atualizado com sucesso

 @prioridade1
Esquema do Cenário: Deletar um usuario
Quando enviado requisição com os dados necessários <usuario> para deletar o usuario
Exemplos:
| usuario          |
| amanda.mendes    |
Então o usuario sera deletado com sucesso