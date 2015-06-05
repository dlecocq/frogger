'''The frogger game.

A frog may hop forward 3, or back 2. A frog may only jump on an underscore.
Return the number of jumps required to make it to the end, or IMPOSSIBLE
otherwise.'''

import sys

IMPOSSIBLE = sys.maxint

def dfs(string, visited=None, spot=-1, iteration=0):
    '''A dfs-approach.'''
    # If we can jump to the end, we're done
    if spot + 3 >= len(string):
        return iteration + 1

    # Initialize visited if we've not already done so
    if not visited:
        visited = [-1] * len(string)
    else:
        # Visit the spot we're on
        visited[spot] = iteration

    # To jump to a square, we cannot have visited it and it has to be safe
    options = []
    if (visited[spot + 3] == -1) and string[spot + 3] == '_':
        options.append(spot + 3)
    if spot >= 2 and (visited[spot - 2] == -1) and string[spot - 2] == '_':
        options.append(spot - 2)

    if not options:
        return IMPOSSIBLE
    return min(
        dfs(string, list(visited), o, iteration + 1) for o in options
    )


def bfs(string):
    '''A bfs-approach, articulated not as a graph.'''
    visited = [False] * len(string)
    # We have initially exactly one option -- jumping to 2.
    options = [2]
    # There can be at most len(string) iterations
    for iteration in xrange(len(string)):
        if not options:
            break
        # Our next options. It's important that this be a set.
        next = set()
        # Visit all of our options. Do this before the next loop
        for option in options:
            visited[option] = True
        for option in options:
            if (option + 3) > len(string):
                # If we have the option to jump to the end, success
                return iteration + 2
            if option >= 2 and not visited[option - 2] and (string[option - 2] == '_'):
                next.add(option - 2)
            if not visited[option + 3] and (string[option + 3] == '_'):
                next.add(option + 3)
        options = next
    return IMPOSSIBLE
