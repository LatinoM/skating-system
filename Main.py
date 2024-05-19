from NonFinalRound import NonFinalRound
beginner_waltz_one = NonFinalRound([102,105,115,118,121,124,130,142,145,148,151,153,155,160,163,166,170,173,176], 15)
beginner_waltz_one.take_marks([105,118,121,124,130,142,145,148,151,153,160,163,166,170,176])
beginner_waltz_one.take_marks([105,115,121,124,130,142,145,148,151,153,155,160,163,166,176])
beginner_waltz_one.take_marks([105,115,118,121,124,142,145,148,151,153,160,163,166,173,176])
print(beginner_waltz_one.get_recalled())