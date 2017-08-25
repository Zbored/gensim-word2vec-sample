# -*- coding: utf-8 -*
import jieba,re,os
from gensim.models import word2vec
import logging

def SplitSentence(inputfile,fout):      #语料处理：去符号，分词
    fin = open(inputfile,'r')
    for line in fin:
        line1 = line.strip().decode('utf-8','ignore')
        line2 = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*“”➕「」《》（）]+".decode("utf-8"), "".decode("utf-8"), line1)
        wordlist = list(jieba.cut(line2))
        outstr = ''
        for word in wordlist:
            outstr += word
            outstr += ' '
        fout.write(outstr.strip().encode('utf-8')+'\n')
    fin.close()

def TextLoader(dir):
    fout = open('SplitSentence.txt', 'w')
    for root, dirs, files in os.walk(dir):      # 遍历所有文件夹
        for file in files:
            inputfile = os.path.join(root, file)
            print inputfile     #打印文件记录
            SplitSentence(inputfile,fout)   #处理该文件
    fout.close()

def Training():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)   #打印日志
    sentences = word2vec.Text8Corpus('SplitSentence.txt')  # 加载语料
    model = word2vec.Word2Vec(sentences)  # 训练skip-gram模型; 默认参数
    model.save('vector.bin')
#model = word2vec.Word2Vec(sentences, sg=1, size=100, window=5, min_count=5, negative=3, sample=0.001, hs=1, workers=4)
#
# sentences：可以是一个list，对于大语料集，建议使用BrownCorpus,Text8Corpus或·ineSentence构建。
#
# sg：用于设置训练算法，默认为0，对应CBOW算法；sg=1则采用skip-gram算法,对低频词敏感；默认sg=0为CBOW算法。
#
# size是输出词向量的维数，值太小会导致词映射因为冲突而影响结果，值太大则会耗内存并使算法计算变慢，一般值取为几十到几百之间。默认为100
#
# window是句子中当前词与目标词之间的最大距离，3表示在目标词前看3-b个词，后面看b个词（b在0-3之间随机）。
#
# min_count是对词进行过滤，频率小于min-count的单词则会被忽视，默认值为5。
#
# negative和sample可根据训练结果进行微调，sample表示更高频率的词被随机下采样到所设置的阈值，默认值为1e-3。
#
# hs=1表示层级softmax将会被使用，默认hs=0且negative不为0，则负采样将会被选择使用。
#
# workers控制训练的并行，此参数只有在安装了Cpython后才有效，否则只能使用单核。

if __name__ == "__main__":
    TextLoader('text/')     #语料目录
    Training()
    pass