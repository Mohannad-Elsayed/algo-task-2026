from manim import *

class BoyerMoore(Scene):
    def construct(self):
        A = [3, 4, 3, 2, 3, -1, 3, 3]
        threshold = len(A) // 2

        title = Text("Boyer-Moore Dominator", font_size=36).to_edge(UP)
        self.play(Write(title))

        # 1. Array Construction
        boxes = VGroup()
        for val in A:
            box = Square(side_length=0.6).set_fill(BLUE, opacity=0.3)
            num = Text(str(val), font_size=20).move_to(box.get_center())
            group = VGroup(box, num)
            boxes.add(group)
        boxes.arrange(RIGHT, buff=0).shift(UP * 1.5 + LEFT * 1.5)
        
        self.play(FadeIn(boxes))

        # Pointer setup
        pointer = Arrow(UP, DOWN, color=RED, buff=0.1).scale(0.5)
        pointer.next_to(boxes[0], UP)
        self.play(FadeIn(pointer))

        # 2. Dynamic Ball setup (Left/Center bottom)
        ball_base_y = -2.5
        ball = Circle(radius=0.5, color=YELLOW, fill_opacity=0.5).move_to(LEFT * 4 + UP * ball_base_y)
        cand_text = Text("None", font_size=20).move_to(ball.get_center())
        ball_group = VGroup(ball, cand_text)
        
        cand_label = Text("Candidate", font_size=20, color=YELLOW).next_to(ball, UP)
        cand_label.add_updater(lambda m: m.next_to(ball_group, UP))
        self.play(FadeIn(ball_group), Write(cand_label))

        count_tracker = 0
        count_label = Text("Count: 0", font_size=24).move_to(LEFT * 4 + DOWN * 3.3)
        self.play(Write(count_label))

        # 3. Discarded Pairs section (Right)
        pairs_title = Text("Discarded Pairs:", font_size=24, color=RED).to_edge(RIGHT).shift(UP * 1.5 + LEFT * 0.5)
        self.play(Write(pairs_title))
        pairs_group = VGroup()

        # Phases
        phase_text = Text("Phase 1: Find Candidate", font_size=24, color=YELLOW).to_edge(DOWN)
        self.play(Write(phase_text))

        candidate_val = None

        # -- Phase 1 Execution --
        for i, val in enumerate(A):
            self.play(pointer.animate.next_to(boxes[i], UP), run_time=0.4)
            boxes[i][0].set_stroke(YELLOW, width=4)

            if count_tracker == 0:
                candidate_val = val
                count_tracker = 1
                new_text = Text(str(val), font_size=24).move_to(ball.get_center())
                self.play(
                    Transform(cand_text, new_text),
                    ball_group.animate.move_to(LEFT * 4 + UP * (ball_base_y + count_tracker * 0.6)),
                    run_time=0.5
                )
            elif candidate_val == val:
                count_tracker += 1
                self.play(
                    ball_group.animate.move_to(LEFT * 4 + UP * (ball_base_y + count_tracker * 0.6)),
                    run_time=0.5
                )
            else:
                # Pair logic
                count_tracker -= 1
                pair_entry = Text(f"({candidate_val}, {val})", font_size=20)
                if len(pairs_group) == 0:
                    pair_entry.next_to(pairs_title, DOWN, buff=0.3).align_to(pairs_title, LEFT)
                else:
                    pair_entry.next_to(pairs_group[-1], DOWN, buff=0.2).align_to(pairs_title, LEFT)
                
                pairs_group.add(pair_entry)
                
                self.play(
                    ball_group.animate.move_to(LEFT * 4 + UP * (ball_base_y + count_tracker * 0.6)),
                    Write(pair_entry),
                    run_time=0.5
                )
                
                if count_tracker == 0:
                    new_text = Text("None", font_size=20).move_to(ball.get_center())
                    self.play(Transform(cand_text, new_text), run_time=0.2)
                    candidate_val = None

            self.play(Transform(count_label, Text(f"Count: {count_tracker}", font_size=24).move_to(LEFT * 4 + DOWN * 3.3)), run_time=0.2)
            boxes[i][0].set_stroke(WHITE, width=2)

        # -- Phase 2 Execution --
        self.play(Transform(phase_text, Text("Phase 2: Validation Pass", font_size=24, color=GREEN).to_edge(DOWN)))
        candy_copy = candidate_val
        val_count = 0
        
        val_label = Text(f"Validation: 0 / {threshold}", font_size=24, color=GREEN).next_to(phase_text, UP)
        self.play(Write(val_label))
        
        self.play(pointer.animate.next_to(boxes[0], UP))

        for i, val in enumerate(A):
            self.play(pointer.animate.next_to(boxes[i], UP), run_time=0.2)
            if val == candy_copy:
                boxes[i][0].set_fill(GREEN, opacity=0.6)
                val_count += 1
                self.play(Transform(val_label, Text(f"Validation: {val_count} / {threshold}", font_size=24, color=GREEN).next_to(phase_text, UP)), run_time=0.2)
            else:
                boxes[i][0].set_fill(RED, opacity=0.6)
                self.wait(0.1)
                boxes[i][0].set_fill(BLUE, opacity=0.3)

        if val_count > threshold:
            final_res = Text(f"Boyer-Moore Dominator: {candy_copy}!", font_size=32, color=GREEN).to_edge(DOWN)
            self.play(FadeOut(phase_text), FadeOut(val_label), Write(final_res))
            self.play(ball.animate.set_color(GREEN), ball.animate.scale(1.5))

        self.wait(2)
