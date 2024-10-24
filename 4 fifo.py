class FIFO:
    def fifo_implementation(self, pages, capacity):
        page_faults = 0
        map = {}
        current_set = set()

        for i in range(len(pages)):
            if len(current_set) < capacity:
                if pages[i] not in current_set:
                    current_set.add(pages[i])
                    page_faults += 1
                map[pages[i]] = i
            else:
                if pages[i] not in current_set:
                    # Find the FIFO page to remove
                    fifo = float('inf')
                    val = None
                    for temp in current_set:
                        if map[temp] < fifo:
                            fifo = map[temp]
                            val = temp
                    current_set.remove(val)
                    del map[val]
                    map[pages[i]] = i
                    current_set.add(pages[i])
                    page_faults += 1

        print(f"Page Faults: {page_faults}")
        page_hits = len(pages) - page_faults
        print(f"Page Hits: {page_hits}")
        print(f"Page Fault Ratio: {page_faults}/{len(pages)} = {page_faults/len(pages):.2f}")
        print(f"Hit Ratio: {page_hits}/{len(pages)} = {page_hits / len(pages):.2f}")

if __name__ == "__main__":
    capacity = int(input("Enter capacity of page frame: "))
    pages = list(map(int, input("Enter values (space separated): ").split()))

    fifo = FIFO()
    fifo.fifo_implementation(pages, capacity)
