import os
import json

"""
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.
before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.
before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.
before_tag(context, tag), after_tag(context, tag)
"""

# -- SETUP: Use cfparse as default matcher
# from behave import use_step_matcher
# step_matcher("cfparse")

def get_bdd(scenario):
    bdd = ''
    for passo in scenario.steps:
        bdd += passo.keyword + ' ' + passo.name + '\n'
    return bdd

def get_prioridade(list_tags):
    for tag in list_tags:
        if str(tag).lower() == "prioridade1":
            return 1
        if str(tag).lower() == "prioridade2":
            return 2
        if str(tag).lower() == "prioridade3":
            return 3
        if str(tag).lower() == "prioridade4":
            return 4
    return -1

def before_scenario(context, scenario):
    json_file_path = os.getenv('JSON_FILE_PATH', 'util/archives')
    file_path = os.path.join(json_file_path, 'accounts.data')

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado")

    with open(file_path, 'r') as file:
        context.dados_json = json.load(file)

def after_step(context, step):
    if step.status == 'passed':
        pass
    elif step.status == 'failed':
        raise Exception('failed')
