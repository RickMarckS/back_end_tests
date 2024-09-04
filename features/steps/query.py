import logging
import requests
from behave import given, when, then
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@given('the client wants to query the employee list')
def step_impl(context):
    context.url = 'https://teste-back-end-79fd6-default-rtdb.firebaseio.com/.json' #url base da API


@when('the client makes a query to the database')
def step_impl(context):
    context.response = requests.get(context.url)


@then('the response should be a list with the employee data')
def step_impl(context):
    assert context.response.status_code == 200, f"Erro na requisição: {context.response.status_code}" #erro de status code
    try:
        data = context.response.json() #tenta converter os arquivos se não for Json
        logger.info("Dados recebidos: %s", data) #logger de dados da lista get
    except ValueError as e:
        assert False, f"Falha ao analisar o JSON: {e}" #retorna um erro caso não seja possivél analisar
