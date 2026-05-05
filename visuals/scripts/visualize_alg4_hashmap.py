from manim import *

class HashMapDominator(Scene):
    def construct(self):
        A = [45, 92, 45, 23, 45, 45, 81, 45]
        threshold = len(A) // 2

        title = Text("Hash Map / Dictionary Dominator", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Array construction, shifted to the left
        boxes = VGroup()
        for val in A:
            box = Square(side_length=0.7).set_fill(BLUE, opacity=0.3)
            num = Text(str(val), font_size=24).move_to(box.get_center())
            group = VGroup(box, num)
            boxes.add(group)
        boxes.arrange(RIGHT, buff=0).move_to(LEFT * 2)
        
        self.play(FadeIn(boxes))

        # Hash map dynamic representation on the right
        map_title = Text("Frequency Map", font_size=28, color=YELLOW).to_edge(RIGHT).shift(UP * 1.5 + LEFT * 1)
        self.play(Write(map_title))

        map_group = VGroup()
        map_entries = {}
        
        pointer = Arrow(start=UP, end=DOWN, color=RED, buff=0.1).scale(0.5)
        pointer.next_to(boxes[0], UP)
        
        threshold_text = Text(f"Threshold: > {threshold}", font_size=24).to_edge(DOWN)
        self.play(FadeIn(pointer), Write(threshold_text))

        for i, val in enumerate(A):
            self.play(pointer.animate.next_to(boxes[i], UP), run_time=0.4)
            boxes[i][0].set_stroke(YELLOW, width=4)
            
            if val not in map_entries:
                # Create new entry in dictionary
                entry = Text(f"Key: {val}  ->  Count: 1", font_size=22)
                if len(map_group) == 0:
                    entry.next_to(map_title, DOWN, buff=0.5)
                else:
                    entry.next_to(map_group[-1], DOWN, buff=0.3)
                
                # Align left text entries with the title
                entry.align_to(map_title, LEFT)
                
                map_group.add(entry)
                self.play(FadeIn(entry), run_time=0.4)
                map_entries[val] = {"count": 1, "mob": entry}
            else:
                # Increment existing entry
                map_entries[val]["count"] += 1
                new_entry = Text(f"Key: {val}  ->  Count: {map_entries[val]['count']}", font_size=22)
                new_entry.move_to(map_entries[val]["mob"].get_left(), aligned_edge=LEFT)
                
                # Flash the entry sequence
                self.play(map_entries[val]["mob"].animate.set_color(GREEN), run_time=0.2)
                self.play(Transform(map_entries[val]["mob"], new_entry), run_time=0.4)
                map_entries[val]["mob"].set_color(WHITE)
            
            boxes[i][0].set_stroke(WHITE, width=2)
            
            if map_entries[val]["count"] > threshold:
                res = Text(f"Dominator {val} found!", font_size=32, color=GREEN).next_to(threshold_text, UP)
                self.play(Write(res))
                
                # Highlight the winning Map key-value pair and array element
                self.play(
                    map_entries[val]["mob"].animate.set_color(GREEN).scale(1.2),
                    boxes[i][0].animate.set_fill(GREEN, opacity=0.5)
                )
                break

        self.wait(2)
