

import chunk
from posixpath import split


word = 'nice'
val=[('', 'nice'), ('n', 'ice'), ('ni', 'ce'), ('nic', 'e'), ('nice', '')]



def delete_letter(word):
    chunks=[]
    splits= [(word[:i],word[i:]) for i in range(len(word)+1)]
    for a,b in splits:
        if b:
            chunks.append(a+b[1:])
    return chunks

print(delete_letter(word))

    

    # print(word)