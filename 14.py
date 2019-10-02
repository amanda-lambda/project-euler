max_seqlen = 0
prev_seqs = {}

for i in range(1, 999999):

    # Find Colatz chain length
    i_orig = i
    seqlen = 1
    while True:
        if i == 1:
            break
        if i in prev_seqs:
            seqlen += prev_seqs[i]
            break
        if i % 2 == 0:
            i = i/2
            seqlen += 1
        else:
            i = 3*i + 1
            seqlen += 1

    # Cache old results for faster computation
    prev_seqs[i] = seqlen

    # Keep track of longest Colatz chain
    if seqlen > max_seqlen:
        max_seqlen = seqlen
        max_num = i_orig

print(max_num)