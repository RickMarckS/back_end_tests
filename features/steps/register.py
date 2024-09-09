import requests
from behave import given, when, then
from configs.settings import logger, url_base, post_payload



@given('the client wants to register a new employee')
def step_impl(context):
    context.url = url_base  # url de acesso básica


@when('the client fills out the form with the data')
def step_impl(context):
    context.payload = post_payload # Dados do novo funcionário que serão enviados no POST


@then('the client submits the form and the employee is registered')
def step_impl(context):
    # Envia os dados via POST
    context.response = requests.post(context.url, json=context.payload)

    # Verifica se o POST foi bem-sucedido
    assert context.response.status_code == 200, f"Erro na requisição: {context.response.status_code}"
    try:
        data = context.response.json()  # Tenta converter a resposta para JSON
        logger.info("Dados recebidos: %s", data)  # Logger dos dados recebidos
    except ValueError as e:
        assert False, f"Falha ao analisar o JSON: {e}"  # Retorna um erro caso não seja possível analisar

