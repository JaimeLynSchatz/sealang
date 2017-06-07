import markovify

# pull in text from a file
with open("haskell_code.txt") as f:
	text = f.read()

# build the model
# if regular, period-delimited sentences
# text_model = markovify.Text(text)

# if no periods
text_model = markovify.NewlineText

# Print five randomly-generated sentences
for i in range(5):
	print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
	print(text_model.make_short_sentence(140))
