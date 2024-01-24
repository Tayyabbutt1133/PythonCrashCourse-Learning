import time

# Get the current local time
current_time = time.localtime()

# Format the time in 12-hour format
formatted_time = time.strftime("%I:%M:%S %p", current_time)

print("Current time in 12-hour format:", formatted_time)


if(formatted_time>8):
    print("Good Morning")
elif(formatted_time>2):
    print("Good Evening")
elif(formatted_time>8):
    print("Good Night")