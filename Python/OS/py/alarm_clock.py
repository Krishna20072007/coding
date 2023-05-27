import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            # Play a sound (Windows only)
            winsound.Beep(440, 1000)  # frequency, duration in milliseconds
            break
        time.sleep(1)

# Set the alarm time
alarm_time = input("Enter the alarm time in HH:MM:SS format: ")

set_alarm(alarm_time)
