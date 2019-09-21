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


def calculate_centroid_y(nodes: list):
    """
    Calculates centroid of a polygon from the top.
    :param nodes: Nodes list. The coordinates of each corner of a section.
    :return: Distance of centroid from the top.
    """
    _nodes = nodes.copy()

    # Add the last node to the list
    _nodes.append(_nodes[-1])

    # Number of nodes
    _n = len(_nodes)

    _area = calculate_area(_nodes)

    _kd = 0

    for i in range(_n - 1):
        _kd += (_nodes[i].y + _nodes[i+1].y) * \
              (_nodes[i].x * _nodes[i+1].y - _nodes[i+1].x * _nodes[i].y)

    _kd = abs(_kd / (6 * _area))
    _kd = abs(get_highest_node(_nodes).y - _kd)

    return _kd


def get_highest_node(nodes: list):
    """
    Get the topmost node from the section.
    :param nodes: Nodes list. The coordinates of each corner of a section.
    :return: Highest node.
    """
    if len(nodes) == 0:
        return None

    _highest_node = nodes[0]

    for _node in nodes:
        if _node.y > _highest_node.y:
            _highest_node = _node

    return _highest_node


def get_lowest_node(nodes: list):
    """
        Get the bottommost node from the section.
        :param nodes: Nodes list. The coordinates of each corner of a section.
        :return: Lowest node.
        """
    if len(nodes) == 0:
        return None

    _lowest_node = nodes[0]

    for _node in nodes:
        if _node.y < _lowest_node.y:
            _lowest_node = _node

    return _lowest_node
