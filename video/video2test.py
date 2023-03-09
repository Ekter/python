# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from numpy import array, int32

list1 = [
    array([-46, -46], dtype=int32),
    array([-45, -46], dtype=int32),
    array([-44, -47], dtype=int32),
    array([63,  5], dtype=int32),
    array([64,  5], dtype=int32),
    array([65,  4], dtype=int32),
    array([67,  2], dtype=int32),
    array([-45, -45], dtype=int32),
    array([65,  3], dtype=int32),
    array([65,  4], dtype=int32),
    array([65,  3], dtype=int32),
    array([64,  3], dtype=int32),
    array([65,  3], dtype=int32),
    array([63,  4], dtype=int32),
    array([64,  4], dtype=int32),
    array([64,  4], dtype=int32),
    array([64,  3], dtype=int32),
    array([65,  3], dtype=int32),
    array([64,  4], dtype=int32),
    array([65,  4], dtype=int32),
    array([-43, -46], dtype=int32),
    array([-43, -45], dtype=int32),
    array([-44, -45], dtype=int32),
    array([-43, -46], dtype=int32),
    array([-41, -47], dtype=int32),
    array([-43, -45], dtype=int32),
    array([-43, -46], dtype=int32),
    array([-41, -46], dtype=int32),
    array([-43, -45], dtype=int32),
    array([-44, -45], dtype=int32),
    array([-43, -46], dtype=int32),
    array([-44, -45], dtype=int32),
    array([-42, -46], dtype=int32),
    array([-44, -46], dtype=int32),
    array([-43, -46], dtype=int32),
    array([-42, -47], dtype=int32),
    array([-43, -46], dtype=int32),
    array([-43, -46], dtype=int32),
    array([-43, -46], dtype=int32),
    array([-40, -47], dtype=int32),
    array([-42, -47], dtype=int32),
    array([-41, -47], dtype=int32),
    array([-41, -47], dtype=int32),
    array([-41, -46], dtype=int32),
    array([-40, -47], dtype=int32),
    array([-41, -46], dtype=int32),
    array([-40, -47], dtype=int32),
    array([-39, -47], dtype=int32),
    array([-38, -47], dtype=int32),
    array([-39, -46], dtype=int32),
    array([-38, -47], dtype=int32),
    array([-37, -47], dtype=int32),
    array([-37, -47], dtype=int32),
    array([-37, -47], dtype=int32),
    array([-37, -45], dtype=int32),
    array([-39, -45], dtype=int32),
    array([-39, -46], dtype=int32),
    array([-37, -46], dtype=int32),
    array([-37, -46], dtype=int32),
    array([-35, -47], dtype=int32),
    array([-37, -45], dtype=int32),
    array([-35, -46], dtype=int32),
    array([-35, -44], dtype=int32),
    array([-33, -45], dtype=int32),
    array([-31, -46], dtype=int32),
    array([-33, -46], dtype=int32),
    array([-31, -45], dtype=int32),
    array([-33, -47], dtype=int32),
    array([-33, -47], dtype=int32),
    array([-33, -47], dtype=int32),
    array([-35, -45], dtype=int32),
    array([-37, -46], dtype=int32),
    array([-36, -45], dtype=int32),
    array([-35, -46], dtype=int32),
    array([-34, -45], dtype=int32),
    array([-33, -47], dtype=int32),
    array([-35, -49], dtype=int32),
    array([-35, -49], dtype=int32),
    array([-33, -49], dtype=int32),
    array([-31, -48], dtype=int32),
    array([-32, -47], dtype=int32),
    array([-30, -47], dtype=int32),
    array([-29, -47], dtype=int32),
    array([-29, -47], dtype=int32),
    array([-28, -47], dtype=int32),
    array([-26, -47], dtype=int32),
    array([-24, -46], dtype=int32),
    array([-24, -46], dtype=int32),
    array([-22, -46], dtype=int32),
    array([-21, -46], dtype=int32),
    array([1, -74], dtype=int32),
    array([-19, -45], dtype=int32),
    array([-19, -45], dtype=int32),
    array([-20, -51], dtype=int32),
    array([-20, -51], dtype=int32),
    array([-20, -42], dtype=int32),
    array([-19, -42], dtype=int32),
    array([-19, -41], dtype=int32),
    array([-19, -40], dtype=int32),
    array([-19, -40], dtype=int32),
    array([-19, -40], dtype=int32),
    array([-19, -40], dtype=int32),
    array([-20, -40], dtype=int32),
    array([-21, -39], dtype=int32),
    array([-21, -39], dtype=int32),
    array([-21, -39], dtype=int32),
    array([-21, -39], dtype=int32),
    array([-21, -38], dtype=int32),
    array([-21, -38], dtype=int32),
    array([-21, -38], dtype=int32),
    array([-21, -38], dtype=int32),
    array([-21, -37], dtype=int32),
    array([-21, -37], dtype=int32),
    array([-22, -37], dtype=int32),
    array([-20, -38], dtype=int32),
    array([-21, -37], dtype=int32),
    array([-21, -38], dtype=int32),
    array([-20, -38], dtype=int32),
    array([-20, -38], dtype=int32),
    array([-21, -37], dtype=int32),
    array([-21, -36], dtype=int32),
    array([-20, -36], dtype=int32),
    array([-18, -36], dtype=int32),
    array([-18, -37], dtype=int32),
    array([-18, -37], dtype=int32),
    array([-17, -37], dtype=int32),
    array([-15, -37], dtype=int32),
    array([-16, -37], dtype=int32),
    array([-16, -36], dtype=int32),
    array([-17, -37], dtype=int32),
    array([-18, -35], dtype=int32),
    array([-18, -36], dtype=int32),
    array([-16, -35], dtype=int32),
    array([-17, -35], dtype=int32),
    array([-17, -35], dtype=int32),
    array([-17, -35], dtype=int32),
    array([-18, -35], dtype=int32),
    array([-18, -35], dtype=int32),
    array([-20, -34], dtype=int32),
    array([-18, -35], dtype=int32),
    array([-19, -35], dtype=int32),
    array([-20, -35], dtype=int32),
    array([-19, -35], dtype=int32),
    array([-19, -34], dtype=int32),
    array([-21, -34], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-20, -34], dtype=int32),
    array([-19, -33], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-19, -34], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-19, -33], dtype=int32),
    array([-20, -32], dtype=int32),
    array([-19, -32], dtype=int32),
    array([-19, -32], dtype=int32),
    array([-19, -33], dtype=int32),
    array([-19, -32], dtype=int32),
    array([-19, -32], dtype=int32),
    array([-20, -33], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-22, -33], dtype=int32),
    array([-20, -35], dtype=int32),
    array([-22, -33], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-20, -33], dtype=int32),
    array([-19, -34], dtype=int32),
    array([-19, -34], dtype=int32),
    array([-20, -33], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-21, -34], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-22, -35], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-21, -34], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-21, -34], dtype=int32),
    array([-20, -33], dtype=int32),
    array([-21, -32], dtype=int32),
    array([-19, -34], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-19, -34], dtype=int32),
    array([-19, -34], dtype=int32),
    array([-19, -34], dtype=int32),
    array([-20, -34], dtype=int32),
    array([-20, -34], dtype=int32),
    array([-19, -35], dtype=int32),
    array([-19, -35], dtype=int32),
    array([-20, -35], dtype=int32),
    array([-21, -35], dtype=int32),
    array([-21, -35], dtype=int32),
    array([-21, -36], dtype=int32),
    array([-22, -35], dtype=int32),
    array([-22, -35], dtype=int32),
    array([-22, -35], dtype=int32),
    array([-21, -36], dtype=int32),
    array([-23, -34], dtype=int32),
    array([-22, -35], dtype=int32),
    array([-21, -36], dtype=int32),
    array([-21, -37], dtype=int32),
    array([-23, -37], dtype=int32),
    array([-21, -37], dtype=int32),
    array([-19, -36], dtype=int32),
    array([-21, -36], dtype=int32),
    array([-19, -36], dtype=int32),
    array([-17, -35], dtype=int32),
    array([-20, -32], dtype=int32),
    array([-16, -33], dtype=int32),
    array([-15, -33], dtype=int32),
    array([-15, -32], dtype=int32),
    array([-17, -33], dtype=int32),
    array([-19, -31], dtype=int32),
    array([-23, -31], dtype=int32),
    array([-25, -32], dtype=int32),
    array([-25, -32], dtype=int32),
    array([-25, -32], dtype=int32),
    array([-27, -31], dtype=int32),
    array([-27, -31], dtype=int32),
    array([-29, -31], dtype=int32),
    array([-28, -33], dtype=int32),
    array([-29, -33], dtype=int32),
    array([-28, -32], dtype=int32),
    array([-27, -33], dtype=int32),
    array([-27, -32], dtype=int32),
    array([-26, -31], dtype=int32),
    array([-25, -31], dtype=int32),
    array([-25, -32], dtype=int32),
    array([-25, -32], dtype=int32),
    array([-25, -32], dtype=int32),
    array([-25, -32], dtype=int32),
    array([-24, -33], dtype=int32),
    array([-23, -33], dtype=int32),
    array([-23, -32], dtype=int32),
    array([-24, -32], dtype=int32),
    array([-21, -34], dtype=int32),
    array([-23, -32], dtype=int32),
    array([-22, -32], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-21, -33], dtype=int32),
    array([-21, -34], dtype=int32),
    array([-20, -34], dtype=int32),
    array([-22, -33], dtype=int32),
    array([-21, -34], dtype=int32),
    array([-21, -35], dtype=int32),
    array([-20, -36], dtype=int32),
    array([-22, -34], dtype=int32),
    array([-21, -35], dtype=int32),
    array([-22, -35], dtype=int32),
    array([-23, -35], dtype=int32),
    array([-21, -36], dtype=int32),
    array([-23, -36], dtype=int32),
    array([-22, -37], dtype=int32),
    array([-23, -36], dtype=int32),
    array([-22, -37], dtype=int32),
    array([-21, -38], dtype=int32),
    array([-24, -36], dtype=int32),
    array([-25, -37], dtype=int32),
    array([-23, -37], dtype=int32),
    array([-26, -36], dtype=int32),
    array([-25, -36], dtype=int32),
    array([-24, -37], dtype=int32),
    array([-26, -36], dtype=int32),
    array([-26, -36], dtype=int32),
    array([-26, -36], dtype=int32),
    array([-27, -36], dtype=int32),
    array([-25, -37], dtype=int32),
    array([-25, -37], dtype=int32),
    array([-25, -35], dtype=int32),
    array([-26, -35], dtype=int32),
    array([-24, -36], dtype=int32),
    array([-26, -36], dtype=int32),
    array([-25, -36], dtype=int32),
    array([-23, -36], dtype=int32),
    array([-23, -36], dtype=int32),
    array([-24, -36], dtype=int32),
    array([-23, -36], dtype=int32),
    array([-24, -36], dtype=int32),
    array([-23, -37], dtype=int32),
    array([-22, -38], dtype=int32),
    array([-23, -38], dtype=int32),
    array([-23, -38], dtype=int32),
    array([-23, -38], dtype=int32),
    array([-22, -38], dtype=int32),
    array([-22, -37], dtype=int32),
    array([-22, -38], dtype=int32),
    array([-23, -37], dtype=int32),
    array([-22, -37], dtype=int32),
    array([-21, -37], dtype=int32),
    array([-21, -37], dtype=int32),
    array([-23, -37], dtype=int32),
    array([-22, -38], dtype=int32),
    array([-21, -38], dtype=int32),
    array([-22, -38], dtype=int32),
    array([-22, -39], dtype=int32),
    array([-22, -38], dtype=int32),
    array([-22, -39], dtype=int32),
    array([-22, -38], dtype=int32),
    array([-21, -39], dtype=int32),
    array([-22, -38], dtype=int32),
    array([-22, -37], dtype=int32),
    array([-23, -37], dtype=int32),
    array([-22, -38], dtype=int32),
    array([-23, -37], dtype=int32),
    array([-23, -37], dtype=int32),
    array([-23, -38], dtype=int32),
    array([-24, -38], dtype=int32),
    array([-24, -38], dtype=int32),
    array([-24, -38], dtype=int32),
    array([-24, -38], dtype=int32),
    array([-25, -38], dtype=int32),
    array([-25, -38], dtype=int32),
    array([-23, -39], dtype=int32),
    array([-23, -38], dtype=int32),
    array([-26, -37], dtype=int32),
    array([-23, -37], dtype=int32),
    array([-25, -37], dtype=int32),
    array([-25, -37], dtype=int32),
    array([-25, -38], dtype=int32),
    array([-25, -38], dtype=int32),
    array([-28, -36], dtype=int32),
    array([-25, -36], dtype=int32),
    array([-25, -37], dtype=int32),
    array([-25, -35], dtype=int32),
    array([-27, -37], dtype=int32),
    array([-25, -36], dtype=int32),
    array([-28, -35], dtype=int32),
    array([-27, -35], dtype=int32),
    array([-27, -36], dtype=int32),
    array([-27, -36], dtype=int32),
    array([-28, -35], dtype=int32),
    array([-27, -35], dtype=int32),
    array([-27, -35], dtype=int32),
    array([-28, -35], dtype=int32),
    array([-27, -35], dtype=int32),
    array([-27, -35], dtype=int32),
    array([-27, -35], dtype=int32),
    array([-29, -34], dtype=int32),
    array([-26, -35], dtype=int32),
    array([-27, -35], dtype=int32),
    array([-26, -36], dtype=int32),
    array([-27, -34], dtype=int32),
    array([-26, -34], dtype=int32),
    array([-27, -35], dtype=int32),
    array([-27, -35], dtype=int32),
    array([-27, -35], dtype=int32),
    array([-26, -35], dtype=int32),
    array([-27, -36], dtype=int32),
    array([-28, -35], dtype=int32),
    array([-29, -36], dtype=int32),
    array([-27, -36], dtype=int32),
    array([-27, -36], dtype=int32),
    array([-29, -35], dtype=int32),
    array([-28, -36], dtype=int32),
    array([-27, -36], dtype=int32),
    array([-28, -37], dtype=int32),
    array([-29, -36], dtype=int32),
    array([-29, -36], dtype=int32),
    array([-29, -37], dtype=int32),
    array([-29, -37], dtype=int32),
    array([-30, -37], dtype=int32),
    array([-30, -37], dtype=int32),
    array([-30, -37], dtype=int32),
    array([-29, -38], dtype=int32),
    array([-31, -37], dtype=int32),
    array([-32, -37], dtype=int32),
    array([-30, -38], dtype=int32),
    array([-30, -38], dtype=int32),
    array([-30, -38], dtype=int32),
    array([-31, -37], dtype=int32),
    array([-32, -37], dtype=int32),
    array([-31, -38], dtype=int32),
    array([-32, -37], dtype=int32),
    array([-32, -37], dtype=int32),
    array([-32, -38], dtype=int32),
    array([-30, -38], dtype=int32),
    array([-30, -37], dtype=int32),
    array([-31, -37], dtype=int32),
    array([-30, -37], dtype=int32),
    array([-29, -38], dtype=int32),
    array([-30, -37], dtype=int32),
    array([-30, -38], dtype=int32),
    array([-30, -38], dtype=int32),
    array([-30, -38], dtype=int32),
    array([-30, -37], dtype=int32),
    array([-31, -37], dtype=int32),
    array([-31, -37], dtype=int32),
    array([-30, -38], dtype=int32),
    array([-32, -38], dtype=int32),
    array([-33, -37], dtype=int32),
    array([-32, -37], dtype=int32),
    array([-32, -37], dtype=int32),
    array([-33, -37], dtype=int32),
    array([-33, -37], dtype=int32),
    array([-33, -38], dtype=int32),
    array([-33, -37], dtype=int32),
    array([-34, -37], dtype=int32),
    array([-36, -36], dtype=int32),
    array([-35, -38], dtype=int32),
    array([-35, -37], dtype=int32),
    array([-35, -38], dtype=int32),
    array([-35, -37], dtype=int32),
    array([-37, -38], dtype=int32),
    array([-36, -39], dtype=int32),
    array([-36, -39], dtype=int32),
    array([-36, -39], dtype=int32),
    array([-2, -71], dtype=int32),
    array([-38, -40], dtype=int32),
    array([-37, -40], dtype=int32),
    array([-39, -39], dtype=int32),
    array([4, -72], dtype=int32),
    array([4, -77], dtype=int32),
    array([0, -77], dtype=int32),
    array([-39, -42], dtype=int32),
    array([-1, -77], dtype=int32),
    array([-41, -42], dtype=int32),
    array([-41, -41], dtype=int32),
    array([9, -89], dtype=int32),
    array([-40, -47], dtype=int32),
    array([-41, -48], dtype=int32),
    array([-40, -48], dtype=int32),
    array([-41, -47], dtype=int32),
    array([-39, -47], dtype=int32),
    array([-40, -45], dtype=int32),
    array([-40, -45], dtype=int32),
    array([-39, -45], dtype=int32),
    array([-39, -45], dtype=int32),
    array([-39, -46], dtype=int32),
    array([-40, -45], dtype=int32),
    array([-40, -46], dtype=int32),
    array([-41, -45], dtype=int32),
    array([-40, -44], dtype=int32),
    array([-38, -45], dtype=int32),
    array([-39, -44], dtype=int32),
    array([-38, -44], dtype=int32),
    array([-37, -45], dtype=int32),
    array([-38, -44], dtype=int32),
    array([-37, -44], dtype=int32),
    array([-37, -44], dtype=int32),
    array([-37, -44], dtype=int32),
    array([-37, -45], dtype=int32),
    array([-36, -45], dtype=int32),
    array([-36, -46], dtype=int32),
    array([-38, -45], dtype=int32),
    array([-38, -45], dtype=int32),
    array([-39, -44], dtype=int32),
    array([-39, -44], dtype=int32),
    array([-40, -43], dtype=int32),
    array([-39, -44], dtype=int32),
    array([-38, -43], dtype=int32),
    array([-39, -43], dtype=int32),
    array([-39, -43], dtype=int32),
    array([-39, -43], dtype=int32),
    array([-37, -43], dtype=int32),
    array([-37, -44], dtype=int32),
    array([-37, -43], dtype=int32),
    array([-37, -43], dtype=int32),
    array([-37, -44], dtype=int32),
    array([-36, -44], dtype=int32),
    array([-37, -44], dtype=int32),
    array([-37, -43], dtype=int32),
    array([-35, -43], dtype=int32),
    array([-37, -43], dtype=int32),
    array([-35, -43], dtype=int32),
    array([-35, -43], dtype=int32),
    array([-33, -43], dtype=int32),
    array([-33, -44], dtype=int32),
    array([-33, -43], dtype=int32),
    array([-33, -43], dtype=int32),
    array([-32, -43], dtype=int32),
    array([-32, -43], dtype=int32),
    array([-32, -42], dtype=int32),
    array([-32, -43], dtype=int32),
    array([-32, -42], dtype=int32),
    array([-31, -42], dtype=int32),
    array([-31, -41], dtype=int32),
    array([-29, -42], dtype=int32),
    array([-31, -42], dtype=int32),
    array([-29, -42], dtype=int32),
    array([-31, -41], dtype=int32),
    array([-30, -41], dtype=int32),
    array([-29, -43], dtype=int32),
    array([-29, -42], dtype=int32),
    array([-30, -42], dtype=int32),
    array([-30, -42], dtype=int32),
    array([-29, -41], dtype=int32),
    array([-29, -43], dtype=int32),
    array([-29, -42], dtype=int32),
    array([-29, -42], dtype=int32),
    array([-29, -42], dtype=int32),
    array([-29, -42], dtype=int32),
    array([-29, -42], dtype=int32),
    array([-30, -41], dtype=int32),
    array([-31, -39], dtype=int32),
    array([-31, -39], dtype=int32),
    array([-30, -41], dtype=int32),
    array([-29, -41], dtype=int32),
    array([-31, -40], dtype=int32),
    array([-30, -40], dtype=int32),
    array([-31, -41], dtype=int32),
    array([-30, -41], dtype=int32),
    array([-30, -43], dtype=int32),
    array([-31, -42], dtype=int32),
    array([-29, -43], dtype=int32),
    array([-30, -43], dtype=int32),
    array([-30, -43], dtype=int32),
    array([-31, -43], dtype=int32),
    array([-31, -44], dtype=int32),
    array([-32, -43], dtype=int32),
    array([-33, -44], dtype=int32)]

plt.plot(list1)
plt.show()

input()