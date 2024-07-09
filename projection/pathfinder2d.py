import random
import tkinter as tk
import shapely
import bezier
import numpy as np
import time
from typing import Callable


# setattr(shapely.geometry.Point, "__mul__", lambda self, number: shapely.geometry.Point(self.x * number, self.y * number))
# setattr(shapely.geometry.Point, "__add__", lambda self, other: shapely.geometry.Point(self.x + other.x, self.y + other.y))
# setattr(shapely.geometry.Point, "__sub__", lambda self, other: shapely.geometry.Point(self.x - other.x, self.y - other.y))

class Point2D(shapely.geometry.Point):

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

    def __add__(self, other) -> "Point2D":
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> "Point2D":
        return Point2D(self.x - other.x, self.y - other.y)

    def __mul__(self, number) -> "Point2D":
        return Point2D(self.x * number, self.y * number)



class Line2D:
    ACCURACY = 0.0001 # is used for avoiding vertical lines in Line2D for gradient calculation in above method
    def __init__(self, a: Point2D, b: Point2D):
        self.a = a+Point2D(random.random()*Line2D.ACCURACY, random.random()*Line2D.ACCURACY)
        self.b = b

    def __repr__(self):
        return f"Line2D({self.a}, {self.b})"

    def above(self, point: Point2D):
        return (self.b.x - self.a.x) * (point.y - self.a.y) - (self.b.y - self.a.y) * (point.x - self.a.x) > 0


class Polygon2D(shapely.geometry.Polygon):
    def __init__(self, points: list[Point2D]):
        super().__init__([point.x, point.y] for point in points)
        self.points = points

    def __repr__(self):
        return f"Polygon2D({self.points})"


class BezierCurve2D:
    def __init__(self, points: list[Point2D]):
        self.points = points
        self._points_iter = []

    def __repr__(self) -> str:
        return f"BezierCurve2D({self.points})"

    def get_points(self, dx) -> list[Point2D]:
        if not self._points_iter:
            for i in range(0, len(self.points)-1):
                for t in range(0, int(1/dx)+1):
                    x = self.points[i].x + (self.points[i+1].x - self.points[i].x) * t * dx
                    y = self.points[i].y + (self.points[i+1].y - self.points[i].y) * t * dx
                    self._points_iter.append(Point2D(x, y))
        return self._points_iter




