import pandas as pd
lst = []

with open('../data/brown_corp.txt', 'r+') as f:
	text =  f.readlines()[0]
	for line in text.split('.'):
		if len(line) > 4:
			lst.append(line)


df = pd.DataFrame(lst, columns=['text'])
print(df.head())
df.to_csv('../data/cleaned/brown.csv', index=False)

print('done')