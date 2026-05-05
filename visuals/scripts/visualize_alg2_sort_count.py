from manim import *

class SortAndCount(Scene):
    def construct(self):
        A_unsorted = [3, -1, 3, 1, 2, 3, 3, 3]
        A = sorted(A_unsorted)
        threshold = len(A) // 2

        title = Text("Sort and Count Dominator", font_size=36).to_edge(UP)
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

        boxes = create_array(A_unsorted).move_to(ORIGIN)
        self.play(FadeIn(boxes))
        self.wait(1)

        # 1. Sort animation
        sorted_boxes = create_array(A).move_to(ORIGIN)
        sort_text = Text("1. Sort the Array", font_size=24).next_to(sorted_boxes, UP)
        self.play(Write(sort_text))
        self.play(Transform(boxes, sorted_boxes), run_time=1.5)
        self.wait(1)
        
        scan_text = Text("2. Scan with Two Pointers", font_size=24).next_to(sorted_boxes, UP)
        self.play(Transform(sort_text, scan_text))

        # 2. Pointers
        i_arrow = Arrow(start=DOWN, end=UP, color=YELLOW, buff=0.1).scale(0.5)
        j_arrow = Arrow(start=UP, end=DOWN, color=RED, buff=0.1).scale(0.5)

        i_label = Text("i (Start of run)", font_size=18, color=YELLOW).next_to(i_arrow, DOWN)
        j_label = Text("j (End of run)", font_size=18, color=RED).next_to(j_arrow, UP)

        i_group = VGroup(i_arrow, i_label)
        j_group = VGroup(j_arrow, j_label)

        # Place them initially off-screen or faded out
        i_group.next_to(boxes[0], DOWN)
        j_group.next_to(boxes[0], UP)

        count_text = Text(f"Window Count: 0 / {threshold}", font_size=28).to_edge(DOWN)
        self.play(FadeIn(i_group), FadeIn(j_group), Write(count_text))

        i = 0
        while i < len(A):
            self.play(i_group.animate.next_to(boxes[i], DOWN), run_time=0.5)
            boxes[i][0].set_stroke(YELLOW, width=4)
            
            j = i
            count = 0
            while j < len(A) and A[j] == A[i]:
                self.play(j_group.animate.next_to(boxes[j], UP), run_time=0.5)
                boxes[j][0].set_fill(GREEN, opacity=0.6)
                count += 1
                self.play(Transform(count_text, Text(f"Window Count: {count} / {threshold}", font_size=28).to_edge(DOWN)), run_time=0.2)
                
                if count > threshold:
                    res = Text(f"Dominator found: {A[i]}", font_size=32, color=GREEN).next_to(count_text, UP)
                    self.play(Write(res))
                    
                    window_box = SurroundingRectangle(boxes[i:j+1], color=YELLOW)
                    self.play(Create(window_box))
                    self.wait(3)
                    return
                j += 1
                
            # If we didn't hit the threshold, reset colors for the window that failed
            for k in range(i, j):
                boxes[k][0].set_fill(BLUE, opacity=0.3)
                boxes[k][0].set_stroke(WHITE, width=2)
            
            i = j
            
        self.wait(2)
