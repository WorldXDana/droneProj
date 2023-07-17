
from graph import graphPlot

def test_graphs():
    plotter = graphPlot('subtitles.csv')
    plotter.plot_distance_vs_time()
    plotter.plot_speed_vs_time()
    plotter.plot_altitude_vs_time()