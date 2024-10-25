class Optimal:
    def predict(self, page, current_set, index):
        val = -1
        farthest_index = -1

        for temp in current_set:
            try:
                # Find the index of the next occurrence of temp in the page reference string
                i = page[index:].index(temp) + index
            except ValueError:
                # temp is not found, so it's a candidate for removal
                return temp

            # If the index of this page is farther than the current farthest_index
            if i > farthest_index:
                farthest_index = i
                val = temp

        return val

    def optimal_implementation(self, page, cap):
        page_faults = 0
        current_set = set()

        for i in range(len(page)):
            if len(current_set) < cap:
                if page[i] not in current_set:
                    current_set.add(page[i])
                    page_faults += 1
            else:
                if page[i] not in current_set:
                    predicted_element = self.predict(page, current_set, i + 1)
                    current_set.remove(predicted_element)
                    current_set.add(page[i])
                    page_faults += 1

        print("Page Faults:", page_faults)
        page_hits = len(page) - page_faults
        print("Page Hits:", page_hits)
        print(f"Page Fault Ratio: {page_faults}/{len(page)} = {page_faults / len(page):.2f}")
        print("Hit Ratio: {}/{} = {:.2f}".format(page_hits, len(page), page_hits / len(page)))


if __name__ == "__main__":
    capacity = int(input("Enter capacity of page frame: ")) #3
    pages = list(map(int, input("Enter values (space separated): ").split())) # 7 0 1 2 0 3 0 4

    optimal = Optimal()
    optimal.optimal_implementation(pages, capacity)
