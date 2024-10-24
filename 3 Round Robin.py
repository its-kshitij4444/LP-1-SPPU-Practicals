from collections import deque

def round_robin_scheduling(processes, time_slice):
    n = len(processes)

    process_ids = [process[0] for process in processes]
    burst_times = [process[1] for process in processes]

    waiting_times = [0] * n
    turn_around_times = [0] * n
    remaining_times = burst_times[:]
    queue = deque([(i, burst_times[i]) for i in range(n)])

    current_time = 0

    while queue:
        process_index, remaining_time = queue.popleft()

        if remaining_time > time_slice:
            remaining_times[process_index] -= time_slice
            current_time += time_slice
            queue.append((process_index, remaining_times[process_index]))
        else:
            current_time += remaining_time
            remaining_times[process_index] = 0
            turn_around_times[process_index] = current_time
            waiting_times[process_index] = turn_around_times[process_index] - burst_times[process_index]

    average_turn_around_time = sum(turn_around_times) / n
    average_waiting_time = sum(waiting_times) / n
    
    print(f"{'Serial No':<10} {'Process':<10} {'CPU Time':<10} {'Turnaround Time':<15} {'Waiting Time':<15}")
    for i in range(n):
        print(f"{i + 1:<10} {process_ids[i]:<10} {burst_times[i]:<10} {turn_around_times[i]:<15} {waiting_times[i]:<15}")
    
    print(f"\nAverage Turnaround Time: {average_turn_around_time:.2f}")
    print(f"Average Waiting Time: {average_waiting_time:.2f}")

def get_process_input():
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    
    for i in range(num_processes):
        process_id = int(input(f"Enter ID for process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for process {process_id}: "))
        processes.append((process_id, burst_time))
    
    return processes

def main():
    processes = get_process_input()
    time_slice = int(input("Enter the time slice (quantum): "))
    round_robin_scheduling(processes, time_slice)

if __name__ == "__main__":
    main()
