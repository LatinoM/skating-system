import csv
class NonFinalRound:
    def __init__(self, numbers:list = [], min_to_qualify:int = 0, name:str = "Unnamed Dance"):
        self.name = name
        self.scoreboard = {num:0 for num in sorted(numbers)}
        self.min_to_qualify = min_to_qualify

    def take_marks(self, nums):
        for num in nums:
            self.scoreboard[num] += 1

    def get_recalled(self):
        recalled = []
        sb = self.scoreboard.copy()
        while(len(recalled)<self.min_to_qualify):
            sb = NonFinalRound._get_remaining(sb, recalled)
            highest_marks = max(sb.values())
            if highest_marks == 0:
                break
            for num in sb.keys():
                if sb[num] == highest_marks:
                    recalled.append(num)
        print(f"{len(recalled)} couples recalled.")
        return sorted(recalled)
    
    def _get_remaining(scoreboard, recalled_so_far):
        output = scoreboard.copy()
        for num in recalled_so_far:
            if num in output.keys():
                output.pop(num)
        return output
    
    def read_csv(self, pathname):
        dances = 0
        couples = 0
        marks = dict()
        with open(pathname, mode='r', encoding="utf-8-sig") as file:
            csv_file = csv.reader(file)
            for index,line in enumerate(csv_file):
                if index == 0:
                    self.judges = len(line)-1
                    self.name = line[0]
                    print(f"Reading {self.name} Scoresheet")
                elif index == 1:
                    self.min_to_qualify = int(line[0])
                    print(f"- need {self.min_to_qualify} to be recalled.")
                elif index == 2:
                    couples = int(line[0])
                    print(f"- currently {couples} couples.")
                elif index == 3:
                    dances = int(line[0])
                    print(f"- {dances} dance{'s' if dances>1 else ''}")
                elif index - 4 % (couples+1) == 0:
                    print(f"Processing {line[0]}")
                else:
                    if line[0] not in marks.keys():
                        marks[int(line[0])] = 0
                    marks[int(line[0])] += line[1:].count("x")
            self.scoreboard = marks   
            



    