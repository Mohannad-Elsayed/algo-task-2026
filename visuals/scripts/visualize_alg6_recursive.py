from manim import *

class DivideAndConquer(Scene):
    def construct(self):
        # Specific case where left and right halves dominators are completely different
        A = [2, 2, 2, 1, 1, 1, 1, 1]

        title = Text("Divide and Conquer Dominator", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        def create_array_mobj(arr):
            boxes = VGroup()
            for i, val in enumerate(arr):
                box = Square(side_length=0.5).set_fill(BLUE, opacity=0.3)
                num = Text(str(val), font_size=20).move_to(box.get_center())
                group = VGroup(box, num)

                if i > 0:
                    group.next_to(boxes[-1], RIGHT, buff=0)
                boxes.add(group)

            boxes.move_to(ORIGIN)
            return boxes

        def animate_recursive(arr, depth, target_pos, parent_mobj=None):
            arr_mobj = create_array_mobj(arr)
            
            if parent_mobj is None:
                arr_mobj.move_to(target_pos)
                self.play(FadeIn(arr_mobj), run_time=0.5)
            else:
                arr_mobj.move_to(parent_mobj.get_center())
                self.play(arr_mobj.animate.move_to(target_pos), run_time=0.4)

            if len(arr) == 1:
                result_text = Text(str(arr[0]), font_size=20, color=RED).next_to(arr_mobj, DOWN, buff=0.1)
                self.play(Write(result_text), run_time=0.3)
                return arr[0], arr_mobj, result_text

            mid = len(arr) // 2
            left_arr = arr[:mid]
            right_arr = arr[mid:]

            y_offset = target_pos[1] - 1.2
            x_shift = 3.5 / (2 ** depth)

            left_pos = [target_pos[0] - x_shift, y_offset, 0]
            right_pos = [target_pos[0] + x_shift, y_offset, 0]

            l_line = Line(arr_mobj.get_bottom(), np.array(left_pos) + np.array([0, 0.25, 0]))
            r_line = Line(arr_mobj.get_bottom(), np.array(right_pos) + np.array([0, 0.25, 0]))
            self.play(Create(l_line), Create(r_line), run_time=0.3)

            left_val, l_mobj, l_text = animate_recursive(left_arr, depth+1, left_pos, arr_mobj)
            right_val, r_mobj, r_text = animate_recursive(right_arr, depth+1, right_pos, arr_mobj)

            self.play(
                Indicate(l_text, color=YELLOW),
                Indicate(r_text, color=YELLOW),
                run_time=0.4
            )

            # Richification: Visually highlight the matching boxes and track counting
            info_text = Text(f"Candidates L:{left_val}, R:{right_val}", font_size=18, color=YELLOW)
            info_text.next_to(arr_mobj, UP, buff=0.1)
            self.play(Write(info_text), run_time=0.4)

            candidate = "None"
            left_count = 0
            right_count = 0

            # Scan for left candidate if it's not None
            if left_val != "None":
                self.play(Transform(info_text, Text(f"Counting L: {left_val}", font_size=18, color=YELLOW).next_to(arr_mobj, UP, buff=0.1)), run_time=0.3)
                for i, x in enumerate(arr):
                    if x == left_val:
                        self.play(arr_mobj[i][0].animate.set_fill(GREEN, opacity=0.7), run_time=0.1)
                        left_count += 1
                if left_count > len(arr) // 2:
                    candidate = left_val
                # Reset
                for i, x in enumerate(arr):
                    self.play(arr_mobj[i][0].animate.set_fill(BLUE, opacity=0.3), run_time=0.05)

            # Scan for right candidate if it's not None and we don't already have a valid candidate
            if right_val != "None" and candidate == "None":
                self.play(Transform(info_text, Text(f"Counting R: {right_val}", font_size=18, color=YELLOW).next_to(arr_mobj, UP, buff=0.1)), run_time=0.3)
                for i, x in enumerate(arr):
                    if x == right_val:
                        self.play(arr_mobj[i][0].animate.set_fill(GREEN, opacity=0.7), run_time=0.1)
                        right_count += 1
                if right_count > len(arr) // 2:
                    candidate = right_val
                # Reset
                for i, x in enumerate(arr):
                    self.play(arr_mobj[i][0].animate.set_fill(BLUE, opacity=0.3), run_time=0.05)

            self.play(FadeOut(info_text), run_time=0.2)

            if candidate != "None":
                matches = VGroup(*[arr_mobj[i][0] for i, x in enumerate(arr) if x == candidate])
                if len(matches) > 0:
                    self.play(matches.animate.set_fill(GREEN, opacity=0.7), run_time=0.4)

            result_text = Text(str(candidate), font_size=24, color=RED).next_to(arr_mobj, UP, buff=0.1)
            self.play(Write(result_text), run_time=0.4)
            
            # Collapse lower branches to keep screen neat and emphasize the recursive stack resolution
            self.play(
                FadeOut(l_mobj), FadeOut(l_text), 
                FadeOut(r_mobj), FadeOut(r_text),
                FadeOut(l_line), FadeOut(r_line),
                run_time=0.4
            )

            return candidate, arr_mobj, result_text

        root_pos = [0, 2.5, 0]
        final_candidate, root_mobj, root_result = animate_recursive(A, 0, root_pos)

        final_box = SurroundingRectangle(root_result, color=GREEN)
        self.play(Create(final_box))

        final_msg = Text(f"Final Dominator is {final_candidate}", font_size=30, color=GREEN)
        final_msg.to_edge(DOWN)
        self.play(Write(final_msg))

        self.wait(3)
