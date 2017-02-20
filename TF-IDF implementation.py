#import required modules and packages
import os
import operator
from math import log10,sqrt
from collections import Counter
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#Regular expression used for tokenizing. Then stemming and stopword removal were performed
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
stemmer=PorterStemmer()
sw=stopwords.words('english')
dfs={}
idfs={}
sp={}
spv={}
ld=[]

#Function for tokenization
def tokenize(doc):
    doc=doc.lower()
    tokens=tokenizer.tokenize(doc)
    nonswtokens=[stemmer.stem(token) for token in tokens if token not in sw]
    return nonswtokens

#Function to calculate IDF
def incdfs(tfvec):
    for token in set(tfvec):
        if token not in dfs:
            dfs[token]=1
        else:
            dfs[token]+=1
            
#Function to read files from the corpus            
def readfiles(corpus_root):
    for filename in os.listdir(corpus_root):
        file = open(os.path.join(corpus_root, filename), "r", encoding='UTF-8')
        doc = file.read()
        file.close()
        tokens=tokenize(doc)
        tfvec=Counter(tokens)
        ld.append(dict(tfvec))
        sp[filename]=tfvec
        incdfs(tfvec)
    ndoc=len(sp)
    for token,df in dfs.items():
        idfs[token]= log10(ndoc/df)
    for filename,tfvec in sp.items():
        spv[filename]=caltfidfvec(tfvec)

#Function to find TF-IDF vector
def caltfidfvec(tfvec):
    tfidfvec={}
    vectorlength=0.0
    for token in tfvec:
        tfidf=(1+log10(tfvec[token]))*getidf(token)
        tfidfvec[token]=tfidf
        vectorlength+=pow(tfidf,2)
    if vectorlength>0:
        for token in tfvec:
            tfidfvec[token]/=sqrt(vectorlength)
    return tfidfvec

#Function to find cosine similarity
def cosinesim(vec1,vec2):
    commonterms=set(vec1).intersection(vec2)
    sim=0.0
    for token in commonterms:
        sim+=vec1[token]*vec2[token]
    return sim
#Function for cosine similarity between two document vectors
def docdocsim(filename1,filename2):
    return cosinesim(gettfidfvec(filename1),gettfidfvec(filename2))
    
def gettfidfvec(filename):
    return spv[filename]

#Function for cosine similarity between a document vector and a query vector
def query(qstring):
    tokens=tokenize(qstring)
    tfvec=Counter(tokens)
    qvec=caltfidfvec(tfvec)
    score={filename:cosinesim(qvec,tfidfvec) for filename,tfidfvec in spv.items()}
    return max(score.items(),key=operator.itemgetter(1))[0]

def getcount(token):
    count=0
    for d in ld:
        for k in d:
            if(k == token):
                count=count+d[k]
    return count

def getidf(token):
    if token not in idfs:
        return 0
    else:
        return idfs[token]
    
def querydocsim(qstring,filename):
    tokens=tokenize(qstring)
    tfvec=Counter(tokens)
    vectorlength=0.0
    tfidfvec={}
    for token in tfvec:
        tfidf=(1+log10(tfvec[token]))
        tfidfvec[token]=tfidf
        vectorlength+=pow(tfidf,2)
    if vectorlength>0:
        for token in tfvec:
            tfidfvec[token]/=sqrt(vectorlength)
    return cosinesim(tfidfvec,gettfidfvec(filename))

readfiles('E:\Data Mining\Assignments\Assignment1\presidential_debates')

print("%.12f" % docdocsim("1960-09-26.txt", "1980-09-21.txt"))
print(query("health insurance wall street"))
print(getcount("health"))
print("%.12f" % getidf("health"))
print("%.12f" % querydocsim("health insurance wall street", "1996-10-06.txt"))
querydocsim("health insurance wall street", "1996-10-06.txt")

#References
#https://docs.python.org/2/library/collections.html
#http://www.nltk.org
#https://docs.python.org/3/library/



    
