from behave import *
from feature.impl.ordem_de_compra import OrdemDeCompra


@given(u'que o usuário selecionou o animal com o id correspondente a "{id}" desejado na petstore')
def step_impl(context, id):
    context.api = OrdemDeCompra()
    context.api.id = int(id)
    context.api.petId = 2
    context.api.quantidade = 10
    context.api.post_criar_uma_nova_ordem()


@then(u'o sistema valida se a ordem de pedido foi armazenada corretamente')
def step_impl(context):
    response = context.api.get_detalhes_ordem(context.api.id)
    assert response.status_code == 200, f"Status code esperado: 200, obtido: {response.status_code}"

    data = context.api.response_data
    print(f"Tipo do ID esperado: {type(context.api.id)}, valor: {context.api.id}")
    print(f"Tipo do ID obtido: {type(data['id'])}, valor: {data['id']}")

    assert data['id'] == context.api.id, f"ID esperado: {context.api.id}, obtido: {data['id']}"
    assert data['petId'] == context.api.petId, f"petId esperado: {context.api.petId}, obtido: {data['petId']}"
    assert data['quantity'] == context.api.quantidade, f"Quantidade esperada: {context.api.quantidade}, obtido: {data['quantity']}"
    assert data['status'] == "placed", f"Status esperado: placed, obtido: {data['status']}"
    assert data['complete'] == True, f"Complete esperado: True, obtido: {data['complete']}"