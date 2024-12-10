from lib.constants import STATE
from lib.memory import Memory


class LRU(Memory):
    def __init__(self, config, pages):
        super().__init__(config, pages)
        self.st = []

    def addPageToMemory(self, page):
        if len(self.queue) < self.memory_capacity:
            self.queue.append(page)
            self.st.append(len(self.queue) - 1)
        else:
            i = self.st.pop(0)
            self.queue[i] = page
            self.st.append(i)

    def run(self):
        for page in self.pages:
            if not self.isPageInMemory(page):
                self.total_faults += 1
                self.state = STATE["FAULT"]
                self.addPageToMemory(page)
            else:
                self.st.append(self.st.pop(self.st.index(self.queue.index(page))))
                self.state = STATE["HIT"]
            self.printCurrentState(page)
        self.printStats()


metadata = {
    "name": "Least Recently Used (LRU)",
    "description": "LRU is a page-replacement algorithm that replaces the least recently used page in the memory.",
}
