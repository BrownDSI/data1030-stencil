# In python, parenthesis, square and curly brackets need to line up
# For example this is well formed (), because there is one open and one closed parentheiss
# This is called Brace Matching
# More info: https://en.wikipedia.org/wiki/Brace_matching

def is_well_formed(s):
    left_chars, lookup = [], {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif lookup[left_chars.pop()] != c:
            # Unmatched right char or mismatched chars.
            return False
    return not left_chars

def test_brace_matching():
    assert is_well_formed('()')
    assert is_well_formed('()[]{}')
    assert is_well_formed('[()[]]{}')
    assert is_well_formed('(()[]{()[]{}{}})')
    assert not is_well_formed('([)]')
    assert not is_well_formed('[')
    assert not is_well_formed('[([()])])')
    assert not is_well_formed(('(([[]])))'))
    assert not is_well_formed('(()[]{()[]{})({}})')
