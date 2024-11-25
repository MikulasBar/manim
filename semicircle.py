from manim import *
import numpy as np

R = 2.0

class Semicircle(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-R-1,R+1],
            y_range=[-1,R+1]
        )

        sc_graph = FunctionGraph(
            lambda t: np.sqrt(R ** 2 - t ** 2),
            x_range=[-R,R],
            color=RED
        )

        self.add(axes, sc_graph)

