from manim import *
import numpy as np

class X(Scene):
    def construct(self):
        totalTrials = 2000
        X = np.random.normal(10, 9, totalTrials)

        title = Paragraph("Running a Simulation we can see what values x","from a given distribution X might take on:")
        title.scale(0.8)

        trial = Text("Trial = ").scale(1.1)  
        trialNumber = DecimalNumber(0, num_decimal_places=0).scale(1.5)  
        TrialGroup = VGroup(trial, trialNumber)
        TrialGroup.arrange(RIGHT, buff=0.7)


        sample= Text("X = ").scale(1.5)
        outcomeValue = DecimalNumber(X[0], num_decimal_places=0).scale(2).set_color(RED) 
        OutcomeGroup = VGroup(sample, outcomeValue)
        OutcomeGroup.arrange(RIGHT, buff=0.7)
        OutcomeGroup.color=RED
        
        pageGroup = VGroup(title, TrialGroup, OutcomeGroup)
        pageGroup.arrange(DOWN, buff=0.5)
        self.add(pageGroup.to_edge(UP, buff=0.1))

        

        # Loop for updating the trial number
        for i in range(1,11):
            new_trial_number = DecimalNumber(i, num_decimal_places=0).scale(1.5)  # Start from 1
            new_trial_number.move_to(trialNumber.get_center())  # Keep position consistent

            new_outcome_number = DecimalNumber(X[i], num_decimal_places=0 ).scale(2).set_color(RED) 
            new_outcome_number.move_to(outcomeValue.get_center())

            # Update trialNumber reference after transformation
            self.play(ReplacementTransform(trialNumber, new_trial_number), ReplacementTransform(outcomeValue, new_outcome_number), run_time=0.5)
            trialNumber = new_trial_number  
            outcomeValue = new_outcome_number 

            self.wait(1)

        final_text = Paragraph("The outcomes seem chaotic,","We must step back,","consider 1000s of samples").scale(1.2).next_to(OutcomeGroup, DOWN).set_color(BLUE)
        self.play(Write(final_text))

        for i in range(11,31):
            new_trial_number = DecimalNumber(i, num_decimal_places=0).scale(1.5)  # Start from 1
            new_trial_number.move_to(trialNumber.get_center())  # Keep position consistent

            new_outcome_number = DecimalNumber(X[i], num_decimal_places=0 ).scale(2).set_color(RED) 
            new_outcome_number.move_to(outcomeValue.get_center())

            # Update trialNumber reference after transformation
            self.play(ReplacementTransform(trialNumber, new_trial_number), ReplacementTransform(outcomeValue, new_outcome_number), run_time=0.2)
            trialNumber = new_trial_number  
            outcomeValue = new_outcome_number 

            self.wait(0.5)

        self.play(FadeOut(final_text))

        for i in range(31,51):
            new_trial_number = DecimalNumber(i, num_decimal_places=0).scale(1.5)  # Start from 1
            new_trial_number.move_to(trialNumber.get_center())  # Keep position consistent

            new_outcome_number = DecimalNumber(X[i], num_decimal_places=0 ).scale(2).set_color(RED) 
            new_outcome_number.move_to(outcomeValue.get_center())

            # Update trialNumber reference after transformation
            self.play(ReplacementTransform(trialNumber, new_trial_number), ReplacementTransform(outcomeValue, new_outcome_number), run_time=0.05)
            trialNumber = new_trial_number  
            outcomeValue = new_outcome_number 

            self.wait(0.2)

                # Create histogram bins (range -10 to 30, step = 1)
        bin_edges = np.arange(-10, 31, 1)
        histogram_values = np.zeros(len(bin_edges) - 1)  # Start empty

        # Create histogram
        histogram = BarChart(
            values=histogram_values,
            bar_names=[str(int(x)) for x in bin_edges[:-1]],
            y_range=[0, 100, 20],  # Max 50 frequency, increments of 10
            x_length=10,
            y_length=3,
            bar_width=0.3,
        ).to_edge(DOWN, buff=0.5)

        self.play(FadeIn(histogram))

        for i in range(51, totalTrials):
            # Update trial number and outcome value
            new_trial_number = DecimalNumber(i, num_decimal_places=0).scale(1.5)
            new_outcome_number = DecimalNumber(X[i], num_decimal_places=0).scale(2).set_color(RED)

            new_trial_number.move_to(trialNumber.get_center())
            new_outcome_number.move_to(outcomeValue.get_center())

            # Update histogram frequency
            bin_index = np.clip(np.digitize(X[i], bin_edges) - 1, 0, len(histogram_values) - 1)

            histogram_values[bin_index] += 1

            # Animate first 20 updates (51-70)
            if i <= 70:
                new_histogram = BarChart(
                    values=histogram_values,
                    bar_names=[str(int(x)) for x in bin_edges[:-1]],
                    y_range=[0, 100, 20],
                    x_length=10,
                    y_length=3,
                    bar_width=0.3,
                ).to_edge(DOWN, buff=0.5)

                self.play(
                    ReplacementTransform(trialNumber, new_trial_number),
                    ReplacementTransform(outcomeValue, new_outcome_number),
                    ReplacementTransform(histogram, new_histogram),
                    run_time=0.1,
                )
                histogram = new_histogram
                trialNumber = new_trial_number  
                outcomeValue = new_outcome_number
            else:  # Silent fast updates after 70 trials

                if i % 5 == 0:  # Update histogram every 5 frames
                    self.remove(trialNumber, outcomeValue)
                    self.add(new_trial_number, new_outcome_number)
                    new_histogram = BarChart(
                        values=histogram_values,
                        bar_names=[str(int(x)) for x in bin_edges[:-1]],
                        y_range=[0, 100, 20],
                        x_length=10,
                        y_length=3,
                        bar_width=0.3,
                    ).to_edge(DOWN, buff=0.5)

                    self.remove(histogram)
                    self.add(new_histogram)
                    histogram = new_histogram
                    trialNumber = new_trial_number  
                    outcomeValue = new_outcome_number
            self.wait(0.1 if i <= 70 else 0.01)  # Speed up later frames


        normalize = MathTex("X \\sim N(10, 3^2)").scale(1).next_to(OutcomeGroup, buff=0.8).set_color(RED)
        self.play(Write(normalize))
        self.wait(5)