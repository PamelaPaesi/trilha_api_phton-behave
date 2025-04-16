from util.environments.gen_func import *


def main_sem_args():
    try:
        features = [
            "criacao_cenario.feature"
        ]
        for feature in features:
            executar(feature)
    except Exception as e:
        print(e)

main_sem_args()