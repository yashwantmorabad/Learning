import numpy as np
from manim import *


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


class LinearTransformationScene(Scene):

    def construct(self):
        # 1. Create the grid plane
        plane = NumberPlane()
        self.add(plane)

        # 2. Define the homotopy function
        def homotopy(x, y, z, t):
            norm = np.linalg.norm([x, y])
            tau = interpolate(5, -5, t) + norm / config.frame_width
            alpha = sigmoid(tau)
            return [x, y + 0.5 * np.sin(2 * np.pi * alpha), z]

        # 3. Animate non-linear homotopy transformation (using Homotopy instead of HomotopyAnimation)
        self.play(Homotopy(homotopy, plane, run_time=3))
        self.wait(2)

        # 4. Animate linear matrix transformation
        matrix = [[2, 1], [1, 2]]
        self.play(plane.animate.apply_matrix(matrix))
        self.wait(1)
        