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
    psi = psi / math.pow(MILLIMETER_PER_INCH, 2)
    return psi


def mpa_to_psi(mpa):
    """
    Converts pressure from MPa to PSI
    :param mpa: Pressure in MPa
    :return: Pressure in PSI
    """
    mpa = mpa * POUND_PER_KILOGRAM
    mpa = mpa / GRAVITY_METRIC
    mpa = mpa * math.pow(MILLIMETER_PER_INCH, 2)
    return mpa


def mm_to_in(mm):
    """
    Converts length in millimeter to inches.
    :param mm: Length in millimeter
    :return: Length in inches
    """
    return mm / MILLIMETER_PER_INCH


def in_to_mm(inch):
    """
    Convertes length in inches to millimeter
    :param inch: Length in inches
    :return: Length in millimeter
    """
    return inch * MILLIMETER_PER_INCH
