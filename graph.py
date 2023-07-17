import pandas as pd
import matplotlib.pyplot as plt

class graphPlot:
    def __init__(self, csv_file_path):
        self.data = pd.read_csv(csv_file_path)

    def plot_distance_vs_time(self):
        plt.plot(self.data['Timestamp']/1000, self.data['D [m]'])
        plt.xlabel('Timestamp')
        plt.ylabel('Distance (m)')
        plt.title('Distance vs. Time')
        plt.show()

    def plot_speed_vs_time(self):
        plt.plot(self.data['Timestamp'], self.data['H.S [m/s]'])
        plt.xlabel('Timestamp')
        plt.ylabel('Speed (m/s)')
        plt.title('Speed vs. Time')
        plt.show()

    def plot_altitude_vs_time(self):
        plt.plot(self.data['Timestamp'], self.data['H [m]'])
        plt.xlabel('Timestamp')
        plt.ylabel('Altitude (m)')
        plt.title('Altitude vs. Time')
        plt.show()


