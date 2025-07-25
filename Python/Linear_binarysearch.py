import numpy as np
salaries = np.array([35000, 45000, 50000, 60000, 75000, 80000, 95000])
target=75000

# linear search
for i in range(len(salaries)):
    if salaries[i]==target:
        print(f"From linear search: The number is {i+1} position in the array.")

#binary search

#binary search only works on sorted arrays
sorted_salaries=np.sort(salaries)

low=0    #Starting index
high=len(sorted_salaries)-1     #Ending index


while low<=high:
    mid=(low+high)//2   #we want a mid value

    if sorted_salaries[mid]==target:
        print(f"From binary search: The target is at {mid+1} position.")
        break

    elif sorted_salaries[mid]>target:
        #Target lies in the left half
        high=mid-1

    else:
        #Target lies in the right half
        low=mid+1



    

        




