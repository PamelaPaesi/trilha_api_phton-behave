from behave import *
from feature.impl.pet_shop import Petshop

@given("que sera identificado os dados para o login na petshop")
def step_impl(context):
    context.petshop = Petshop()


@when("enviado requisição com os dados {usuario}, {nome}, {sobrenome}, {email}, {senha}, {telefone}, {status} para cadastrar usuario")
def step_impl(context, usuario, nome, sobrenome, email, senha, telefone, status):
    context.petshop.post_criar_usuario(usuario, nome, sobrenome, email, senha, telefone, status)

@given("que eu tenha os dados {usuario} para consultar")
def step_impl(context, usuario):
    context.petshop.get_retonar_usuario(usuario)

@when("enviado requisição com os dados {usuario} para consultar usuario")
def step_impl(context, usuario):
    context.petshop.get_retonar_usuario(usuario)

@when("enviado requisição com os dados  {usuario}, {nome}, {sobrenome} {email}, {senha}, {telefone}, {status} para atualizar usuario")
def step_impl(context, usuario, nome, sobrenome, email, senha, telefone, status):
    context.petshop.put_atualiza_usuario(usuario, nome, sobrenome, email, senha, telefone, status)

@when("enviado requisição com os dados {usuario} para deletar usuario")
def step_impl(context, usuario):
    context.petshop.delete_usuario(usuario)

@then("usuario sera cadastrado com sucesso")
def step_impl(context):
    context.petshop.retorno_usuario()

@then("usuario sera validado com sucesso")
def step_impl(context):
    context.petshop.valida_usuario()

@then("usuario sera atualizado com sucesso")
def step_impl(context):
    context.petshop.atualiza_usuario()

@then("usuario sera deletado com sucesso")
def step_impl(context):
    context.petshop.deletar_usuario()
