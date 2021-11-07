import csv
import time


def print_arr(arr):
    for line in arr:
        for elem in line:
            print(elem, end='\t')
        print()


def copy_2d_array(arr, only_structure=False, default_value=0):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append([])
        for elem in arr[i]:
            val = default_value if only_structure else elem
            new_arr[i].append(val)
    return new_arr


def get_min(arr):
    min_v = 0

    for elem in arr:
        if (min_v == 0 and elem) \
                or (elem and elem < min_v)\
                or (elem == 0 and elem < min_v):
            min_v = elem

    return min_v


def log_workload(
    cpus: int,
    time_range: int,
    field: list,
    best_schedule: list
):
    logfile = 'log.csv'
    with open(logfile, 'a+') as f:
        writer = csv.writer(f)
        writer.writerow([
            int(time.time()),
            cpus,
            time_range,
            field,
            best_schedule,
        ])
