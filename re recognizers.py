#!/usr/bin/python

def match(pattern, text):
	remainders = pattern(text)
	if remainders:
		shortest = min(remainders, key = len)
		return text[:len(text) - len(shortest)]
	return None	
	
def search(pattern, text):
	# takes a pattern and text: return the first matched text
	for i in range(len(text)):
		m = match(pattern, text[i:])
		if m is not None:
			return m
			
def lit(x): return lambda text : set([text[len(x):]] if text.startswith(x) else null)
def seq(x, y): return lambda text : set().union(*map(y, x(text)))
def alt(x, y): return lambda text : x(text) | y(text)
def oneof(chars): return lambda text : set([text[1:]] if (text and text[0] in chars) else null)
dot = lambda text : set([text[1:]] if len(text) >= 1 else null)
eol = lambda text : set([""] if text == "" else null)
def star(x) : return lambda text : (set([text]) | set(t2 for t1 in x(text) if t1 != text for t2 in star(x)(t1)))

null = frozenset([])


def test():
	assert match(star(lit('a')), 'aaaaabbbaa') == 'aaaaa'
	assert match(lit('hello'), 'hello how are you?') == 'hello'
	assert match(lit('x'), 'hello how are you?') == None
	assert match(oneof('xyz'), 'x**2 + y**2 = r**2') == 'x'
	assert match(oneof('xyz'), '   x is here!') == None
	return 'tests pass'
print test()


