
from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, show
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)


plt.figure(figsize=(7, 4))
plt.plot(x, y, label="Sine Wave", color="blue", linewidth=2)

plt.title("Static Sine Wave", fontsize=14)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True, linestyle="--", alpha=0.16)
plt.legend()

print("Displaying Matplotlib plot... (Close the window to proceed to Bokeh)")
plt.show()

output_file("bokeh_plot.html")


p = figure(
    title="Bokeh: Interactive Sine Wave",
    x_axis_label="X",
    y_axis_label="Y",
    tools="pan,wheel_zoom,box_zoom,reset,save",
)

p.line(x, y, legend_label="Sine", line_width=3, color="navy")

p.add_tools(HoverTool(tooltips=[("X", "$x"), ("Y", "$y")]))

print("Opening Bokeh interactive plot in your browser...")
show(p)