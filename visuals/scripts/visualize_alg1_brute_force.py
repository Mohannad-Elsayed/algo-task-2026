from manim import *

class BruteForce(Scene):
    def construct(self):
        # Dominator is 3, threshold is 4. It starts showing up at index 3 (4th spot)
        A = [2, -1, 1, 3, 3, 3, 3, 3]
        threshold = len(A) // 2

        title = Text("Brute Force Dominator", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Function to generate array MObjects
        def create_array(arr):
            boxes = VGroup()
            for val in arr:
                box = Square(side_length=0.7).set_fill(BLUE, opacity=0.3)
                num = Text(str(val), font_size=24).move_to(box.get_center())
                group = VGroup(box, num)
                boxes.add(group)
            boxes.arrange(RIGHT, buff=0)
            return boxes

        # 1. Create two copies of the array
        boxes1 = create_array(A).move_to(UP * 1)
        boxes2 = create_array(A).move_to(DOWN * 1)

        label1 = Text("i (Outer)", font_size=20).next_to(boxes1, LEFT)
        label2 = Text("j (Inner)", font_size=20).next_to(boxes2, LEFT)

        self.play(FadeIn(boxes1), FadeIn(boxes2), Write(label1), Write(label2), run_time=2.0)

        # 2. Create the traversal arrows
        arrow1 = Arrow(start=UP, end=DOWN, color=YELLOW, buff=0.1).scale(0.5)
        arrow1.next_to(boxes1[0], UP)
        
        arrow2 = Arrow(start=DOWN, end=UP, color=RED, buff=0.1).scale(0.5)
        arrow2.next_to(boxes2[0], DOWN)

        # 3. Create the counter
        count_text = Text(f"Count: 0 / {threshold}", font_size=28).to_edge(DOWN)
        self.play(FadeIn(arrow1), FadeIn(arrow2), Write(count_text), run_time=2.0)

        # Traverse the arrays
        for i in range(len(A)):
            self.play(arrow1.animate.next_to(boxes1[i], UP), run_time=0.6)
            boxes1[i].set_color(YELLOW)
            
            count = 0
            # Cleanly transform the simple text object
            self.play(Transform(count_text, Text(f"Count: {count} / {threshold}", font_size=28).to_edge(DOWN)), run_time=0.2)
            
            for j in range(len(A)):
                self.play(arrow2.animate.next_to(boxes2[j], DOWN), run_time=0.2)
                
                # Detailed color flash showing match vs mismatch
                if A[i] == A[j]:
                    # Match
                    boxes2[j][0].set_fill(GREEN, opacity=0.8)
                    self.wait(0.1)
                    count += 1
                    self.play(Transform(count_text, Text(f"Count: {count} / {threshold}", font_size=28).to_edge(DOWN)), run_time=0.2)
                    boxes2[j][0].set_fill(BLUE, opacity=0.3)
                else:
                    # Mismatch
                    boxes2[j][0].set_fill(RED, opacity=0.8)
                    self.wait(0.1)
                    boxes2[j][0].set_fill(BLUE, opacity=0.3)
            
            boxes1[i].set_color(WHITE)
            
            # Check the threshold condition
            if count > threshold:
                res = Text(f"Dominator found at index {i} in outer array!", font_size=32, color=GREEN).next_to(count_text, UP)
                self.play(Write(res))
                
                # Emphasis on the final found element
                self.play(boxes1[i].animate.scale(1.2).set_stroke(GREEN, width=4))
                break
        
        self.wait(2)
