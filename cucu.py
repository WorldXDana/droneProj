import csv
import re
import pysrt

def srt_to_text(srt_file):
    subs = pysrt.open(srt_file)
    text = ""
    for sub in subs:
        text += sub.text_without_tags + " "
    return text.strip()

def extract_info(text):
    headers = ["SS", "ISO", "EV", "DZOOM", "GPS", "D", "H", "H.S", "V.S"]
    pattern = r"SS (\d+\.\d+), ISO (\d+), EV ([+-]?\d+\.\d+), DZOOM (\d+\.\d+), GPS \(([^)]+)\), D ([^m]+)m, H ([^m]+)m, H.S ([^m/s]+)m/s, V.S ([^m/s]+)m/s"
    matches = re.findall(pattern, text)
    values = [list(match) for match in matches]
    return headers, values

def write_csv(headers, values, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(values)

def write_text(text, txt_file):
    with open(txt_file, 'w') as file:
        file.write(text)

srt_file = "flight3.srt"
csv_file = "subtitle3.csv"
txt_file = "info3.txt"

text = srt_to_text(srt_file)
headers, values = extract_info(text)

write_csv(headers, values, csv_file)
write_text(text, txt_file)

print(f"Converted SRT to CSV: {csv_file}")
print(f"Created TXT file: {txt_file}")
