words = ['hello', 'world', 'how', 'are', 'world','how']
labels = [0, 1, 0, 0, 0, 1]
sentence = ['hello there', 'the world today', 'how you doing?', 'are you lucky', 'world news', 'how is it possible']
result = {}
for i, word in enumerate(words):
    if not word in result:
        result[word] = []
    result[word].append([labels[i], sentence[i]])
print(result)