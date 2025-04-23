from util.requests.request import *

class PetShop:
    def __init__(self):
        self.header = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        self.url = "https://petstore.swagger.io/v2"

    def post_criar_usuario(self, ):
        body = {

        }