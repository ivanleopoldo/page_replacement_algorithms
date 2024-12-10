from .constants import DEFAULT_STRING, STATE


class Memory:
    def __init__(self, config, pages=[]):
        # CONFIG
        self.memory_capacity = config["defaults"]["capacity"]
        self.settings = config["settings"]

        self.state = STATE["FAULT"]

        # INPUT
        self.pages = pages

        # MEMORY STATE
        self.top = 0
        self.queue = []

        # STATS
        self.total_faults = 0

    def isPageInMemory(self, page):
        return page in self.queue

    def addPageToMemory(self, page):
        if len(self.queue) < self.memory_capacity:
            self.queue.append(page)
        else:
            self.queue[self.top] = page
            self.top = (self.top + 1) % self.memory_capacity

    def printCurrentState(self, page):
        print(f"   {page}\t\t", end="")
        print(self.getMemoryState, end=" ")
        for _ in range(self.memory_capacity - len(self.queue)):
            print(" ", end=" ")
        print(f" {self.state}")

    def printStats(self):
        print(f"\nTotal Pages: {len(self.pages)}")
        print(f"Total Page Faults: {self.total_faults}")
        print(f"Total Page Hits: {len(self.pages) - self.total_faults}")
        print("Fault Rate: %.2f%%" % self.getFaultRate())
        print("Hit Rate: %.2f%%" % self.getHitRate())

    def getFaultRate(self):
        return (self.total_faults / len(self.pages)) * 100

    def getHitRate(self):
        return 100 - self.getFaultRate()

    @property
    def getMemoryState(self):
        return self.queue
