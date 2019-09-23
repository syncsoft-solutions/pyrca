import unittest
from pyrca.properties.node import Node
from pyrca.properties.section import Section
from pyrca.properties.beam_section import BeamSection
from pyrca.properties.steel_tension import SteelTension
from ..beam_analyses import BeamAnalyses
from ..stress_distribution import StressDistribution


class TestBeamAnalysis(unittest.TestCase):
    _nodes = [Node(0, 0), Node(0, 500), Node(250, 500), Node(250, 0)]

    _section = Section()
    _section.set_main_section(_nodes)

    _bs = BeamSection()
    _bs.set_fc_prime(20.7)
    _bs.set_fy(276.5)
    _bs.set_effective_depth(460)

    _tension_steel = SteelTension()
    _tension_steel.set_total_area(1472.62)

    _bs.steel_tension = _tension_steel

    _analysis = BeamAnalyses.beam_capacity_analysis(sd=StressDistribution.WHITNEY)
    print(_analysis)


if __name__ == '__main__':
    unittest.main()