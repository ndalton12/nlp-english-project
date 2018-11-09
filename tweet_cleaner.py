import string
import langid

cleaned = open("data/MarchForScience_tweets_cleaned.txt", "w+")

with open('data/MarchForScience_tweets.txt', 'r+') as f:
    for line in f.readlines():
    	if langid.classify(line)[0] != 'en':
    		continue
    	for word in line.split(' '):
    		if not word:
    			continue
	    	if not any([x for x in ('http', '@', '#', 'RT') if x in word]) and word[0].lower() in string.ascii_lowercase:
	    		cleaned.write('{word} '.format(word=word))

cleaned.close()
print('done')
