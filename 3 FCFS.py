def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = processes[i-1][1] + waiting_time[i-1]

    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

    return waiting_time, turnaround_time

def sjf(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sort by burst time

    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = processes[i-1][1] + waiting_time[i-1]

    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

    return waiting_time, turnaround_time

def priority_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[2])  # Sort by priority

    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = processes[i-1][1] + waiting_time[i-1]

    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

    return waiting_time, turnaround_time

def round_robin(processes, quantum):
    n = len(processes)
    remaining_burst_time = [process[1] for process in processes]
    waiting_time = [0] * n
    time = 0  # Current time

    while True:
        done = True

        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False

                if remaining_burst_time[i] > quantum:
                    time += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    time += remaining_burst_time[i]
                    waiting_time[i] = time - processes[i][1]
                    remaining_burst_time[i] = 0

        if done:
            break

    turnaround_time = [waiting_time[i] + processes[i][1] for i in range(n)]

    return waiting_time, turnaround_time

def print_result(processes, waiting_time, turnaround_time):
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    avg_waiting_time = sum(waiting_time) / len(waiting_time)
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f} ms")


def main():
    n = int(input("Enter the number of processes: "))
    processes = []

    for i in range(n):
        pid = input(f"Enter process ID for process {i+1}: ")
        bt = int(input(f"Enter burst time for process {pid}: "))
        ar = int(input(f"Enter arrival time for process {pid}: "))
        pr = 0
        if i > 0:
            pr = int(input(f"Enter priority for process {pid} (only if Priority Scheduling, otherwise enter 0): "))
        processes.append((pid, bt, pr, ar))
    
    print("\nSelect Scheduling Algorithm:")
    print("1. First-Come, First-Served (FCFS)")
    print("2. Shortest Job First (SJF)")
    print("3. Priority Scheduling")
    print("4. Round Robin")
    
    choice = int(input("Enter choice (1/2/3/4): "))

    if choice == 1:
        waiting_time, turnaround_time = fcfs(processes)
    elif choice == 2:
        waiting_time, turnaround_time = sjf(processes)
    elif choice == 3:
        waiting_time, turnaround_time = priority_scheduling(processes)
    elif choice == 4:
        quantum = int(input("Enter time quantum: "))
        waiting_time, turnaround_time = round_robin(processes, quantum)
    else:
        print("Invalid choice!")
        return

    print_result(processes, waiting_time, turnaround_time)

if __name__ == "__main__":
    main()
