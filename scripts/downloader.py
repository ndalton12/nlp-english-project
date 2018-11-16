import nltk

# Generate brown corpus text file
with open('../data/brown_corp.txt', 'w+') as f:
    for word in nltk.corpus.brown.words():
        f.write('{word} '.format(word=word))

print('done')