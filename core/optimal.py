from lib.constants import STATE
from lib.memory import Memory


class OPTIMAL(Memory):
    def __init__(self, config, pages):
        super().__init__(config, pages)

    def run(self):
        occurance = [None for _ in range(self.memory_capacity)]
        for i in range(len(self.pages)):
            if not self.isPageInMemory(self.pages[i]):
                if len(self.queue) < self.memory_capacity:
                    self.addPageToMemory(self.pages[i])
                else:
                    for j in range(len(self.queue)):
                        if self.queue[j] not in self.pages[i + 1 :]:
                            self.queue[j] = self.pages[i]
                            break
                        else:
                            occurance[j] = self.pages[i + 1 :].index(self.queue[j])
                    else:
                        self.queue[occurance.index(max(occurance))] = self.pages[i]
                self.total_faults += 1
                self.state = STATE["FAULT"]
            else:
                self.state = STATE["HIT"]

            self.printCurrentState(self.pages[i])
        self.printStats()


metadata = {
    "name": "Optimal",
    "description": "OPTIMAL is a page-replacement algorithm that replaces the page that will not be used for the longest period of time.",
}
