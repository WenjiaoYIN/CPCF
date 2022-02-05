import spacy

# 传入文件为utf-8编码的txt格式，写入文件为txt格式
# 获取法文句法标注
def get_parser_fr(file_input,file_output):
    nlp = spacy.load('fr_core_news_md')
    lines = open(file_input,"r", encoding='utf-8').readlines()

    with open(file_output,"w",encoding='utf-8') as f:
        for line in lines:
            doc = nlp(line.strip())
            for token in doc:
                f.write(f"{str(token.text)}_{str(token.dep_)}_{str(token.lemma_)} ")
            f.write('\n')

# 获取中文句法标注
def get_parser_zh(file_input,file_output):
    nlp = spacy.load('zh_core_web_md')
    lines = open(file_input,"r", encoding='utf-8').readlines()

    with open(file_output,"w",encoding='utf-8') as f:
        for line in lines:
            doc = nlp(line.strip())
            for token in doc:
                f.write(f"{str(token.text)}_{str(token.dep_)} ")
            f.write('\n')