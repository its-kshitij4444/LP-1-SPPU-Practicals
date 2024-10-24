from tabulate import tabulate

class Process:
    def __init__(self, name, burst_time, priority):
        self.name = name
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0

def calculate_waiting_times(processes):
    # Sort processes based on priority (higher priority first) and arrival order
    processes.sort(key=lambda x: (-x.priority, x.name))
    
    total_waiting_time = 0
    current_time = 0
    
    for process in processes:
        process.waiting_time = current_time
        process.turnaround_time = process.waiting_time + process.burst_time
        total_waiting_time += process.waiting_time
        current_time += process.burst_time
    
    # Calculate average waiting time
    avg_waiting_time = total_waiting_time / len(processes)
    return avg_waiting_time

def get_process_details():
    processes = []
    num_processes = int(input("Enter the number of processes: "))
    
    for i in range(num_processes):
        name = input(f"Enter the name of process {i + 1}: ")
        while True:
            try:
                burst_time = int(input(f"Enter the burst time of {name}: "))
                priority = int(input(f"Enter the priority of {name} (higher number means higher priority): "))
                break
            except ValueError:
                print("Invalid input. Please enter numeric values for burst time and priority.")
        
        process = Process(name, burst_time, priority)
        processes.append(process)
    
    return processes

def display_results(processes, avg_waiting_time):
    # Prepare data for tabulation
    table_data = [
        [process.name, process.burst_time, process.priority, process.waiting_time, process.turnaround_time]
        for process in processes
    ]
    
    headers = ["Process Name", "Burst Time", "Priority", "Waiting Time", "Turnaround Time"]
    
    # Print results in a tabular format
    print("\nProcess Schedule:")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f} msec")

def main():
    processes = get_process_details()
    avg_waiting_time = calculate_waiting_times(processes)
    display_results(processes, avg_waiting_time)

if __name__ == "__main__":
    main()
