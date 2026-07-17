from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, show
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns

# 1. Shared Data Setup
x = np.linspace(0, 10, 100)
y = np.sin(x)

# ==========================================
# PART 1: Matplotlib (Static Base Plot)
# ==========================================
plt.figure(figsize=(7, 4))
plt.plot(x, y, label="Sine Wave", color="blue", linewidth=2)
plt.title("Matplotlib: Static Sine Wave", fontsize=14)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

print("Displaying Matplotlib plot... (Close window to proceed to Seaborn)")
plt.show()

# ==========================================
# PART 2: Seaborn (Styled Statistical Plot)
# ==========================================
sns.set_theme(style="darkgrid")
plt.figure(figsize=(7, 4))

sns.lineplot(x=x, y=y, color="crimson", label="Sine Wave", linewidth=2.5)
plt.title("Seabornfig = px.line(x=x, y=y, labels={'x': 'X Axis', 'y': 'Y Axis'},
              title="Plotly: Interactive Sine Wave (Hover & Zoom)")

print("Opening Plotly interactive plot in your web browser... (Then return to terminal)")
fig.show()

output_file("bokeh_plot.html")

p = figure(
    title="Bokeh: Interactive Sine Wave",
    x_axis_label="X Axis",
    y_axis_label="Y Axis",
    tools="pan,wheel_zoom,box_zoom,reset,save",
)

p.line(x, y, legend_label="Sine", line_width=3, color="navy")
p.add_tools(HoverTool(tooltips=[("X", "$x"), ("Y", "$y")]))

print("Opening Bokeh interactive plot in your web browser...")
show(p)