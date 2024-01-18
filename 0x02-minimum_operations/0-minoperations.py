#!/usr/bin/python3
'''The minimum operations, coding interview.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''

    if not isinstance(n, int):
        return 0
    

    operatiion_count = 0
    clip_board = 0
    done_ops = 1

    while done_ops < n:
        if clip_board == 0:
            clip_board = done_ops
            done += clip_board
            operatiion_count +=2

        elif - done_ops > 0 and (n - done_ops) % done_ops == 0:
            done_ops += clip_board
            operatiion_count += 1


        return operatiion_count
    