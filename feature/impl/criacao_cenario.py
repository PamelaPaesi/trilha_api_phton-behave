from util.requests.request import *
class Criacaocenario:

    def __init__(self):
        self.header = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.url = "https://petstore.swagger.io/v2"

    def post_criar_usuario(self, usuario, nome, sobrenome, email, senha, telefone, status):
        body = {
            "id": 0,
            "username": usuario,
            "firstName": nome,
            "lastName": sobrenome,
            "email": email,
            "password": senha,
            "phone": telefone,
            "userStatus": status
        }
        self.request_ret = call(
            POST,
            self.url + "/user",
            headers=self.header,
            json=body,
        )

    def get_retona_usuario(self, usuario):
        body={}
        self.request_ret = call(
            GET,
            self.url + "/user/" + usuario,
            headers=self.header,
            json=body,
        )

    def put_atualiza_usuario(self, usuario, nome, sobrenome, email, senha, telefone, status):
        body = {
            "id": 0,
            "username": usuario,
            "firstName": nome,
            "lastName": sobrenome,
            "email": email,
            "password": senha,
            "phone": telefone,
            "userStatus": status
        }
        self.request_ret = call(
            PUT,
            self.url + "/user/" + usuario,
            headers=self.header,
            json=body,
        )

    def delete_usuario(self, usuario):
        body = {}
        self.request_ret = call(
            DELETE,
            self.url + "/user/" + usuario,
            headers=self.header,
            json=body,
        )

    def retorno_usuario(self):
        assert (
            self.request_ret.status_code == STATUS_200
        ), f"Error status {self.request_ret.status_code}"

    def valida_usuario(self):
        assert (
            self.request_ret.status_code == STATUS_200
        ), f"Error status {self.request_ret.status_code}"
        assert "id" in self.request_ret.json(), "Resposta não contém ID do usuário"

    def atualiza_usuario(self):
        assert (
                self.request_ret.status_code == STATUS_200
        ), f"Error status {self.request_ret.status_code}"

    def deletar_usuario(self):
        assert (
                self.request_ret.status_code == STATUS_200
        ), f"Error status {self.request_ret.status_code}"
