from datetime import datetime


def TimeDateCur():

    now = datetime.now()  # Get the current date and time
    current_time = now.strftime('%Y-%m-%d %H:%M:%S') # Format the date and time 34-hrt fmt

    return current_time  # Example output: '2024-09-26 02:15:30 PM'
# def TD(curTime,Last_Seen):
#    # Parse the times to datetime objects
#    Greater_Time = datetime.strptime(curTime, '%Y-%m-%d %H:%M:%S')
#    Smaller_Time = datetime.strptime(Last_Seen, '%Y-%m-%d %H:%M:%S')

#    # Calculate the difference
#    time_difference = Greater_Time - Smaller_Time
#    time_obj = datetime.strptime(str(time_difference),'%H:%M:%S')
    

#    # Display the time difference
#    return (int(time_difference),time_obj)
 

# print(TD('2024-09-26 22:32:00','2024-09-26 22:28:15'))