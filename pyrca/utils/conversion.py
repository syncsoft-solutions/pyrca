import math
from .constants import *


def psi_to_mpa(psi):
    """
    Converts pressure from PSI to MPa.
    :param psi: The pressure in PSI
    :return: Pressure in MPa.
    """
    psi = psi / POUND_PER_KILOGRAM
    psi = psi * GRAVITY_METRIC
    psi = psi / math.pow(25.4, 2)
    return psi


def mpa_to_psi(mpa):
    mpa = mpa * POUND_PER_KILOGRAM
    mpa = mpa / GRAVITY_METRIC
    mpa = mpa * math.pow(25.4, 2)
    return mpa
