from util.requests.request import *

class Petshop:
    def __init__(self):
        self.header = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.url = "https://petstore.swagger.io/v2"
        self.id = "0"

    def post_criar_usuario(self, usuario, nome, sobrenome, email, senha, telefone, status):
        body = [
            {
                "id": self.id,
                "username": usuario,
                "firstName": nome,
                "lastName": sobrenome,
                "email": email,
                "password": senha,
                "phone": telefone,
                "userStatus": status
            }
        ]
        self.request_ret = call(
            POST,
            self.url + "/user/createWithList",
            headers=self.header,
            json=body,
        )

    def get_retonar_usuario(self, usuario):
        self.user_get = usuario
        self.request_ret = call(
            GET,
            self.url + "/user/" + usuario,
            headers=self.header,
        )
        dados = self.request_ret.json()
        self.id = dados["id"]

    def put_atualiza_usuario(self, usuario, nome, sobrenome, email, senha, telefone, status):
        self.user_put = usuario
        self.pass_put = senha
        body = {
            "id": self.id,
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
        self.user_del = usuario
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
        message = self.request_ret.json()["message"]
        assert message == "ok", f"retorno esperado: ok, obtido: {message}"

    def valida_usuario(self):
        assert (
            self.request_ret.status_code == STATUS_200
        ), f"Error status {self.request_ret.status_code}"
        assert "id" in self.request_ret.json(), "Resposta não contém ID do usuário"
        assert self.user_get == self.request_ret.json()["username"], f"Usuário {self.user_get}, não encontrado na resposta"

    def atualiza_usuario(self):
        assert (
                self.request_ret.status_code == STATUS_200
        ), f"Error status {self.request_ret.status_code}"
        self.get_retonar_usuario(self.user_put)
        self.valida_usuario()
        assert self.request_ret.json()["password"] == self.pass_put, "Retorno ok mas não atualizou a senha"



    def deletar_usuario(self):
        assert (
                self.request_ret.status_code == STATUS_200
        ), f"Error status {self.request_ret.status_code}"
        assert self.user_del == self.request_ret.json()["message"], f"Usuário {self.user_del}, não encontrado na resposta"
