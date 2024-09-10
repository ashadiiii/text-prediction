import random
from predict import file2prob, file2pairs,tokenise_strings
import sys

loops = int(sys.argv[2])
file = sys.argv[1]
support = tokenise_strings(file)
        
words_and_probs = file2prob(file)

probs = words_and_probs.values()
word = random.choices(support,probs)[0]
words_dict = file2pairs(file) 
print(word+" ",end="")

for _ in range(loops-1):
    prob  = words_dict[word]
    p_value = prob.values()
    word = random.choices(support, p_value)
    word= word[0]
    print(word+" ",end="")


print()
    

