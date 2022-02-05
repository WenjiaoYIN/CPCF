import spacy

# 传入文件为utf-8编码的txt格式，写入文件为txt格式
# 计算法语文件中句子的平均句长
def sent_len_in_token_mean_fr(file_input,file_output):
    nlp = spacy.load('fr_core_news_md')
    content_fr = open(file_input,"r", encoding='utf-8').readlines()

    # 句子数量，因为和汉语对齐之后句子还有没有拆分的，要重新拆分一遍
    nlp_content = nlp(str(content_fr))
    sents = []
    for sent in nlp_content.sents:
        sents.append(sent)

    # 计算总token的数量
    # 和计算ttr和sttr里面的算法对齐，否则数据对不上
    tokens = []
    for each_sentence in content_fr:
        doc = nlp(each_sentence)
        for token in doc:
            tokens.append(token.text.lower())

    # mean = token总数/句子总数
    mean = len(tokens)/len(sents)

    with open(file_output,"w",encoding='utf-8') as f:
        f.write(f"这个文本中共有句子：{len(sents)}句\n")
        f.write(f"token总数为：{len(tokens)}\n")
        f.write(f"平均句长为：{mean}个token")