import sys

items = {}

for arg in sys.argv[1:]:
    with open(arg, "r") as f:
        for entry in f:
            entry = entry.rstrip()
            if not entry:
                continue
            try:
                items[entry] += 1
            except KeyError as e:
                items[entry] = 0

duplicates = []
for key, val in items.items():
    if val > 0:
        duplicates.append(key)

print("Total entries: {} | Total Duplicates: {} | Percent Duplicated: {}".
      format(len(items), len(duplicates), int((len(duplicates) + 1)/len(items))))
