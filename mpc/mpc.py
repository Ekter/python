import numpy as np
print("importing qpsolvers...")
import qpsolvers
print("Available solvers:", qpsolvers.available_solvers)
print("ok")
import col
from tqdm import tqdm

import clarabel




def newMPC(x0: np.ndarray, xh: np.ndarray, horizon=8, t = 0.1, tolerance: np.ndarray = np.array([0.01, 0.01, 0.1, 0.1, 0.1, 0.1])):

    XH = get_XH(horizon, t)


    TR = np.eye(7*horizon)
    for line in range(horizon):
        TR[line*7:6+line*7, 6+line*7] = -xh

    diag = np.diag([1, 10, 1, 10, 1, 1, 1]*horizon) # = np.eye(7)

    P = XH.T @ TR.T @ diag @ TR @ XH

    # q = np.ones((6+horizon * 2+1))
    q = np.linspace(0, 1, 6+horizon * 2+1)

    # crop = np.zeros(())
    # crop[0:6,0:6] = np.eye(6)
    # crop[-1, -1] = 1

    # b = np.concatenate((x0, np.array([1])), axis=0)                 #XH*u = b   -> initial and final condition, with constraints on all inputs but x0 grounded
    # b = xh
    lb = np.ones_like(q)*-5
    lb[0:6] = x0
    lb[-1] = 1
    ub = np.ones_like(q)*5
    ub[0:6] = x0
    ub[-1] = 1
    u = qpsolvers.solve_qp(P, q, None, None, None, None, lb, ub, solver="clarabel")

    if u is None:
        col.error("Error! No solution found")
        return 0, 0
    col.info("Solution found!")
    return u

def get_XH(horizon, t=0.1):
    A = np.array(
        [
            [0, 1,       0,      0,     0, 0],
            [0, -12.698, -1.926, 0.508, 0, 0],
            [0, 0,       0,      1,     0, 0],
            [0, 234.62,  96.094, 9.385, 0, 0],
            [0, 0,       0,      0,     0, 1],
            [0, 0,       0,      0,     0, 0],
        ]
    )
    cnst = 0.1
    B = np.array(
        [
            [0,     0,     0, 0, 0, 0],
            [2.1,   2.1,   0, 0, 0, 0],
            [0,     0,     0, 0, 0, 0],
            [-39.4, -39.4, 0, 0, 0, 0],
            [0,     0,     0, 0, 0, 0],
            [cnst,  -cnst, 0, 0, 0, 0],
        ]
    )                                               # x dot = A*x+B*u
    I = np.eye(6)
    I_TA = I + t*A
    TB = t*B[:,0:2]

    XH = np.zeros(((6+1)*horizon, 6+2*horizon+1))

    for line in range(horizon-1):          # k in [0,H-1]
        for column in range(line+1):              # i in [0,k]
            XH[7*line:6+7*line, 6+2*column:8+2*column] = I_TA**(line-column+1)@TB
            XH[7*line:6+7*line, 0:6] = I_TA**(line+1)
            XH[7*line+6, -1] = 1
    return XH

# newMPC(np.array([0.1,0,0,0,0,0]), np.array([0,0,0,0,0,0]))


def monoMPC(x0: np.ndarray, xh: np.ndarray, horizon=14, t = 0.1, tolerance: np.ndarray = np.array([0.01, 0.01, 0.1, 0.1, 0.1, 0.1])):
    IC_P = np.array([-0.26,0])
    A = np.array([[1, t], [0, 1]])
    B = np.array([[0.5*t**2], [t]])
    I = np.eye(6)
    I_TA = I + t*A



