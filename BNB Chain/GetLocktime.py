import datetime

# Unix timestamp
timestamp = int(input("Enter unix timestamp: "))

# Convert the timestamp to a date
date = datetime.datetime.fromtimestamp(timestamp)

# Get the current date
current_date = datetime.datetime.now()

lock_date = f"{current_date:%d-%m-%Y %H:%M:%S}"

# Calculate the difference from current date
difference = date-current_date
locktime= difference.days
print(current_date)
print(locktime)
print("Tokens are locked till: ",lock_date)
print("Months Lock",locktime//30)
print("Years Lock",locktime//365)
