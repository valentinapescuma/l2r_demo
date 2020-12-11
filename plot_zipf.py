import matplotlib.pyplot as plt

def read_subtlex_file(subtlex_file_path):
	freqs = {}
	with open(subtlex_file_path) as file:
		for line in file:
			word, freq = line.split('\t')
			freqs[word] = int(freq)
	return freqs

def get_n_most_frequent_words(freqs, n):
	words_freqs = []
	for word, freq in freqs.items():
		words_freqs.append((freq, word))
	words_freqs.sort(reverse=True)
	return words_freqs[:n]

def plot_freq_against_rank(most_frequent_words):
	frequencies = [freq for freq, _ in most_frequent_words]
	ranks = range(1, len(frequencies)+1)
	plt.plot(ranks, frequencies)
	plt.xlabel('Rank')
	plt.show()

freqs = read_subtlex_file('subtlex_english')
most_frequent_words = get_n_most_frequent_words(freqs, 1000)
plot_freq_against_rank(most_frequent_words)
