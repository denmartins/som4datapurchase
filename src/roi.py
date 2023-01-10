from dataclasses import dataclass
import matplotlib.patches as pat

@dataclass
class RegionOfInterest:
    x_lower: int
    y_lower: int
    x_upper: int 
    y_upper: int
    
    def contains(self, point) -> bool:
        x_condition = point[0] >= self.x_lower and point[0] <= self.x_upper
        y_condition = point[1] >= self.y_lower and point[1] <= self.y_upper
        return x_condition and y_condition
    
    def get_plt_rectangle(self):
        offset = 0.1
        rect = pat.Rectangle(
            (self.x_lower, self.y_lower),
            self.x_upper - self.x_lower,
            self.y_upper - self.y_lower,
            fc = 'none',
            color='lime',
            linewidth=1,)
        return rect