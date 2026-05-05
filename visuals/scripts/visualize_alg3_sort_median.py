from manim import *

class SortAndMedian(Scene):
    def construct(self):
        A_unsorted = [3, 4, 3, 2, 3, -1, 3, 3]
        A = sorted(A_unsorted)
        n = len(A)
        mid = n // 2
        threshold = n // 2

        title = Text("Sort and Check Median", font_size=36).to_edge(UP)
        self.play(Write(title))

        def create_array(arr):
            boxes = VGroup()
            for val in arr:
                box = Square(side_length=0.7).set_fill(BLUE, opacity=0.3)
                num = Text(str(val), font_size=24).move_to(box.get_center())
                group = VGroup(box, num)
                boxes.add(group)
            boxes.arrange(RIGHT, buff=0)
            return boxes

        # 1. Unsorted array
        boxes = create_array(A_unsorted).move_to(ORIGIN)
        self.play(FadeIn(boxes))
        self.wait(0.5)

        # 2. Sort animation
        step_text = Text("1. Sort the Array", font_size=24).next_to(boxes, UP)
        self.play(Write(step_text))
        
        sorted_boxes = create_array(A).move_to(ORIGIN)
        self.play(Transform(boxes, sorted_boxes), run_time=1.5)
        self.wait(1)

        # 3. Calculate Median
        med_text = Text(f"2. Find Median: length = {n}, index = {n} // 2 = {mid}", font_size=24).next_to(boxes, UP)
        self.play(Transform(step_text, med_text))
        
        # Point to median
        med_arrow = Arrow(start=DOWN, end=UP, color=YELLOW, buff=0.1).scale(0.5)
        med_arrow.next_to(boxes[mid], DOWN)
        med_label = Text(f"Candidate = {A[mid]}", font_size=20, color=YELLOW).next_to(med_arrow, DOWN)
        
        self.play(FadeIn(med_arrow), Write(med_label))
        self.play(boxes[mid][0].animate.set_fill(YELLOW, opacity=0.8), run_time=0.5)
        self.wait(1)

        candidate = A[mid]

        # 4. Count phase
        count_title = Text("3. Count Occurrences of Candidate", font_size=24).next_to(boxes, UP)
        self.play(Transform(step_text, count_title))
        
        counter = 0
        count_display = Text(f"Count: {counter} / {threshold}", font_size=28).to_edge(DOWN)
        self.play(Write(count_display))

        scan_arrow = Arrow(start=UP, end=DOWN, color=RED, buff=0.1).scale(0.5)
        scan_arrow.next_to(boxes[0], UP)
        self.play(FadeIn(scan_arrow))

        for i in range(n):
            self.play(scan_arrow.animate.next_to(boxes[i], UP), run_time=0.3)
            if A[i] == candidate:
                boxes[i][0].set_stroke(GREEN, width=4)
                boxes[i][0].set_fill(GREEN, opacity=0.5)
                self.wait(0.1)
                counter += 1
                self.play(Transform(count_display, Text(f"Count: {counter} / {threshold}", font_size=28).to_edge(DOWN)), run_time=0.2)
            else:
                boxes[i][0].set_fill(RED, opacity=0.5)
                self.wait(0.1)
                boxes[i][0].set_fill(BLUE, opacity=0.3)

        if counter > threshold:
            res = Text(f"Count > {threshold}. Dominator is {candidate}!", font_size=32, color=GREEN).next_to(count_display, UP)
            self.play(Write(res))
        
        self.wait(2)
