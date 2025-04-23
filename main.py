from util.environments.gen_func import *


def main_sem_args():
    try:
        features = [
            #"criacao_cenario.feature",
            "ordem_de_compra.feature",
            #"pet_shop.feature"
        ]
        for feature in features:
            executar(feature)
    except Exception as e:
        print(e)

main_sem_args()