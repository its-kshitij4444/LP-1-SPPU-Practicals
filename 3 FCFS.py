# Function to implement First Come First Served (FCFS)
def fcfs_scheduling(n, arrival_time, burst_time):
    waiting_time = [0] * n
    total_waiting_time = 0

    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = max(waiting_time[i-1] + burst_time[i-1], arrival_time[i-1] + burst_time[i-1]) - arrival_time[i]

    # Calculate total waiting time
    total_waiting_time = sum(waiting_time)

    # Calculate average waiting time
    avg_waiting_time = total_waiting_time / n

    # Display results
    print("\nProcess | Arrival Time | Burst Time | Waiting Time")
    for i in range(n):
        print(f"P{i+1}\t\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")

# User input
n = int(input("Enter the number of processes: "))
arrival_time = []
burst_time = []

for i in range(n):
    print(f"\nProcess {i+1}:")
    arrival_time.append(int(input(f"Enter arrival time for process {i+1}: ")))
    burst_time.append(int(input(f"Enter burst time for process {i+1}: ")))

# Call the FCFS function
fcfs_scheduling(n, arrival_time, burst_time)