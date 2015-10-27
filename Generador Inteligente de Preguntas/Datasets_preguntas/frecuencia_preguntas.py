import nltk

a = 'What year was the Mona Lisa painted ? date What is the date of Boxing Day ?'
b = nltk.word_tokenize(a)

f = open('train_5500.label.txt')
tokenized_text = [linea.split()[1] for linea in f]
fdist = nltk.FreqDist(tokenized_text)
print "Who\t=\t"+ str(fdist['Who']) +"\n"+ "Where\t=\t"+ str(fdist['Where']) +"\n"+ "When\t=\t"+ str(fdist['When']) +"\n"+ "Why\t=\t"+ str(fdist['Why']) +"\n"+ "What\t=\t"+ str(fdist['What']) +"\n"+ "Which\t=\t"+ str(fdist['Which']) +"\n"+ "How\t=\t"+ str(fdist['How'])
fdist.plot(21)