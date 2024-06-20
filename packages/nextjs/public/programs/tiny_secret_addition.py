from nada_dsl import *

def nada_main():
    party1 = Party(name="Tom")

    my_int1 = SecretInteger(Input(name="test", party=party1))

    my_int2 = SecretInteger(Input(name="test2", party=party1))

    new_int = my_int1 + my_int2

    return [Output(new_int, "my_output", party1)]