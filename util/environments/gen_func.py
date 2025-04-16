from behave import __main__ as behave_executable

def executar(modulo=""):
    config_behave = r" --no-capture --no-capture-stderr "
    config_behave = config_behave + " --stop "
    behave_command = r"feature/%s %s" % (modulo, config_behave)
    behave_executable.main(behave_command)