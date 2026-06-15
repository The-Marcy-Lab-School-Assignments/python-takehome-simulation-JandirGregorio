import csv

requests = []

with open('nyc_311_requests.csv') as f:
  reader = csv.DictReader(f)
  for row in reader:
    requests.append(row)

# How many requests are currently open?
num_open_requests = 0
for request in requests:
  if request['resolution_status'] == 'Open':
    num_open_requests += 1

# What is the most common complaint type?

complaint_counter = {}

for request in requests:
  complaint = request['complaint_type']
  complaint_counter[complaint] = complaint_counter.get(complaint, 0) + 1

most_common = max(complaint_counter, key=lambda k: complaint_counter[k])
most_common_count = complaint_counter[most_common]

# How many requests were submitted per borough?

requests_per_borough = {}

for request in requests:
  borough = request['borough']
  requests_per_borough[borough] = requests_per_borough.get(borough, 0) + 1

sorted_boroughs = sorted(requests_per_borough.items())

with open('output.txt', 'w') as f:
  f.write(f'Open requests: {num_open_requests}\n')
  f.write('\n')
  f.write(f'Most common complaint type: {most_common} ({most_common_count} requests)\n')
  f.write('\n')
  f.write('Requests per borough:\n')
  for br, count in sorted_boroughs:
    f.write(f'- {br}: {count}\n')

print('Output saved to output.txt')

