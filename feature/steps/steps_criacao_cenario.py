from behave import *
from feature.impl.criacao_cenario import Criacaocenario


@given("que sera identificado os dados para a criacao de usuario")
def step_impl(context):
    context.criacaocenario = Criacaocenario()


@when("enviado requisição com os dados necessários {usuario}, {nome}, {sobrenome}, {email}, {senha}, {telefone}, {status} para cadastrar um usuario")
def step_impl(context, usuario, nome, sobrenome, email, senha, telefone, status):
    context.criacaocenario.post_criar_usuario(usuario, nome, sobrenome, email, senha, telefone, status)

@when("enviado requisição com os dados necessários {usuario} para consultar um usuario")
def step_impl(context, usuario):
    context.criacaocenario.get_retona_usuario(usuario)

@when("enviado requisição com os dados necessários {usuario}, {nome}, {sobrenome}, {email}, {senha}, {telefone}, {status} para atualizar o usuario")
def step_impl(context, usuario, nome, sobrenome, email, senha, telefone, status):
    context.criacaocenario.put_atualiza_usuario(usuario, nome, sobrenome, email, senha, telefone, status)

@when("enviado requisição com os dados necessários {usuario} para deletar o usuario")
def step_impl(context, usuario):
    context.criacaocenario.delete_usuario(usuario)

@then("o usuario sera cadastrado com sucesso")
def step_impl(context):
    context.criacaocenario.retorno_usuario()

@then("o usuario sera validado com sucesso")
def step_impl(context):
    context.criacaocenario.valida_usuario()

@then("o usuario sera atualizado com sucesso")
def step_impl(context):
    context.criacaocenario.atualiza_usuario()

@then("o usuario sera deletado com sucesso")
def step_impl(context):
    context.criacaocenario.deletar_usuario()

