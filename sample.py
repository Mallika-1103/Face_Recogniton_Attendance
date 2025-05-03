from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time with AM/PM
current_time = now.strftime('%Y-%m-%d %I:%M:%S %p')

print(current_time)  # Example output: '2024-09-26 02:15:30 PM'
