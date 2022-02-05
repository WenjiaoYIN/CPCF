import spacy
import jieba

# 传入文件为utf-8编码的txt格式，写入文件为txt格式
# 使用spacy进行中文分词
def chinese_tokenization(file_input,file_output):
    content_zh = open(file_input,"r",encoding = 'utf-8').readlines()
    nlp = spacy.load('zh_core_web_md')

    with open(file_output,"w",encoding = 'utf-8') as f:
        for sentence in content_zh:
            doc = nlp(sentence)
            for token in doc:
                f.write(f"{token} ")

# 使用spacy进行法文分词
def french_tokenization(file_input,file_output):
    content_fr = open(file_input,"r",encoding = 'utf-8').readlines()
    nlp = spacy.load('fr_core_news_md')

    with open(file_output,"w",encoding = 'utf-8') as f:
        for sentence in content_fr:
            doc = nlp(sentence)
            for token in doc:
                f.write(f"{token} ")

# 使用jieba进行中文分词
def chinese_tokenization_jieba(file_input,file_output):
    content_zh = open(file_input,"r",encoding = 'utf-8').readlines()

    with open(file_output,"w",encoding = 'utf-8') as f:
        for sentence in content_zh:
            seg_list = jieba.cut(sentence,cut_all=False) # 精确模式
            f.write(' '.join(seg_list))