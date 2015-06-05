from nose.tools import assert_equal

from frogger import dfs, bfs, IMPOSSIBLE

implementations = [
    dfs,
    bfs
]

# Frogger puzzles and their solutions
examples = {
    '_X__XX_': 5,
    '____XX_': 5,
    '_____________': 5,
    'XXXXXXXXXXXXX': IMPOSSIBLE
}

def test_frogger():
    def function(implementation, string, expected):
        assert_equal(implementation(string), expected)

    for prompt, expected in examples.items():
        for implementation in implementations:
            yield function, implementation, prompt, expected


def test_agreement():
    def function(string):
        results = dict((f.__name__, f(string)) for f in implementations)
        message = '; '.join('%s(%s) = %s' % (k, string, v) for k, v in results.items())
        assert len(set(results.values())) == 1, message

    for prompt in examples.keys():
        yield function, prompt

def test_stress():
    '''The BFS implementation should be able to handle some real stress.'''
    string = '_' * 1000
    assert_equal(bfs(string), 334)
