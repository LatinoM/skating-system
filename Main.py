from NonFinalRound import NonFinalRound

novice_wq_one = NonFinalRound([100, 101,104,106,109,112,114,117,123,125,127,129,133,135,141,143,144,146,149,152,156,159,161,165,168,169,175],20)
# Waltz
novice_wq_one.take_marks([100,101,104,106,109,112,125,129,133,141,144,146,149,152,156,159,161,165,169,175])
novice_wq_one.take_marks([100,101,104,106,109,112,123,125,129,133,141,144,146,149,152,156,159,161,165,175])
novice_wq_one.take_marks([100,106,109,112,114,123,125,127,129,133,141,144,146,152,156,159,161,165,168,175])
# Quickstep
novice_wq_one.take_marks([100,101,104,106,109,112,123,125,129,133,135,141,144,146,156,159,161,168,169,175])
novice_wq_one.take_marks([100,101,106,109,112,117,123,125,127,129,133,141,144,146,149,152,159,161,165,175])
novice_wq_one.take_marks([104,106,109,112,114,123,125,127,129,133,141,144,146,149,152,156,159,161,165,175])

novice_wq_two = NonFinalRound(novice_wq_one.get_recalled(),15)
# Waltz
novice_wq_two.take_marks([101,104,106,109,112,125,129,133,144,146,149,156,161,165,175])
novice_wq_two.take_marks([100,104,109,112,123,129,133,144,146,149,152,159,161,165,175])
novice_wq_two.take_marks([100,106,109,112,123,125,129,133,141,144,146,149,156,165,175])
# Quickstep
novice_wq_two.take_marks([101,104,106,109,112,125,129,133,141,144,149,156,161,165,175])
novice_wq_two.take_marks([100,106,109,112,123,129,133,144,146,149,152,159,161,165,175])
novice_wq_two.take_marks([100,106,109,112,123,125,129,133,144,149,152,156,159,161,175])

novice_wq_three = NonFinalRound(novice_wq_two.get_recalled(),10)
# Waltz
novice_wq_three.take_marks([106,109,125,129,133,144,149,156,161,165])
novice_wq_three.take_marks([106,109,112,123,129,133,146,149,161,165])
novice_wq_three.take_marks([100,106,109,112,123,125,129,133,156,165])
# Quickstep
novice_wq_three.take_marks([106,109,125,129,133,144,149,156,161,165])
novice_wq_three.take_marks([106,109,112,129,133,146,149,161,165,175])
novice_wq_three.take_marks([100,106,109,112,123,125,129,133,156,165])

novice_wq_four = NonFinalRound(novice_wq_three.get_recalled(),6)
#Waltz
novice_wq_four.take_marks([106,125,133,149,156,165])
novice_wq_four.take_marks([106,109,112,129,133,165])
novice_wq_four.take_marks([106,109,112,129,133,156])
# Quickstep
novice_wq_four.take_marks([125,133,149,156,161,165])
novice_wq_four.take_marks([106,112,133,149,161,165])
novice_wq_four.take_marks([106,109,129,133,156,165])

novice_wq_finalists = novice_wq_four.get_recalled()

#print(f"The {len(novice_wq_finalists)} finalists for the Novice WQ are:")
#print(novice_wq_finalists)

b_n_tango_one = NonFinalRound()
b_n_tango_one.read_csv("./examples/liverpool_bn_tango_one.csv")
print(b_n_tango_one.get_recalled())
















