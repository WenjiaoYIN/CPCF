import spacy

# 传入文件为utf-8编码的txt格式，写入文件为txt格式
# 同时输出三个文件：原文件、lemmatization之后的文件、去掉停用词之后的文件
def word_freq_fr(file_input,file_output_raw,file_output_lemma,file_output_without_stop_words):
    # 未进行lemmatization
    nlp = spacy.load('fr_core_news_md')
    content_fr = open(file_input,"r",encoding='utf-8').readlines()
    # 类符
    types = []
    # 形符
    tokens = []
    # 此处计算类符形符比并未进行标准化，且未使用lemmatization之后的结果，是未经过处理的类符形符比

    for each_sentence in content_fr:
        doc = nlp(each_sentence)
        for token in doc:
            if token.text.lower() not in types:
                types.append(token.text.lower())
            tokens.append(token.text.lower())

    freq_fr = {}
    for type in types:
        freq_fr[type] = tokens.count(type)

    items = list(freq_fr.items())
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    # 未经处理的词频统计
    with open(file_output_raw,"w", encoding = 'utf-8') as f:
        f.write('单词\t\t词频\t\t占比\n')
        # 占比为占所有token数的比
        for item in sorted_items:
            f.write(f"{item[0]}\t\t{item[1]}\t\t{(item[1]/len(tokens))*100}%\n")

    # 进行lemmatization
    types_lemma = []
    tokens_lemma = []

    for each_sentence in content_fr:
        doc = nlp(each_sentence)
        for token in doc:
            lemma = token.lemma_
            if lemma not in types_lemma:
                types_lemma.append(lemma)
            tokens_lemma.append(lemma)

    freq_fr_lemma = {}
    for type_lemma in types_lemma:
        freq_fr_lemma[type_lemma] = tokens_lemma.count(type_lemma)

    items_lemma = list(freq_fr_lemma.items())
    sorted_items_lemma = sorted(items_lemma, key=lambda x: x[1], reverse=True)

    # lemmatization 之后的词频统计
    with open(file_output_lemma,"w", encoding = 'utf-8') as f:
        f.write('单词\t\t词频\t\t占比\n')
        # 占比为占所有token数的比
        for item_lemma in sorted_items_lemma:
            f.write(f"{item_lemma[0]}\t\t{item_lemma[1]}\t\t{(item_lemma[1]/len(tokens_lemma))*100}%\n")

    # 去掉标点符号和停用词和数字
    types_no_stop = []
    tokens_no_stop = []

    for each_sentence in content_fr:
        doc = nlp(each_sentence)
        for token in doc:
            if token.is_punct == False and token.is_stop == False and token.is_digit == False and token.is_space == False:
                token_no_stop = token.lemma_
                if token_no_stop not in types_no_stop:
                    types_no_stop.append(token_no_stop)
                tokens_no_stop.append(token_no_stop)

    freq_fr_no_stop = {}
    for type_no_stop in types_no_stop:
        freq_fr_no_stop[type_no_stop] = tokens_no_stop.count(type_no_stop)

    items_no_stop = list(freq_fr_no_stop.items())
    sorted_items_no_stop = sorted(items_no_stop, key=lambda x: x[1], reverse=True)

    with open(file_output_without_stop_words,"w", encoding = 'utf-8') as f:
        f.write('单词\t\t词频\t\t占比\n')
        # 占比为占所有token数的比
        for item_no_stop in sorted_items_no_stop:
            f.write(f"{item_no_stop[0]}\t\t{item_no_stop[1]}\t\t{(item_no_stop[1]/len(tokens_no_stop))*100}%\n")

# 同时输出两个文件：未作处理的文件、去掉停用词之后的文件
def word_freq_zh(file_input,file_output_raw,file_output_without_stop_words):
    nlp = spacy.load('zh_core_web_md')
    content_zh = open(file_input,"r", encoding='utf-8').readlines()
    # 未进行任何处理
    types = []
    tokens = []

    for each_sentence in content_zh:
        doc = nlp(each_sentence)
        for token in doc:
            text = token.text
            if text not in types:
                types.append(text)
            tokens.append(text)

    freq_zh = {}
    for type in types:
        freq_zh[type] = tokens.count(type)

    items = list(freq_zh.items())
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    # 未经处理的词频统计
    with open(file_output_raw,"w", encoding='utf-8') as f:
        f.write('单词\t\t词频\t\t占比\n')
        # 占比为占所有token数的比
        for item in sorted_items:
            f.write(f"{item[0]}\t\t{item[1]}\t\t{(item[1] / len(tokens)) * 100}%\n")

    # 删掉停用词、标点等
    types_no_stop = []
    tokens_no_stop = []

    for each_sentence in content_zh:
        doc = nlp(each_sentence)
        for token in doc:
            if token.is_punct == False and token.is_stop == False and token.is_digit == False and token.is_space == False:
                text_no_stop = token.text
                if text_no_stop not in types_no_stop:
                    types_no_stop.append(text_no_stop)
                tokens_no_stop.append(text_no_stop)

    freq_zh_no_stop = {}

    for type_no_stop in types_no_stop:
        freq_zh_no_stop[type_no_stop] = tokens_no_stop.count(type_no_stop)

    items_no_stop = list(freq_zh_no_stop.items())
    sorted_items_no_stop = sorted(items_no_stop, key=lambda x: x[1], reverse=True)

    with open(file_output_without_stop_words,"w", encoding = 'utf-8') as f:
        f.write('单词\t\t词频\t\t占比\n')
        # 占比为占所有token数的比
        for item_no_stop in sorted_items_no_stop:
            f.write(f"{item_no_stop[0]}\t\t{item_no_stop[1]}\t\t{(item_no_stop[1]/len(tokens_no_stop))*100}%\n")