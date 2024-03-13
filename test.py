


# import uuid 
# print(uuid.uuid4().hex)

from csvFunc import WorkoutData

csvList = WorkoutData()

# for csvList in csvList:

#     print(f"{csvList.duration}")  # this code runs

    
# print(f"{csvList[0].duration}") # this code also runs.
print(f"{csvList.duration[0]}")
