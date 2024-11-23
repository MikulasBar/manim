from manim import *
import numpy as np

class Intro(ThreeDScene):
    def construct(self):
        cylinder = Cylinder(
            radius=1,
            height=2,
            stroke_width=0.5,
        )

        top_base = cylinder.base_bottom.copy()

        text = MathTex("V = ", r"\pi r^2", "v")\
            .to_edge(DOWN)\
            .shift(UP * 0.5)\
            .scale(1.5)

        v_brace = Brace(
            cylinder,
            direction=RIGHT,
        )

        r_brace = BraceBetweenPoints(
            cylinder.get_edge_center(UP),
            cylinder.get_corner(UP + RIGHT),
            direction=UP,
        )

        v_label = v_brace.get_tex("v")
        r_label = r_brace.get_tex("r")


        self.set_camera_orientation(theta=0 * DEGREES, phi=75 * DEGREES, gamma=0 * DEGREES)
        # self.begin_ambient_camera_rotation(rate=0.1, about="theta")
        cylinder.add_updater(lambda m, dt: m.rotate(0.1 * dt, axis=OUT))
        self.wait(1)

        self.play(FadeIn(cylinder, scale=0.0), FadeIn(top_base, scale=0.0))
        self.add(top_base)
        self.wait(2)

        self.add_fixed_in_frame_mobjects(text)
        self.play(Write(text))
        self.wait(4)

        self.add_fixed_in_frame_mobjects(v_brace, v_label, r_brace, r_label)
        self.play(Write(v_brace), Write(v_label), Write(r_brace), Write(r_label))
        self.wait(2)

        self.play(
            Indicate(text[1]),
            Indicate(top_base),
        )
        self.wait(1)

        self.play(cylinder.animate.set_opacity(0.5))
        self.wait(0.3)

        self.play(
            top_base.animate.shift(IN * 2),
            Indicate(text[2]),
        )
        self.play(top_base.animate.shift(OUT * 2))
        self.wait(0.3)

        self.play(cylinder.animate.set_opacity(1))
        self.wait(2)

        self.play(
            FadeOut(cylinder),
            FadeOut(text),
            FadeOut(v_brace),
            FadeOut(v_label),
            FadeOut(r_brace),
            FadeOut(r_label),
            FadeOut(top_base),
        )

