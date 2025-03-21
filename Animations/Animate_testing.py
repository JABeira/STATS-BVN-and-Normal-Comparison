from manim import *

class Testing(Scene):
    def construct(self):
        square = Square()
        square.set_fill(RED, opacity=0.5)
        square.rotate(PI/4)
        self.play(Create(square))
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(color=BLUE, width=4)
        self.wait(1)    
        self.play(Transform(square, circle))
        self.wait(1)
        self.play(circle.animate.set_stroke(color=RED), run_time=2)
        self.wait(1)

        self.play(FadeOut(circle))
        