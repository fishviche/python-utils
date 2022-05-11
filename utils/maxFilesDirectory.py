import sys
import os



UPLOAD_ROUTE ='../uploads/images'

count = 0
def select_max():
    """
    Function to select max number of directories
    """
    list_dir = []
    [list_dir.append(dirs) for root, dirs, files in os.walk(UPLOAD_ROUTE)]
    print(list_dir)
    if len(list_dir[0])==0:
        max_number=0
        return max_number
    list_number = []
    for list_d in list_dir[0]:
        count = int(list_d.split('_')[1])
        list_number.append(count)
    list_number.sort()
    max_number = list_number[-1]
    return max_number

if __name__ == "__main__":
    max_number = select_max()
    print(max_number)