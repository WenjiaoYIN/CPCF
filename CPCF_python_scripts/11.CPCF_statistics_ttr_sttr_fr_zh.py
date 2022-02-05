import spacy

# 传入文件为utf-8编码的txt格式，写入文件为txt格式
# 未标准化处理的类符形符比，未进行lemmatization
def type_token_ratio_fr(file_input,file_output):
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

    type_number = len(types)
    token_number = len(tokens)
    line_number = len(content_fr)

    with open(file_output,"w", encoding='utf-8') as f:
        f.write(f"文本中共含有句子行数：{line_number}\n"
        f"文本中共含有类符（type）数：{type_number}\n"
        f"文本中共含有形符（token）数：{token_number}\n"
        f"文本的类符/形符比（TTR）为：{(type_number/token_number)*100}%")

# 进行标准化处理的类符形符比，未进行lemmatization
def standardized_type_token_ratio_fr(file_input,file_output):
    nlp = spacy.load('fr_core_news_md')
    content_fr = open(file_input,"r",encoding='utf-8').readlines()
    # 类符
    types = []
    # 形符
    tokens = []

    ratios = []

    for each_sentence in content_fr:
        doc = nlp(each_sentence)
        for token in doc:
            if len(tokens) <= 1000:
                if token.text.lower() not in types:
                    types.append(token.text.lower())
                tokens.append(token.text.lower())
            else:
                ratio = (len(types)/len(tokens))*100
                ratios.append(ratio)
                types = []
                tokens = []
                if token.text.lower() not in types:
                    types.append(token.text.lower())
                tokens.append(token.text.lower())

    line_number = len(content_fr)
    sum = 0
    for ratio in ratios:
        sum += ratio
    try:
        ratio = sum / len(ratios)
    except ZeroDivisionError:
        ratio = (len(types)/len(tokens))*100

    ratios_with_percent = []
    for each_ratio in ratios:
        each_ratio_percent = str(each_ratio) + '%'
        ratios_with_percent.append(each_ratio_percent)


    with open(file_output,"w", encoding = 'utf-8') as f:
        f.write(f"文本中共含有句子行数：{line_number}\n")
        f.write('文本中的每千词类符/形符比（TTR）为：\n')
        for ratio_with_percent in ratios_with_percent:
            f.write(f"{ratio_with_percent}\n")
        f.write(f"文本的标准化类符/形符比（STTR）为：{ratio}%")

# 未标准化处理的类符形符比
def type_token_ratio_zh(file_input,file_output):
    nlp = spacy.load('zh_core_web_md')
    content_zh = open(file_input,"r",encoding='utf-8').readlines()
    # 类符
    types = []
    # 形符
    tokens = []
    # 此处计算类符形符比并未进行标准化，且未使用lemmatization之后的结果，是未经过处理的类符形符比

    for each_sentence in content_zh:
        doc = nlp(each_sentence)
        for token in doc:
            if token.text.lower() not in types:
                types.append(token.text.lower())
            tokens.append(token.text.lower())

    type_number = len(types)
    token_number = len(tokens)
    line_number = len(content_zh)

    with open(file_output,"w", encoding = 'utf-8') as f:
        f.write(f"文本中共含有句子行数：{line_number}\n"
        f"文本中共含有类符（type）数：{type_number}\n"
        f"文本中共含有形符（token）数：{token_number}\n"
        f"文本的类符/形符比（TTR）为：{(type_number/token_number)*100}%")

# 进行标准化处理的类符形符比，未进行lemmatization
def standardized_type_token_ratio_zh(file_input,file_output):
    nlp = spacy.load('zh_core_web_md')
    content_zh = open(file_input,"r", encoding='utf-8').readlines()
    # 类符
    types = []
    # 形符
    tokens = []

    ratios = []

    for each_sentence in content_zh:
        doc = nlp(each_sentence)
        for token in doc:
            if len(tokens) <= 1000:
                if token.text.lower() not in types:
                    types.append(token.text.lower())
                tokens.append(token.text.lower())
            else:
                ratio = (len(types) / len(tokens)) * 100
                ratios.append(ratio)
                types = []
                tokens = []
                if token.text.lower() not in types:
                    types.append(token.text.lower())
                tokens.append(token.text.lower())

    line_number = len(content_zh)
    sum = 0
    for ratio in ratios:
        sum += ratio
    try:
        ratio = sum / len(ratios)
    except ZeroDivisionError:
        ratio = (len(types)/len(tokens))*100

    ratios_with_percent = []
    for each_ratio in ratios:
        each_ratio_percent = str(each_ratio) + '%'
        ratios_with_percent.append(each_ratio_percent)

    with open(file_output,"w", encoding='utf-8') as f:
        f.write(f"文本中共含有句子行数：{line_number}\n")
        f.write('文本中的每千词类符/形符比（TTR）为：\n')
        for ratio_with_percent in ratios_with_percent:
            f.write(f"{ratio_with_percent}\n")
        f.write(f"文本的标准化类符/形符比（STTR）为：{ratio}%")