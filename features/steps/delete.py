import requests
from behave import given, when, then
from configs.settings import url_modify, logger

@given('the client wants to delete an existing employee')
def step_impl(context):
    context.url = url_modify # Substituir por um ID real


@when('the client confirms the deletion of the employee')
def step_impl(context):
    pass  # Nada a ser feito aqui, pois não há payload para DELETE


@then('the employee should be removed from the database')
def step_impl(context):
    # Envia a requisição DELETE
    context.response = requests.delete(context.url)
    
    # Verifica se o DELETE foi bem-sucedido
    assert context.response.status_code == 200, f"Erro na requisição: {context.response.status_code}"
    try:
        data = context.response.json()  # Tenta converter a resposta para JSON
        logger.info("Resposta ao deletar: %s", data)  # Logger da resposta recebida
    except ValueError as e:
        assert context.response.text == '', f"Falha ao analisar o JSON: {e}"  # Retorna um erro caso não seja possível analisar ou a resposta não seja vazia
