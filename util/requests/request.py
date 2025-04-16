import json
from enum import *
import requests

STATUS_200 = 200
STATUS_201 = 201
STATUS_202 = 202
STATUS_204 = 204
STATUS_302 = 302
STATUS_404 = 404
STATUS_422 = 422
STATUS_500 = 500
STATUS_401 = 401
STATUS_400 = 400
STATUS_428 = 428

POST = "post"
PUT = "put"
GET = "get"
DELETE = "delete"
PATCH = "patch"


def imprime_resultado(response, status_response=True):
    print('--------------------------')
    print(f'STATUS: {response.status_code} - LATÊNCIA: {response.elapsed}')

    if status_response:
        print('RESPONSE:')
        try:
            if response.content:
                decoded_content = response.content.decode('utf-8')
                json_data = json.loads(decoded_content)
                print(json.dumps(json_data, indent=2))
            else:
                print("Resposta vazia.")
        except UnicodeDecodeError as ude:
            print(f"Erro de decodificação: {ude}")
            print("Conteúdo bruto (hex):", response.content.hex())
        except json.JSONDecodeError as jde:
            print(f"Erro ao carregar JSON: {jde}")
            print("Texto da resposta:", response.text)
        except Exception as e:
            print(f"Erro inesperado: {e}")

    print('--------------------------')


def imprime_entrada(metodo, url, header, body, data, jsonArg):
    print("--------------------------")
    print(metodo + " " + str(url))
    print("HEADER:")
    print(json.dumps(str(header), indent=2))
    print("BODY:")
    if body is not None:
        try:
            print(json.dumps(body, indent=2))
        except:
            pass
    if data is not None:
        try:
            print(json.dumps(data, indent=2))
        except:
            pass
    if json is not None:
        try:
            print(json.dumps(jsonArg, indent=2))
        except:
            pass
    print("--------------------------")


def call(metodo, url, **kwargs):
    """CONFORME informacoes da biblioteca requests temos esses argumentos
        :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
        :param url: URL for the new :class:`Request` object.
    ######## IMPORTANTE ###############################
    ####### kwargs que podemos usar: ##################
    ###################################################
        :param params: (optional) Dictionary, list of tuples or bytes to send
            in the query string for the :class:`Request`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
        :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
            ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
            or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
            defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
            to add for the file.
        :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How many seconds to wait for the server to send data
            before giving up, as a float, or a :ref:`(connect timeout, read
            timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
                the server's TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use. Defaults to ``True``.
        :param stream: (optional) if ``False``, the response content will be immediately downloaded.
        :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.

      #return
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
    """

    # Remover status_response de kwargs
    status_response = kwargs.pop('status_response', True)

    # Imprime a entrada
    imprime_entrada(
        metodo, url, kwargs.get("headers"), kwargs.get("body"), kwargs.get("data"), kwargs.get("json")
    )

    # Fazer a requisição
    response = requests.request(metodo, url, **kwargs)

    # Imprimir o resultado
    imprime_resultado(response, status_response)

    return response