import sys, pprint, randon

class Markov(object):
	def __init__(self, order):
		# order determines how many words to consider before generating
		self.order = order

		self.group_size = self.order + 1

		# self.text will hold the training text
		self.text = None

		# the dictionary that holds the Markov Chains
		self.graph = []

		return

	def train(self, filename)
		# get the text, split it up
		self.text = file(filename).read().split()
		self.text = self.text + self.text[:self.order]

		for i in range(0, len(self.text) - self.group_size):
			key = tuple(self.text[i:i + self.order])
	    	value = self.text[i + self.order]

		if key in self.graph:
	    	self.graph[key].append(value)
	    else:
	    	self.graph[key] = [value]
		return

	def generate(self, length):
		index = random.randint(0, len(self.length) - self.order)
		result = self.text[index:index + self.order]

		for i in range(length):
			state = tuple(result[len(result) - self.order:])
			next_word = random.choice(self.graph[state])
			result.append(next_word)

		return "".join(result[self.order:])

english_markov = Markov(3)
english_markov.train(federalist_papers.txt)


# Text as a sequence of states