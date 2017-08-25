# -*- coding: utf-8 -*

from gensim.models import word2vec

model = word2vec.Word2Vec.load('vector.bin')   #加载模型

#进一步训练其它语料
#model.train(more_sentences)


#20个最相关词
word = model.most_similar(u'中国',topn=20)
for item in word:
    print item[0], item[1]

#查看某个词的向量
#cosine = model[u'中国']
#print cosine

#相似概率
# cosine = model.similarity(u'中国', u'江苏')
# print u'相似度为:'
# print cosine

#找出不相似的词
#word = model.doesnt_match(u"语文 英语 网络".split())
#print word