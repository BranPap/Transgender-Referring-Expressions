import nltk, os, string, csv
from nltk import word_tokenize
import re

def convertTuple(tup):
    str = ''.join(tup)
    return str

ignoreList = ["'",".",",","”","’","''","“","‘","’","―"]

filesText = []

PNDirectory = "PNtext/"
for filename in os.listdir(PNDirectory):
    with open(os.path.join(PNDirectory, filename),encoding='utf-8') as myfile:
        content = myfile.read().lower()
        filesText.append(content)

newList = []

for line in filesText:
    tokens = word_tokenize(line)
    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    tokens = list(filter(lambda token: token not in ignoreList, tokens))
    tokens = [i.strip(".") for i in tokens]
    newList.append(tokens)

newList = [item for sublist in newList for item in sublist]

PinkNewsFinalList = " ".join(newList)

print("PinkNews Word Count:"+str(len(PinkNewsFinalList)))

tokens = nltk.word_tokenize(PinkNewsFinalList)
bigrams = nltk.bigrams(tokens)
frequence = nltk.FreqDist(bigrams)

test = dict(sorted(frequence.items(), key=lambda x:x[1], reverse=True))

stopWords = ['of','the','but','do','as','if','on','a','an','it','to','be','been','is','are','am','that','these','this','those','you','your','us','and','don','who','i','for','in','he','she','they','we','not','s','t','\'re','with','than','their']

PNDict = {}

for item in test.items():
    if item[0][0] not in stopWords and item[0][1] not in stopWords:
        itemList = list(item[0])
        if item[1] < 2000:
            PNDict[' '.join(itemList)] = item[1]

### BREITBART

filesText = []

BreitbartDirectory = "BreitbartText/"
for filename in os.listdir(BreitbartDirectory):
    if filename.endswith('.txt'):
        with open(os.path.join(BreitbartDirectory, filename)) as myfile:
            content = myfile.read().lower()
            filesText.append(content)

newList = []

for line in filesText:
    tokens = word_tokenize(line)
    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    tokens = list(filter(lambda token: token not in ignoreList, tokens))
    tokens = [i.strip(".") for i in tokens]
    newList.append(tokens)

newList = [item for sublist in newList for item in sublist]

BreitbartFinalList = " ".join(newList)

print("Breitbart Word Count:"+str(len(BreitbartFinalList)))

tokens = nltk.word_tokenize(BreitbartFinalList)
bigrams = nltk.bigrams(tokens)
frequence = nltk.FreqDist(bigrams)

test = dict(sorted(frequence.items(), key=lambda x:x[1], reverse=True))

BreitbartDict = {}

for item in test.items():
    if item[0][0] not in stopWords and item[0][1] not in stopWords:
        itemList = list(item[0])
        if item[1] < 2000:
            BreitbartDict[' '.join(itemList)] = item[1]

### Writing to individual files

csv_columns = ['bigram','count','source']

with open("allBigrams.csv",'w') as newFile:
    writer = csv.writer(newFile)
    writer.writerow(csv_columns)
    for row in list(BreitbartDict.items()):
        row = list(row)
        row.append("Breitbart")
        writer.writerow(row)
    for row in list(PNDict.items()):
        row = list(row)
        row.append("PinkNews")
        writer.writerow(row)
        
with open("allBigramsBreitbart.txt",'w') as newFile:
    yes = 0
    for row in list(BreitbartDict.items()):
        newFile.write(str(row[1]) + "_" + "\""+row[0]+"\"")
        newFile.write('\n')
    
        
with open("allBigramsPinkNews.txt",'w') as newFile:
    yes = 0
    for row in list(PNDict.items()):
        newFile.write(str(row[1]) + "_" + "\""+row[0]+"\"")
        newFile.write('\n')

### COMBINED DATA

filesText = []

AllDirectory = "AllText/"
for filename in os.listdir(AllDirectory):
    with open(os.path.join(AllDirectory, filename),encoding='utf-8') as myfile:
        if filename.endswith('.txt'):
            content = myfile.read().lower()
            filesText.append(content)

newList = []

for line in filesText:
    tokens = word_tokenize(line)
    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    tokens = list(filter(lambda token: token not in ignoreList, tokens))
    tokens = [i.strip(".") for i in tokens]
    newList.append(tokens)
    
### Adding in the COCA data ###

COCAfilesText = []

AllDirectory = "COCAText/"
for filename in os.listdir(AllDirectory):
    with open(os.path.join(AllDirectory, filename),encoding='utf-8') as myfile:
        if filename.endswith('.txt'):
            content = myfile.readlines()
            for line in content:
                COCAfilesText.append(line.lower())
    
subbedFilesText = []

for line in COCAfilesText:
    line = re.sub(r"\s([\.,:)?])+",r"\1",line)
    line = re.sub("@{2}[0-9]+",r"",line)
    line =re.sub(r"<[a-z]+>\s?",r"",line)
    line=re.sub(r"\*{2}[A-Z0-9;]+",r"",line)
    line=re.sub(r'@', '', line)
    line=re.sub(r'\s["\']\s',' ',line)
    line=re.sub(r"([(])\s+",r"\1",line)
    line=re.sub(r'\s([a-zA-Z])?\'([a-zA-Z])+',r"\1'\2",line)
    line=re.sub(r'\s{2,}',' ',line)
    line=re.sub(r'\'',"’",line)
    subbedFilesText.append(line.strip('\''))
    
    
for line in subbedFilesText:
    tokens = word_tokenize(line)
    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    tokens = list(filter(lambda token: token not in ignoreList, tokens))
    tokens = [i.strip(".") for i in tokens]
    newList.append(tokens)
    
    
### BACK TO ALL ###

newList = [item for sublist in newList for item in sublist]

AllFinalList = " ".join(newList)

print(str(len(AllFinalList)))

tokens = nltk.word_tokenize(AllFinalList)
bigrams = nltk.bigrams(tokens)
frequence = nltk.FreqDist(bigrams)

test = dict(sorted(frequence.items(), key=lambda x:x[1], reverse=True))

AllDict = {}

for item in test.items():
    if item[0][0] not in stopWords and item[0][1] not in stopWords:
        itemList = list(item[0])
        AllDict[' '.join(itemList)] = item[1]
            
with open("allBigramsInclusive.txt",'w') as newFile:
    yes = 0
    for row in list(AllDict.items()):
        newFile.write(str(row[1]) + "_" + "\""+row[0]+"\"")
        newFile.write('\n')