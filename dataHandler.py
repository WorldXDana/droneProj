import csv
import re
import pysubs2

def extract_info(subtitles):
    headers = ["Timestamp", "SS", "ISO", "EV", "DZOOM", "GPS_LON [°]", "GPS_LAT [°]", "GPS_ALT", "D [m]", "H [m]", "H.S [m/s]", "V.S [m/s]"]
    full_values = []
    na_values = []
    clean_values = []

    for subtitle in subtitles:
        num = 0 
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
        
        # Separate regular expression for H [m] to avoid conflicts
        h_match = re.search(r"H ([^m]+)m", text)
        h = h_match.group(1) if h_match else "n/a"
        
        hs = re.search(r"H.S ([^m/s]+)m/s", text).group(1)
        vs = re.search(r"V.S ([^m/s]+)m/s", text).group(1)

        row = [str(timestamp), ss, iso, ev, dzoom, gps_lon, gps_lat, gps_alt, d, h, hs, vs]
        print(row)
        full_values.append(row)

        if "n/a" in row:
            na_values.append(row)
        else:
            clean_values.append(row)
        num = num + 1

    return headers, full_values, na_values, clean_values
   
def write_csv(headers, values, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(values)

srt_file = "subtitles.srt"

subtitles = pysubs2.load(srt_file)

headers, full_values, na_values, clean_values = extract_info(subtitles)

full_csv_file = "subtitles_full.csv"
na_csv_file = "subtitles_na.csv"
clean_csv_file = "subtitles_clean.csv"

write_csv(headers, full_values, full_csv_file)
write_csv(headers, na_values, na_csv_file)
write_csv(headers, clean_values, clean_csv_file)

print(f"Created full CSV file: {full_csv_file}")
print(f"Created na CSV file: {na_csv_file}")
print(f"Created clean CSV file: {clean_csv_file}")
