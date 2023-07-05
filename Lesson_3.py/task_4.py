# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
import string
text = "aa aaa aaa aaa aaa aaa aa aa aa a a adas asdada sa asd as a as aad ads adsa dasd asdaads as a as da asasasadasdadas as aasas as asd asas as asd asads asassdsdsd zxczxczxcc  zxczxc zxc zx zx zcx zcx cz"
words1 = text.split()
[word.strip(string.punctuation) for word in words1]
words = []
for word in words1:
    if len(word) > 0:
        words.append(word.lower())

freq = {}
for word in words:
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] = freq[word] + 1

tuples = []
for key, value in freq.items():
    tuples.append((key, value))
tuples.sort(key=lambda x: -x[1])

for i in range(0, 10):
    if i >= len(tuples):
        break
    print(tuples[i][0] + " " + str(tuples[i][1]))