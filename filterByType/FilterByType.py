
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
current_tester = bS

# once we estab type, we're good for the rest of the run.
curr_type = type(current_tester)
if ((curr_type) is int):
    if (current_tester >= 100):
        print "Thats' a big number!"
    else:
        print "that's a small number"
elif ((curr_type)is str):
    if (len(current_tester) >= 50):
        print "Long sentence"
    else:
        print "short sentence"
elif ((curr_type) is list):
    if (len(current_tester) >= 10):
        print "big list!"
    else:
        print "short list"
