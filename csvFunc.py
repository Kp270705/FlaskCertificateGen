# data validation creating objects of each row of csv file:- 

import csv

class Workout:
    def __init__(self, duration, pulse, maxpulse, calories):

        self.calories = calories
        self.pulse=pulse
        self.maxpulse=maxpulse
        self.duration=duration
        
csv_file_path="/mnt/Common Drive/programming/Python D/Python frameworks/Flask for Ubuntu/flaskTut/csvUploads/data.csv"
workout_data=[]
i=0


def WorkoutData():
    csvData=[]
    csvData = workout_data
    return csvData

with open(csv_file_path, 'r') as file:
    csv_reader=csv.DictReader(file)
    
    for row in csv_reader:
        
        # removing Nan values from '0.0'
        duration = float(row["Duration"]) if row["Duration"] else 0.0
        pulse=float(row["Pulse"]) if row["Pulse"] else 0.0
        maxpulse=float(row["Maxpulse"]) if row["Maxpulse"] else 0.0
        calories=float(row["Calories"]) if row["Calories"] else 0.0
        
        workout_obj= Workout(duration, pulse, maxpulse, calories)
        workout_data.append(workout_obj)
        
# WorkoutData()

# print(f"{workout_data.calories}, {workout_data.pulse}, {workout_data.maxpulse}, {workout_data.duration}")
    
    
# =============================================================================================

# print(f"Enter the range from which you want to print your list:")
# low_val=int(input("\n Enter the lower value: "))
# high_val=int(input("\n Enter the higher value: "))


# for wrkData in workout_data[(low_val-1):(high_val)]:
#     i+=1
#     index=low_val
#     print(f"\n--------------------------------\nRow{low_val}:\nNo of calories: {wrkData.calories},\nNo. of pulse: {wrkData.pulse}, \nNo. of maxpulse: {wrkData.maxpulse}, \nNo. of duration: {wrkData.duration} \n--------------------------------")

#     low_val+=1
    
    
    