class LRU:
    def lru_implementation(self, pages, capacity):
        page_faults = 0
        page_map = {}
        current_set = set()

        for i in range(len(pages)):
            if len(current_set) < capacity:
                if pages[i] not in current_set:
                    current_set.add(pages[i])
                    page_faults += 1
                page_map[pages[i]] = i
            else:
                if pages[i] not in current_set:
                    # Find the least recently used page
                    lru = float('inf')
                    val = None
                    for temp in current_set:
                        if page_map[temp] < lru:
                            lru = page_map[temp]
                            val = temp
                    current_set.remove(val)
                    del page_map[val]
                    current_set.add(pages[i])
                    page_faults += 1
                page_map[pages[i]] = i

        print("Page Faults:", page_faults)
        page_hits = len(pages) - page_faults
        print("Page Hits:", page_hits)
        print(f"Page Fault Ratio: {page_faults}/{len(pages)} = {page_faults / len(pages):.2f}")
        print("Hit Ratio: {}/{} = {:.2f}".format(page_hits, len(pages), page_hits / len(pages)))


if __name__ == "__main__":
    capacity = int(input("Enter capacity of page frame: ")) #3
    pages = list(map(int, input("Enter values (space separated): ").split())) # 7 0 1 2 0 3 0 4

    lru = LRU()
    lru.lru_implementation(pages, capacity)
