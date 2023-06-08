## length uzunluğı değiştirilerek istenilen uzunlukta oluşabilecek bütün random kelimeler oluşturuluyor.
## Oluşturulan kelimeleri ekrana print ediyorum.
## Bir dosyaya kaydetmek istersem, python random_generator.py > generated_wordlist.txt

## oluşturulan kelimelerin sonunda / karakteri yok, bunu eklemek istersem 
## sed 's/$/\//' generated_wordlist.txt > Slash_Added_wordlist.txt

import itertools
import string

def generate_4_character_words():
    words = []
    characters = string.ascii_letters + string.digits  # Büyük harfler, küçük harfler ve sayılar
    length = 4  # Uzunluk: 4
    
    combinations = itertools.product(characters, repeat=length)
    for combination in combinations:
        word = ''.join(combination)
        words.append(word)
    
    return words

four_character_words = generate_4_character_words()

for word in four_character_words:
    print(word)
