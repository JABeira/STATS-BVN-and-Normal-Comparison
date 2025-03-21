from manim import *

class Intro(Scene):
    def construct(self):
        title = Text("Finding Some Order in Chaos")
        name = Text("Joshua Beira")

        title.scale(1.5)
        name.scale(0.5)

        page = VGroup(title, name)
        page.arrange(DOWN, aligned_edge=RIGHT, buff=0.5)

        self.play(Create(page), run_time=2)

        self.wait(3)
        self.play(FadeOut(page), run_time=0.5)

        self.wait(1.5)

        quoteText = Text("\"Let me start by saying that \nwe are going to have so much fun!\"")
        quoteCredit = Text("- Melusi Mavuso")
        
        quoteCredit.scale(0.5)

        quote = VGroup(quoteText, quoteCredit)
        quote.arrange(DOWN, aligned_edge=RIGHT, buff=0.2)

        self.play(Write(quote.submobjects[0]))
        self.wait(2)
        self.play(Create(quote.submobjects[1]), run_time=1)
        self.wait(6)
        self.play(FadeOut(quote), run_time=0.5)

        self.wait(1.5)

        RVdefinition1 = Paragraph(
            "Let X be a function that assigns a number",
            "to each outcome of a random event."
        )

        RVdefinition2 = Text("We'll call this a Random Variable.")
        RVdefinition2.scale(1.1)

        RVdefinition = VGroup(RVdefinition1, RVdefinition2)
        RVdefinition.arrange(DOWN, buff=1 , aligned_edge=LEFT)

        self.play(Write(RVdefinition.submobjects[0]))
        self.wait(2)
        self.play(Write(RVdefinition.submobjects[1]), run_time=0.5)
        self.wait(5)
        self.play(FadeOut(RVdefinition), run_time=0.5)
        self.wait(5)