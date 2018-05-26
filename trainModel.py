import fasttext

#Para treinar o modelo pela primeira vez (demora vários minutos), irá criar um arquivo com o segundo parâmetro.bin
classifier = fasttext.supervised('./amazonreviews/train.ft.txt', 'model')

result = classifier.test('./amazonreviews/test.ft.txt')
print ('Precion:', result.precision)
print ('Recall:', result.recall)
print ('Número Exemplos:', result.nexamples)