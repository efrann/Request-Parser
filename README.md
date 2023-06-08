## KULLANIM

1. dirsearch ile yapılan dizin taraması yapılır.

`dirsearch -r -u <domain.com> -e all --wordlist <wordlist_file> -x 402,403,404,500,529 -i 200,302 
--full-url --format=plain -o <output_file>`

2. Bazı durumlarda random kelimelerin bulunduğu bir wordlist hazırlanması gerekebilir.

`python random_generator.py > random_generated_wordlist.txt `

Oluşturulan kelimelerin sonunda / karakteri yok, bunu eklemek istersem 

`sed 's/$/\//' generated_wordlist.txt > Slash_Added_wordlist.txt`


## İLK HALİ
- 302     0B   http://a.com:80/aaq/    -> REDIRECTS TO: http://b.com/?q=RFLXVAEU-
- 302     0B   http://a.com:80/aag/    -> REDIRECTS TO: http://b.com/?q=RRNJZTZSVjN
- 302     0B   http://a.com:80/aac/    -> REDIRECTS TO: http://c.com/?q=NTRUACZZZ3--
- 302     0B   http://a.com:80/aab/    -> REDIRECTS TO: http://d.com/?q=TMCGHFZZZ335
- 302     0B   http://a.com:80/aal/    -> REDIRECTS TO: http://d.com/?q=IZVINAZZZ31290
- 302     0B   http://a.com:80/aas/    -> REDIRECTS TO: http://trendyol.com/?q=YCARDZZZZ32719-

`python dirsearch_parser.py -i <input_file> -o <output_temiz.txt>`

3. Dirsearch ile tarama tamamlandıktan sonra çıktıdaki istenmeyen yerler `grep -v` komutu ile elenebilir.

`cat output_file.txt | grep -v d.com | grep -v c.com`


## YENİ HALİ 
- http://b.com/?q=RFLXVAEU-
- http://b.com/?q=RRNJZTZSVjN
- http://trendyol.com/?q=YCARDZZZZ32719-

4. Ardından elimizde kalan bu listedeki URL'leri tek tek gezilmesi durumunda ise,

` python ReqFromList.py ` komutu ile urllere tek tek istek atılarak her biri yeni sekmede açılır.
