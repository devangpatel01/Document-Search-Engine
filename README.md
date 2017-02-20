## TF-IDF implementation using python

### Project Description:

Implemented a toy search engine.The code reads a corpus and produces TF-IDF vectors for documents in the corpus. Then, given a query string, the code computes the cosine similarity between the query vector and the document vectors and return the document that gets the highest similarity score.

### Terminologies:

1) **TF-IDF** is the product of two statistics : Term Frequency (TF) and Inverse Document Frequency (IDF).  
2) **TF** is the number of times a term (word) occurs in a document.  
3) **IDF** is a numerical statistic that is intended to reflect how important a word is to a document.  
4) **Cosine Similarity** is the measure of similarity between two non-zero vectors of an inner product space that measures the cosine of   the angle between them. Cosine of 0° is 1 and it is less than 1 for any other angle.  
5) **Tokenization** is the act of breaking a sequence of strings into pieces (words or keywords).  
6) **Stemming** is the process of reducing inflected word to its word stem.  
7) **NLTK (Natural Language Toolkit)** is a suite of libraries and programs for symbolic and statistical Natural Language Processing (NLP) for English written in python programming language.  
8) **Collections** is the module in python implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.  
9) **Stop Words** are the words which donot contain important significance to the search queries.

### Formulas:
1) Cosine Similarity (d1, d2) =  Dot product(d1, d2) / ||d1|| * ||d2||  
   Dot product (d1,d2) = d1[0] * d2[0] + d1[1] * d2[1] * … * d1[n] * d2[n]  
   ||d1|| = square root(d1[0]2 + d1[1]2 + ... + d1[n]2)  
   ||d2|| = square root(d2[0]2 + d2[1]2 + ... + d2[n]2)  
2) Cosine Similarity(Query,Document1) = Dot product(Query, Document1) / ||Query|| * ||Document1||  

### References:
1) https://janav.wordpress.com/2013/10/27/tf-idf-and-cosine-similarity/  
2) https://en.wikipedia.org/wiki/Tf%E2%80%93idf#Term_frequency  
3) https://docs.python.org/2/library/collections.html  
4) http://www.nltk.org  
5) https://docs.python.org/3/library/  
