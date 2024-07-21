# Create alarm clock using python
# seudo code:
# create a two inputs the input should 'What time you set alarm'. The second input is 'Write a description'.
# after inputting two inputs log message 'You've successfully save the alarm'
# The system should handle multiple alarms.

from datetime import datetime
import time

# List to store alarms
alarms = []

# Function to add a new alarm
def add_alarm():
    alarm_time = input('What time do you want to set the alarm (HH:MM): ')
    description = input('Write a description: ')
    
    # Validate and parse the alarm time
    try:
        alarm_time = datetime.strptime(alarm_time, '%H:%M').time()
    except ValueError:
        print('Invalid time format. Please use HH:MM format.')
        return
    
    # Save the alarm
    alarms.append({'time': alarm_time, 'description': description})
    print("You've successfully saved the alarm")

# Function to check alarms
def check_alarms():
    while True:
        current_time = datetime.now().time()
        for alarm in alarms:
            if alarm['time'].hour == current_time.hour and alarm['time'].minute == current_time.minute:
                print(f"Alarm! Time: {alarm['time']} Description: {alarm['description']}")
                # Remove the alarm after it goes off
                alarms.remove(alarm)
        time.sleep(60)  # Check every minute

# Main loop to add alarms
while True:
    add_alarm()
    more_alarms = input('Do you want to add another alarm? (yes/no): ')
    if more_alarms.lower() != 'yes':
        break

# Start checking for alarms
check_alarms()

