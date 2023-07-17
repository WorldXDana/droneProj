import csv
import re
import pysubs2

def extract_info(subtitles):
    headers = ["Timestamp", "SS", "ISO", "EV", "DZOOM", "GPS_LON [°]", "GPS_LAT [°]", "GPS_ALT", "D [m]", "H [m]", "H.S [m/s]", "V.S [m/s]"]
    values = []

    for subtitle in subtitles:
        text = subtitle.text

        timestamp = subtitle.start
        ss = re.search(r"SS (\d+\.\d+)", text).group(1)
        iso = re.search(r"ISO (\d+)", text).group(1)
        ev = re.search(r"EV ([+-]?\d+\.\d+)", text).group(1)
        dzoom = re.search(r"DZOOM (\d+\.\d+)", text).group(1)
        gps = re.search(r"GPS \(([^)]+)\)", text).group(1).split(", ")
        gps_lon = gps[0]
        gps_lat = gps[1]
        gps_alt = gps[2]
        d = re.search(r"D ([^m]+)", text).group(1)
        h = re.search(r"H ([^m]+)", text).group(1)
        hs = re.search(r"H.S ([^m/s]+)", text).group(1)
        vs = re.search(r"V.S ([^m/s]+)", text).group(1)

        row = [str(timestamp), ss, iso, ev, dzoom, gps_lon, gps_lat, gps_alt, d, h, hs, vs]
        values.append(row)

    return headers, values

def write_csv(headers, values, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(values)

def write_text(text, txt_file):
    with open(txt_file, 'w') as file:
        file.write(text)

srt_file = "subtitles.srt"
csv_file = "subtitles.csv"
txt_file = "info.txt"

subtitles = pysubs2.load(srt_file)
text = "\n".join([subtitle.text for subtitle in subtitles])

headers, values = extract_info(subtitles)
write_csv(headers, values, csv_file)
write_text(text, txt_file)

print(f"Converted SRT to CSV: {csv_file}")
print(f"Created TXT file: {txt_file}")
