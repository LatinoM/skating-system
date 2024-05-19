class NonFinalRound:
    def __init__(self, numbers:list, min_to_qualify:int):
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
            for num in sb.keys():
                if sb[num] == highest_marks:
                    recalled.append(num)
        return sorted(recalled)
    
    def _get_remaining(scoreboard, recalled_so_far):
        output = scoreboard.copy()
        for num in recalled_so_far:
            if num in output.keys():
                output.pop(num)
        return output
    

    