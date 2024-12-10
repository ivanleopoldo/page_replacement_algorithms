from lib.constants import STATE
from lib.memory import Memory


class FIFO(Memory):
    def __init__(self, config, pages):
        super().__init__(config, pages)

    def run(self):
        for page in self.pages:
            if not self.isPageInMemory(page):
                self.total_faults += 1
                self.state = STATE["FAULT"]
                self.addPageToMemory(page)
            else:
                self.state = STATE["HIT"]

            self.printCurrentState(page)

        self.printStats()


metadata = {
    "name": "First In First Out (FIFO)",
    "description": "FIFO is the simplest page-replacement algorithm. It replaces the oldest page in the memory.",
}
