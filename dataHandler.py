import csv
import re
import pysubs2

def extract_info(subtitles):
    headers = ["Timestamp", "SS", "ISO", "EV", "DZOOM", "GPS_LON [°]", "GPS_LAT [°]", "GPS_ALT", "D [m]", "H [m]", "H.S [m/s]", "V.S [m/s]"]
    full_values = []
    na_values = []
    clean_values = []

    for subtitle in subtitles:
        text = subtitle.text

        timestamp = subtitle.start
        ss = re.search(r"SS (\d+\.\d+)", text).group(1)
        iso = re.search(r"ISO (\d+)", text).group(1)
        ev = re.search(r"EV ([+-]?\d+\.\d+)", text).group(1)
        dzoom = re.search(r"DZOOM (\d+\.\d+)", text).group(1)
        gps_data = re.search(r"GPS \(([^)]+)\)", text).group(1).split(", ")
        gps_lon = gps_data[0]
        gps_lat = gps_data[1]
        gps_alt = gps_data[2]
        d_match = re.search(r"D ([^m]+)m", text)
        d = d_match.group(1) if d_match else "n/a"
        h = re.search(r"H ([^m]+)m", text).group(1)
        hs = re.search(r"H.S ([^m/s]+)m/s", text).group(1)
        vs = re.search(r"V.S ([^m/s]+)m/s", text).group(1)

        row = [str(timestamp), ss, iso, ev, dzoom, gps_lon, gps_lat, gps_alt, d, h, hs, vs]
        full_values.append(row)

        if "n/a" in row:
            na_values.append(row)
        else:
            clean_values.append(row)

    return headers, full_values, na_values, clean_values
   
def write_csv(headers, values, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(values)