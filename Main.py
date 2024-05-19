from NonFinalRound import NonFinalRound
beginner_waltz_one = NonFinalRound([102,105,115,118,121,124,130,142,145,148,151,153,155,160,163,166,170,173,176], 15)
beginner_waltz_one.take_marks([105,118,121,124,130,142,145,148,151,153,160,163,166,170,176])
beginner_waltz_one.take_marks([105,115,121,124,130,142,145,148,151,153,155,160,163,166,176])
beginner_waltz_one.take_marks([105,115,118,121,124,142,145,148,151,153,160,163,166,173,176])
print(beginner_waltz_one.get_recalled())

novice_wq_one = NonFinalRound([100, 101,104,106,109,112,114,117,123,125,127,129,133,135,141,143,144,146,149,152,156,159,161,165,168,169,175],20)
# Waltz
novice_wq_one.take_marks([100,101,104,106,109,112,125,129,133,141,144,146,149,152,156,159,161,165,169,175])
novice_wq_one.take_marks([100,101,104,106,109,112,123,125,129,133,141,144,146,149,152,156,159,161,165,175])
novice_wq_one.take_marks([100,106,109,112,114,123,125,127,129,133,141,144,146,152,156,159,161,165,168,175])
# Quickstep
novice_wq_one.take_marks([100,101,104,106,109,112,123,125,129,133,135,141,144,146,156,159,161,168,169,175])
novice_wq_one.take_marks([100,101,106,109,112,117,123,125,127,129,133,141,144,146,149,152,159,161,165,175])
novice_wq_one.take_marks([104,106,109,112,114,123,125,127,129,133,141,144,146,149,152,156,159,161,165,175])

print(novice_wq_one.get_recalled())

