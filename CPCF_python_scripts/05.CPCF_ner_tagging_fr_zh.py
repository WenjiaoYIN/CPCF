import spacy

# 传入文件为utf-8编码的txt格式，写入文件为txt格式
# 获取法文NER
def get_ner_fr(file_input,file_output,file_res_output):
    nlp = spacy.load('fr_core_news_md')
    lines = open(file_input,"r", encoding='utf-8').readlines()

    with open(file_output,"w",encoding='utf-8') as f:
        with open(file_res_output,"w",encoding='utf-8') as f1:
            ent_labels = []
            ent_labels_unique = []
            for line in lines:
                doc = nlp(line.strip())
                ents = doc.ents
                f.write(line)
                f.write('{\n')
                for each_ent in ents:
                    f.write(f"{each_ent.text}_{each_ent.label_}\n")
                    ent_labels.append(each_ent.label_)
                    if each_ent.label_ not in ent_labels_unique:
                        ent_labels_unique.append(each_ent.label_)
                f.write('}\n')
                f.write('\n')
            f1.write("NER标签\t频数\n")
            ent_freq = {}
            for each_ent in ent_labels_unique:
                ent_freq[each_ent] = ent_labels.count(each_ent)
            items = list(ent_freq.items())
            sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
            for item in sorted_items:
                f1.write(f"{item[0]}\t{item[1]}\n")

# 获取中文NER和频数
def get_ner_zh(file_input,file_output,file_res_output):
    nlp = spacy.load('zh_core_web_md')
    lines = open(file_input,"r", encoding='utf-8').readlines()

    with open(file_output,"w",encoding='utf-8') as f:
        with open(file_res_output,"w", encoding='utf-8') as f1:
            ent_labels = []
            ent_labels_unique = []
            for line in lines:
                doc = nlp(line.strip())
                ents = doc.ents
                f.write(line)
                f.write('{\n')
                for each_ent in ents:
                    f.write(f"{each_ent.text}_{each_ent.label_}\n")
                    ent_labels.append(each_ent.label_)
                    if each_ent.label_ not in ent_labels_unique:
                        ent_labels_unique.append(each_ent.label_)
                f.write('}\n')
                f.write('\n')
            f1.write("NER标签\t频数\n")
            ent_freq = {}
            for each_ent in ent_labels_unique:
                ent_freq[each_ent] = ent_labels.count(each_ent)
            items = list(ent_freq.items())
            sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
            for item in sorted_items:
                f1.write(f"{item[0]}\t{item[1]}\n")