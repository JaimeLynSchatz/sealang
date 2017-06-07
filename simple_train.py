sample = "What a to do to die today at a minute or two to two. A thing distinctly hard to say but harder still to do. For they will beat a tattoo at twenty to two, a ra ta ta ta ta ta ta ta ta ta to. And the dragon will come when he hears the drum at a minute or two to two today, at a minute or two to two."

order = 3

group_size = order + 1
text = None
graph = {}

text = sample.split()

text = text + text[:order]

for i in range(0, len(text) - group_size):
	key = tuple(text[i:i + order])
	value = text[i + order]

	if key in graph:
		graph[key].append(value)  # here's where we weight for probability
	else:
		graph[key] = [value]

for keys,values in graph.items():
    print(keys)
    print(values)