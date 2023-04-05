import random


def decimal_to_binary(decimal, N):
    binary = []
    for i in range(0, N):
        binary.append(int(decimal%2))
        decimal = (decimal - decimal%2)/2
    return binary


def binary_to_decimal(binary, N):
    decimal = 0
    for i in range(0, N):
        decimal = decimal + binary[i] * (2**i)
    return decimal


def xor2(x1, x2):
    if x1 == x2:
        z = 0
    else:
        z = 1
    return z


def and2(x1, x2):
    if (x1 == 1) and (x2 == 1):
        z = 1
    else:
        z = 0
    return z


def or2(x1, x2):
    if (x1 == 0) and (x2 == 0):
        z = 0
    else:
        z = 1
    return z


def not1(x1):
    if x1 == 0:
        z = 1
    else:
        z = 0
    return z


def mux3(x1, x2, control):
    if control == 0:
        z = x1
    else:
        z = x2
    return z


def random_sequence_generator(N):
    random_binary_number = []
    for i in range(0,N):
        bit = random.randint(0,1)
        random_binary_number.append(bit)
    random_decimal_number = binary_to_decimal(random_binary_number,N)
    return random_decimal_number
