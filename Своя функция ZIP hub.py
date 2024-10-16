def shortest(string,tpl):
    return min(len(string), len(tpl))

text = 'abcdv'
itr_object = 10, 20, 30, 40
itr_object = list(itr_object)

zip_object = ((text[i], itr_object[i]) for i in range(shortest(text,itr_object)))

print(zip_object)

for i_object in zip_object:
    print(i_object)
