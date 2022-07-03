import numpy 
import math

"""
rotations use euler angle, quaternion and more.
"""

import itertools
import numpy as np

"""
Rotations
=========
Note: these have caused many subtle bugs in the past.
Be careful while updating these methods and while using them in clever ways.
See MuJoCo documentations here: http://mujoco_utils.org/book/modeling.html#COrientation
Conventions
-----------
    - All function accept batches as well as indivisual rotations
    - All rotation conventions math respective MuHoCo defaults
    - All angles are in radians
    - Matrices follow LR convention
    - Euler Angles are all relative with 'xyz' axes ordering
    - See specific representation for more information
Representations
---------------
Euler
    There are many euler angle frames -- here we will strive to use the default
        in MuJoCo, which is eulerseq = 'xyz'
    This frame is a relative rotation frame, about x, y and z axes in order.
        Relative rotating means that after we rotate about x, then new
        (rotated) y, and the same for z.
Quaternions
    These are defined in terms of rotation (angle) about a unit vector (x, y, z)
    We use the following <q0, q1, q2, q3> convention:
            q0 = cos(angle / 2)
            q1 = sin(angle / 2) * x
            q2 = sin(angle / 2) * y
            q3 = sin(angle / 2) * z
        This is also sometimes called qw, qx, qy, qz.
"""

# for testing whether a number is close to zero
_FLOAT_EPS = np.finfo(np.float64).eps
_EPS4 = _FLOAT_EPS * 4.0

def as_rotation(r):
    """convert a 3x3 matrix or a quaternion into a standard 3x3 matrix representation."""
    if isinstance(r,np.ndarray) and r.shape == (3,3): return r
    if isinstance(r,np.ndarray) and r.shape == (4,): return quat2mat(r)
    raise ValueError("Invalid rotation{}".format(r))