from dataHandler import extract_info, write_csv
import pysubs2

def main():
    srt_file = input("please enter the .srt file: ")
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

if __name__ == "__main__":
    main()
