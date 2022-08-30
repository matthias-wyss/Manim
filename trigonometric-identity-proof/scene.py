from manim import *

class formule(Scene):
    def construct(self):
        intro = Tex("Proof of", font_size=40).shift(UP)
        equation = MathTex(r'tan^2(\theta) - sin^2(\theta) = tan^2(\theta) \cdot sin^2(\theta)', font_size=40)
        
        self.play(Write(intro))
        self.play(Write(equation))
        self.wait(2)
        self.play(FadeOut(intro, equation))

        math1 = MathTex(r'tan^2(\theta) - sin^2(\theta)', font_size=40)
        math2 = MathTex(r'\frac{sin^2(\theta)}{cos^2(\theta)} - sin^2(\theta)', font_size=40)
        math3 = MathTex(r'\frac{sin^2(\theta)}{cos^2(\theta)} - \frac{sin^2(\theta) \cdot cos^2(\theta)}{cos^2(\theta)}', font_size=40)
        math4 = MathTex(r'\frac{sin^2(\theta) - sin^2(\theta) \cdot cos^2(\theta)}{cos^2(\theta)}', font_size=40)
        math5 = MathTex(r'\frac{sin^2(\theta) \cdot (1 - cos^2(\theta))}{cos^2(\theta)}', font_size=40)
        math6 = MathTex(r'\frac{sin^2(\theta) \cdot sin^2(\theta)}{cos^2(\theta)}', font_size=40)
        math7 = MathTex(r'\frac{sin^2(\theta) \cdot sin^2(\theta)}{cos^2(\theta)}', font_size=40)
        math8 = MathTex(r'sin^2(\theta) \cdot \frac{sin^2(\theta)}{cos^2(\theta)}', font_size=40)
        math9 = MathTex(r'tan^2(\theta) \cdot sin^2(\theta)', font_size=40)

        self.play(Write(math1))
        self.wait(2)
        self.play(ReplacementTransform(math1, math2))
        self.wait(2)
        self.play(ReplacementTransform(math2, math3))
        self.wait(2)
        self.play(ReplacementTransform(math3, math4))
        self.wait(2)
        self.play(ReplacementTransform(math4, math5))
        self.wait(2)
        self.play(ReplacementTransform(math5, math6))
        self.wait(2)
        self.play(ReplacementTransform(math6, math7))
        self.play(ReplacementTransform(math7, math8))
        self.wait(2)
        self.play(ReplacementTransform(math8, math9))
        self.wait(2)
        self.play(FadeOut(math9))

        conclusion = Tex("Therefore", font_size=40).shift(UP)

        self.play(Write(conclusion))
        self.play(Write(equation))
        self.wait(2)
        self.play(FadeOut(conclusion, equation))