class Path2D:
    def __init__(self, begin: Point2D, end: Point2D, init_speed: Point2D = None, final_speed: Point2D = None, obstacles_: list[Polygon2D] = None):
        self.begin = begin
        self.init_speed = init_speed if init_speed else Point2D(0,0)
        self.end = end
        self.final_speed = final_speed if final_speed else Point2D(0,0)
        self.obstacles = obstacles_ if obstacles_ else []

    def solve(self, retries: int = 1000, max_distance: float = 1000, max_points = 4, spacing = 5, plotter: Callable=None) -> bezier.Curve:
        ok: list[bezier.Curve] = []
        for additional in range(max_points):
            print(additional, "#########################################")
            max_retries_loop = int(retries*additional/max_points+1)
            for retry_n in range(max_retries_loop):
                points = [self.begin]
                if self.init_speed.x or self.init_speed.y:
                    points.append(Point2D(self.begin.x+self.init_speed.x,
                    self.begin.y+self.init_speed.y))
                for i_ in range(1, additional+1):
                    points.append(Point2D(
                        random.normalvariate(
                            self.begin.x+(self.end.x-self.begin.x)*(i_/(additional+1)),
                            retry_n*max_distance/max_retries_loop
                        ),
                        random.normalvariate(
                            self.begin.y+(self.end.y-self.begin.y)*(i_/(additional+1)),
                            retry_n*max_distance/max_retries_loop
                        )
                    ))  #random point around fraction of the path (i+1/additional+1) with variance of retry_n*max_distance
                if self.final_speed.x or self.final_speed.y:
                    points.append(Point2D(self.end.x-self.final_speed.x,
                    self.end.y-self.final_speed.y))
                points.append(self.end)
                curve = bezier.Curve.from_nodes((np.asfortranarray([
                    [point.x for point in points],
                    [point.y for point in points]
                ])))
                if callable(plotter):
                    plotter(curve)
                t = time.time()
                # for obstacle in self.obstacles:
                #     # x_, y_ = obstacle.exterior.coords.xy
                #     corners = shapely.get_coordinates(obstacle)
                #     for index in range(len(corners)-1):
                #         try:
                #             if len(curve.intersect(bezier.Curve.from_nodes(np.array([corners[index], corners[index+1]])))):
                #                 print(f"{n} is not good(index {index})!")
                #                 n+=1
                #                 break
                #         except ValueError as e:
                #             print(e)
                #     else:
                #         continue
                #     break
                dist = max_distance/(max(additional, 1))
                _obstacles = list(filter(lambda obstacle: obstacle.centroid.distance(self.begin) < dist or any((Point2D(*point).distance(self.begin) < dist for point in shapely.get_coordinates(obstacle))), self.obstacles))
                print(_obstacles)
                for point in np.transpose(curve.evaluate_multi(np.linspace(0.0, 1.0, int(curve.length/spacing)))):
                    for obstacle in _obstacles:
                        # t_ = time.time()
                        # a = obstacle.centroid.distance(self.begin)> 200
                        # a = obstacle.centroid.distance(Point2D(*point)) > obstacle.length/2
                        # a = obstacle.contains(Point2D(*point))
                        # print(time.time()-t_)
                        # if a:
                        # if obstacle.centroid.distance(Point2D(*point)) > obstacle.length/2:
                            # continue
                        if obstacle.contains(Point2D(*point)):
                            break
                    else:
                        continue
                    break
                else:
                    ok.append(curve)
                print(time.time()-t)
            if len(ok) > 0:
                break
        else:
            print("No path found")
            return bezier.Curve.from_nodes(np.array([list(set([self.begin.x, self.begin.x+self.init_speed.x, self.end.x-self.final_speed.x, self.end.x])), list(set([self.begin.y, self.begin.y+self.init_speed.y, self.end.y-self.final_speed.y, self.end.y]))]))
        print(additional)
        best = min(ok, key=lambda curve: curve.length)
        return best
        # TODO make the path closer to the obstacles and lower retries
        # for point in best.points[1:-1]:

    def view(self, path: bezier.Curve = None, boundaries: list[int] = None):
        window = tk.Tk()
        if not boundaries:
            boundaries = [800, 800]
        canvas = tk.Canvas(window, width=boundaries[0], height=boundaries[1])

        def plotter(curve:bezier.Curve):
            s_vals = np.linspace(0.0, 1.0, 100)
            points = curve.evaluate_multi(s_vals)
            points = list(zip(points[0], points[1]))
            canvas.create_line(points)

        for obstacle in self.obstacles:
            points = [(point[0], point[1]) for point in shapely.get_coordinates(obstacle)]
            canvas.create_polygon(points, fill="red")

        canvas.create_oval(self.begin.x-5, self.begin.y-5, self.begin.x+5, self.begin.y+5, fill="lightblue")
        canvas.create_oval(self.end.x-5, self.end.y-5, self.end.x+5, self.end.y+5, fill="blue")

        if path:
            points = [(point.x, point.y) for point in path.points]
            canvas.create_line(points, fill="green")
            points = [(point.x, point.y) for point in path.get_points(0.05)]
            canvas.create_line(points, fill="black")
        else:
            t=time.time()
            # plotter = None
            curve = self.solve(max_distance=(boundaries[0]**2+boundaries[1]**2)**0.5, plotter=plotter, retries=74, spacing=3)
            print(time.time()-t)
            s_vals = np.linspace(0.0, 1.0, 100)
            points = curve.evaluate_multi(s_vals)
            # print([(pointsx, pointsy) for (pointsx, pointsy) in zip(points[0], points[1])])
            points = list(zip(points[0], points[1]))
            canvas.create_line(points, fill="green")

        canvas.pack()
        window.mainloop()



if __name__ == "__main__":
    obstacles = []
    maxx = 2500
    maxy = 1300
    for _ in range(15):
        for i in range(3, 5):
            points: list[Point2D] = []
            centerx = random.random()*maxx
            centery = random.random()*maxy

            for j in range(i):
                points.append(Point2D(random.random()*400+centerx, random.random()*400+centery))
            polygon = Polygon2D(points)
            obstacles.append(polygon)
            print(polygon)
    obstacles.append(Polygon2D([Point2D(-37,5), Point2D(maxx+37,5), Point2D(maxx+37,-37), Point2D(-37,-37)]))
    obstacles.append(Polygon2D([Point2D(-37,maxy+37), Point2D(maxx+37,maxy+37), Point2D(maxx+37,maxy-5), Point2D(-37,maxy-5)]))
    obstacles.append(Polygon2D([Point2D(-37,5), Point2D(-37,maxy+37), Point2D(5,maxy+37), Point2D(5,5)]))
    obstacles.append(Polygon2D([Point2D(maxx+37,5), Point2D(maxx+37,maxy+37), Point2D(maxx-5,maxy+37), Point2D(maxx-5,5)]))

    path = Path2D(Point2D(random.uniform(30,maxx-30), random.uniform(30,maxy-30)), Point2D(random.uniform(30,maxx-30), random.uniform(30,maxy-30)), Point2D(random.uniform(-300,300),random.uniform(-300,300)), Point2D(random.uniform(-300,300),random.uniform(-300,300)), obstacles)
    # path.view(BezierCurve2D([Point2D(100, 100), Point2D(200, 700), Point2D(700, 700)]))
    path.view(boundaries=[maxx, maxy])
