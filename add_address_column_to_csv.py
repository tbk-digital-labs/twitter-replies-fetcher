import csv
import re

outrow = []

with open("replies.csv", "r", encoding="utf-8") as fileIn:
    with open("replies_addresses.csv", "w", encoding="utf-8") as fileOut:
        writer = csv.writer(fileOut)
        reader = csv.reader(fileIn, delimiter=',')
        for row in reader:
            print(row)
            text = row[1]
            if re.search("0x[a-fA-F0-9]{40}", text):
                outrow.append(row[0])
                outrow.append(row[1])
                outrow.append(re.search("0x[a-fA-F0-9]{40}", text).group(0))
                writer.writerow(outrow)
                outrow = []
            else:
                outrow.append(row[0])
                outrow.append(row[1])
                outrow.append('')
                writer.writerow(outrow)
                outrow = []
