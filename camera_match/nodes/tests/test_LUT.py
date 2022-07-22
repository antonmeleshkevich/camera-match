import numpy as np
from camera_match import (
    RBF
)

# From https://github.com/Polyrhythm/create_lut/blob/main/main.py
MATRIX_TEST = np.array(
    [
        [0.17224810, 0.09170660, 0.06416938],
        [0.49189645, 0.27802050, 0.21923399],
        [0.10999751, 0.18658946, 0.29938611],
        [0.11666120, 0.14327905, 0.05713804],
        [0.18988879, 0.18227649, 0.36056247],
        [0.12501329, 0.42223442, 0.37027445],
        [0.64785606, 0.22396782, 0.03365194],
        [0.06761093, 0.11076896, 0.39779139],
        [0.49101797, 0.09448929, 0.11623839],
        [0.11622386, 0.04425753, 0.14469986],
        [0.36867946, 0.44545230, 0.06028681],
        [0.61632937, 0.32323906, 0.02437089],
        [0.03016472, 0.06153243, 0.29014596],
        [0.11103655, 0.30553067, 0.08149137],
        [0.41162190, 0.05816656, 0.04845934],
        [0.73339206, 0.53075188, 0.02475212],
        [0.47347718, 0.08834792, 0.30310315],
        [0.00000000, 0.25187016, 0.35062450],
        [0.76809639, 0.78486240, 0.77808297],
        [0.53822392, 0.54307997, 0.54710883],
        [0.35458526, 0.35318419, 0.35524431],
        [0.17976704, 0.18000531, 0.17991488],
        [0.09351417, 0.09510603, 0.09675027],
        [0.03405071, 0.03295077, 0.03702047],
    ]
)

MATRIX_REFERENCE = np.array(
    [
        [0.15579559, 0.09715755, 0.07514556],
        [0.39113140, 0.25943419, 0.21266708],
        [0.12824821, 0.18463570, 0.31508023],
        [0.12028974, 0.13455659, 0.07408400],
        [0.19368988, 0.21158946, 0.37955964],
        [0.19957424, 0.36085439, 0.40678123],
        [0.48896605, 0.20691688, 0.05816533],
        [0.09775522, 0.16710693, 0.47147724],
        [0.39358649, 0.12233400, 0.10526425],
        [0.10780332, 0.07258529, 0.16151473],
        [0.27502671, 0.34705454, 0.09728099],
        [0.43980441, 0.26880559, 0.05430533],
        [0.05887212, 0.11126272, 0.38552469],
        [0.12705825, 0.25787860, 0.13566464],
        [0.35612929, 0.07933258, 0.05118732],
        [0.48131976, 0.42082843, 0.07120612],
        [0.34665585, 0.15170714, 0.24969804],
        [0.08261116, 0.24588716, 0.48707733],
        [0.66054904, 0.65941137, 0.66376412],
        [0.48051509, 0.47870296, 0.48230082],
        [0.33045354, 0.32904184, 0.33228886],
        [0.18001305, 0.17978567, 0.18004416],
        [0.10283975, 0.10424680, 0.10384975],
        [0.04742204, 0.04772203, 0.04914226],
    ]
)



class TestRBF:
    def test_solve(self):
        node = RBF()
        node.solve(MATRIX_TEST, MATRIX_REFERENCE)
        source = node(MATRIX_TEST)

        np.testing.assert_allclose(
            source,
            MATRIX_REFERENCE,
            atol=0.06
        )


