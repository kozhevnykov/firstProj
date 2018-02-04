import csv
import re

ans={}

with open("Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if re.findall(".*/2015.*",row[2]):
            if row[5] not in ans.keys():
                ans[row[5]] = 1
            ans[row[5]] += 1
print(max(ans.values()))
