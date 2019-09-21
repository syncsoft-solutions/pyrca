from ..properties.node import Node
import math


def calculate_area(nodes: list):
    """
    Calculates area of a section.
    :param nodes: Nodes list. The coordinates of each corner of a section.
    :return: Area of the section.
    """
    _nodes = nodes.copy()

    # Add the last node to the list
    _nodes.append(_nodes[-1])

    # Number of nodes
    _n = len(_nodes)

    # Initial value of area
    _area = 0.0

    for i in range(_n - 1):
        j = (i + 1) % _n
        _area += _nodes[i].x * _nodes[j].y
        _area -= _nodes[j].x * _nodes[i].y

    _area = abs(_area) / 2
    return _area
