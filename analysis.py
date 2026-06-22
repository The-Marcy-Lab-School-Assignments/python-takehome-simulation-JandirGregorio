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

# How many requests were submitted for each complaint type?

sorted_complaints = sorted(complaint_counter.items(), key=lambda item: item[1], reverse=True)

# Which borough has the most open requests?

open_by_borough = {}

for request in requests:
  if request['resolution_status'] == 'Open':
    borough = request['borough']
    open_by_borough[borough] = open_by_borough.get(borough, 0) + 1

most_open_borough = max(open_by_borough, key=lambda k: open_by_borough[k])
most_open_count = open_by_borough[most_open_borough]

# What is the closure rate for each borough?

closed_by_borough = {}

for request in requests:
  if request['resolution_status'] == 'Closed':
    borough = request['borough']
    closed_by_borough[borough] = closed_by_borough.get(borough, 0) + 1

closure_rates = {}
for borough, total in requests_per_borough.items():
  closed = closed_by_borough.get(borough, 0)
  closure_rates[borough] = (closed / total) * 100

sorted_closure_rates = sorted(closure_rates.items())

# What are the top 3 boroughs by total number of requests?

top_3_boroughs = sorted(requests_per_borough.items(), key=lambda item: (-item[1], item[0]))[:3]

with open('output.txt', 'w') as f:
  f.write(f'Open requests: {num_open_requests}\n')
  f.write('\n')
  f.write(f'Most common complaint type: {most_common} ({most_common_count} requests)\n')
  f.write('\n')
  f.write('Requests per borough:\n')
  for br, count in sorted_boroughs:
    f.write(f'- {br}: {count}\n')
  f.write('\n')
  f.write('Requests by complaint type:\n')
  for complaint, count in sorted_complaints:
    f.write(f'- {complaint}: {count}\n')
  f.write('\n')
  f.write(f'Borough with most open requests: {most_open_borough} ({most_open_count} open)\n')
  f.write('\n')
  f.write('Closure rate by borough:\n')
  for borough, rate in sorted_closure_rates:
    f.write(f'- {borough}: {rate:.1f}%\n')
  f.write('\n')
  f.write('Top 3 boroughs by total requests:\n')
  for i, (borough, count) in enumerate(top_3_boroughs, 1):
    f.write(f'{i}. {borough} ({count} requests)\n')

print('Output saved to output.txt')

