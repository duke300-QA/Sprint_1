time = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0
times = time.replace(',', ' ').split()
for time in times:
    if 'h' in time:
        total_minutes += int(time.replace('h', '')) * 60
    elif 'm' in time:
        total_minutes += int(time.replace('m', ''))
    elif 's' in time:
        total_minutes += int(time.replace('s', '')) // 60
print(total_minutes)
