def word_count(sentence, word):
    sentence = sentence.lower()
    length_string = len(sentence)
    word = word.lower()
    length_word = len(word)
    find = sentence.find(word)
    num_of_word = 0
    while find != -1:
        slice_start = find + length_word
        slice_end = length_string
        slice_result = slice(slice_start, slice_end)
        length_string = len(sentence[slice_result])
        if length_string != 0:
            find = sentence[slice_result].find(word)
            num_of_word += 1
        else:
            num_of_word += 1
            find = -1
    return num_of_word


file1 = open(r"C:\Users\Simmi\Downloads\String.txt", "r")
string1 = file1.read()
print(string1)
split = string1.rsplit(" ")
i = 0
length = len(split)
word_cloud_dict = {}
while i < length:
    num = word_count(string1, split[i])
    if split[i] in word_cloud_dict:
        word_cloud_dict[split[i]] += 1
    else:
        word_cloud_dict.update({split[i].lower(): num})
    i += 1
print(word_cloud_dict)
