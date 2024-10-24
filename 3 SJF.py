import pandas as pd

def preemptive_sjf(processes):
    # Sort processes based on arrival time
    processes.sort(key=lambda x: x[1])
    
    # Initialize variables
    n = len(processes)
    time = 0
    completed = 0
    burst_remaining = [p[2] for p in processes]
    start_times = [-1] * n
    finish_times = [-1] * n
    
    while completed < n:
        # Find the process with the shortest remaining time
        min_time = float('inf')
        idx = -1
        
        for i in range(n):
            if processes[i][1] <= time and burst_remaining[i] < min_time:
                min_time = burst_remaining[i]
                idx = i
        
        if idx == -1:
            # No process is available to run; jump to the next arrival time
            next_arrival = min(p[1] for p in processes if p[1] > time)
            time = next_arrival
            continue
        
        # Update start time for the process if it's the first time it's being run
        if start_times[idx] == -1:
            start_times[idx] = time
        
        # Run the process
        burst_remaining[idx] -= 1
        time += 1
        
        # Check if the process is finished
        if burst_remaining[idx] == 0:
            finish_times[idx] = time
            completed += 1
    
    # Create DataFrame for better visualization
    data = {
        'Process': [p[0] for p in processes],
        'Burst Time': [p[2] for p in processes],
        'Start Time': start_times,
        'Finish Time': finish_times
    }
    
    df = pd.DataFrame(data)
    return df

def get_processes():
    processes = []
    n = int(input("Enter the number of processes: "))
    
    for i in range(n):
        process_id = input(f"Enter Process ID for Process {i + 1}: ")
        arrival_time = int(input(f"Enter Arrival Time for Process {process_id}: "))
        burst_time = int(input(f"Enter Burst Time for Process {process_id}: "))
        processes.append((process_id, arrival_time, burst_time))
    
    return processes

def main():
    print("Preemptive Shortest Job First (SJF) Scheduling")
    processes = get_processes()
    df = preemptive_sjf(processes)
    
    print("\nScheduling Table:")
    print(df)

if __name__ == "__main__":
    main()
