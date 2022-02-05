import spacy

# 传入文件为utf-8编码的txt格式，写入文件为txt格式
# 获得法文形态标注
def get_morph_fr(file_input,file_output):
    nlp = spacy.load('fr_core_news_md')
    lines = open(file_input,"r", encoding='utf-8').readlines()

    with open(file_output,"w", encoding='utf-8') as f:
        for line in lines:
            doc = nlp(line.strip())
            for token in doc:
                f.write(f"{str(token.text)}_{str(token.morph)}_{str(token.lemma_)} ")
            f.write('\n')

# 获得某个特定的法文形态标注
# 同时输出两个文件，分别是标注文件和结果文件，certain_type为特定的法文形态，格式是字符串格式
def get_certain_morph_fr(file_input,file_output,file_res_output,certain_type):
    nlp = spacy.load('fr_core_news_md')
    lines = open(file_input,"r", encoding='utf-8').readlines()

    with open(file_output,"w", encoding='utf-8') as f:
        with open(file_res_output,"w", encoding='utf-8') as f1:
            types = []
            types_unique = []
            for line in lines:
                doc = nlp(line.strip())
                for token in doc:
                    if token.morph.get(certain_type):
                        f.write(f"{str(token.text)}_{str(token.morph.get(certain_type))} ")
                        types.append(token.morph.get(certain_type))
                        if token.morph.get(certain_type) not in types_unique:
                            types_unique.append(token.morph.get(certain_type))
                    else:
                        f.write(f"{str(token.text)} ")
                f.write('\n')
            # 输出统计结果
            f1.write(f"这项结果是对{certain_type}获取的结果统计\n")
            type_freq = {}
            for each_type in types_unique:
                freq = types.count(each_type)
                type_freq[str(each_type)] = freq
            items = list(type_freq.items())
            sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
            for item in sorted_items:
                f1.write(f"{item[0][2:-2]}\t{item[1]}\n")