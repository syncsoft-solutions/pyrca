import math


def psi_to_mpa(psi):
    """
    Converts pressure from PSI to MPa.
    :param psi: The pressure in PSI
    :return: float Pressure in MPa.
    """
    psi = psi / 2.204
    psi = psi * 9.81
    psi = psi / math.pow(25.4, 2)
    return psi
