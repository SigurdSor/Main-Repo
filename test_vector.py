import numpy as np
import nose.tools as nt
from vector import Vector3D

def test_add():
    u = Vector3D(1, 2, 0)
    v = Vector3D(1, -1, 3)
    w = u + v
    nt.assert_equal(w.x, 2)
    nt.assert_equal(w.y, 1)
    nt.assert_equal(w.z, 3)

def test_equal():
    u = Vector3D(1, 1, 0)
    v = Vector3D(2, 1, 1)
    w = Vector3D(1, 1, 0)

def test_length():
    u = Vector3D(1, 1, 0)
    nt.assert_almost_equal(u.length, np.sqrt(2))
