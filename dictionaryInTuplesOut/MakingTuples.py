x = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}


def making_tuples(x):
    final_tuple = []
    for name in x:
        empty_tuple = (name, x[name])
        final_tuple.append(empty_tuple)
    return final_tuple


print making_tuples(x)
