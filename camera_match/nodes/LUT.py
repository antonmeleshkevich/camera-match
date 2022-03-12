from colour import LUT3D
import numpy as np
from colour.algebra import table_interpolation_tetrahedral
import itertools
from scipy.interpolate import PchipInterpolator
from .Node import Node

from typing import Optional, Any, Tuple
from numpy.typing import NDArray

# xalglib only available in Windows & Linux(?)
try:
    from xalglib import xalglib
except ImportError:
    import warnings
    warnings.warn("RBF library cannot be loaded.", ImportWarning)

class RBF(Node):
    def __init__(self, size: int=33, radius: float=5.0, layers: int=10, smoothing: float=0.001):
        self.size = size
        self.LUT = None

        self.radius = radius
        self.layers = layers
        self.smoothing = smoothing

    def solve(self, source: NDArray[Any], target: NDArray[Any]) -> Tuple[NDArray[Any], NDArray[Any]]:
        data = np.hstack((source, target))

        model = xalglib.rbfcreate(3, 3)
        xalglib.rbfsetpoints(model, data.tolist())
        xalglib.rbfsetalgohierarchical(model, self.radius, self.layers, self.smoothing)
        xalglib.rbfbuildmodel(model)

        LUT_table = LUT3D.linear_table(self.size)

        for x, y, z in itertools.product(range(self.size), range(self.size), range(self.size)):
            LUT_table[x][y][z] = xalglib.rbfcalc(model, [x / self.size, y / self.size, z / self.size])

        self.LUT = LUT3D(table=LUT_table)
        return (self.apply(source), target)

    def apply(self, RGB: NDArray[Any]) -> NDArray[Any]:
        if self.LUT is None:
            return RGB

        return self.LUT.apply(RGB, interpolator=table_interpolation_tetrahedral)

