
import requests
from behave import given, when, then
from configs.settings import logger, url_modify, patch_payload


@given('the client wants to update an existing employee')
def step_impl(context):
    # URL do funcionário específico a ser atualizado (supondo que '-O4QeHU-576CybnpjTnk' seja o ID)
    context.url = url_modify  # Substituir por um ID real


@when('the client fills out the form with the new data')
def step_impl(context):
    # Dados que serão atualizados via PATCH
    context.payload = patch_payload


@then('the client submits the form and the employee is updated')
def step_impl(context):
    # Envia os dados via PATCH
    context.response = requests.patch(context.url, json=context.payload)

    # Verifica se o PATCH foi bem-sucedido
    assert context.response.status_code == 200, f"Erro na requisição: {context.response.status_code}"
    try:
        data = context.response.json()  # Tenta converter a resposta para JSON
        logger.info("Dados atualizados: %s", data)  # Logger dos dados retornados
    except ValueError as e:
        assert False, f"Falha ao analisar o JSON: {e}"  # Retorna um erro caso não seja possível analisar
