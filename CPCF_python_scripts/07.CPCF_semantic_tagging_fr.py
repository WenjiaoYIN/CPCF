# 获取法语语义标注
# 传入想要获取的类型，大写英文字母，后面可以加数字和符号，字符串格式
# 只进行优先匹配（默认先匹配第一位传入的type），不做完全匹配：可以导出结果之后自行查找
# 导出两份文件：进行语义标注的文件，格式lemma_semantic；进行语义统计的文件
# 最好只传入一个type，这是最准确的，否则结果可能不准，格式为字符串格式
def get_semantic_fr(file_input_pos,file_input_semantic_lexicon,file_input_semantic_terms,file_output,file_res_output,*types):
    content_fr = open(file_input_pos,"r",encoding='utf-8').readlines()

    # 字典位置：CPCF_reference文件夹中的french_semantic_lexicon.txt
    # 加载法语语义标注为字典格式
    french_semantic_lexicon = open(file_input_semantic_lexicon, "r", encoding='utf-8').readlines()[1:]
    french_semantic_dict = {}
    for each_line in french_semantic_lexicon:
        word = each_line.split('\t')[0].strip()
        semantic = each_line.split('\t')[2].strip()
        french_semantic_dict[word] = semantic

    # 将多种内容的进行分隔
    for item, value in french_semantic_dict.items():
        if '/' in value:
            values = value.split('/')
            french_semantic_dict[item] = values
        else:
            pass

    # 字典位置：CPCF_reference文件夹中的french_semantic_terms.txt
    # 加载法语语义标注说明为字典格式
    french_semantic_des = open(file_input_semantic_terms, "r", encoding='gbk').readlines()
    french_semantic_des_dict = {}
    for each in french_semantic_des:
        tag = each.split('\t')[0].strip()
        des = each.split('\t')[1].strip()
        french_semantic_des_dict[tag] = des

    # 储存semantic的值并进行统计
    semantics = []

    with open(file_output,"w",encoding='utf-8') as f:
        for line in content_fr:
            units = line.split(' ')
            # 提取出lemma
            for unit in units:
                lemma = unit.split('_')[-1].strip()
                # 如果lemma位于词典之中，就把它的格式转换为：lemma_semantic
                if lemma in french_semantic_dict.keys():
                    value = french_semantic_dict[lemma]
                    # 判断value的类型是字符串（对应一个结果）还是列表（对应多个结果）
                    if type(value) == str:
                        # 直接导出结果，不做判断
                        semantics.append(value)
                        semantic_output = lemma + '_' + value
                    elif type(value) == list:
                        # 如果有传入的类型，就优先选择标注传入的类型
                        count_value = 0
                        count_types = 0
                        if types:
                            # 判断每一种传入的type
                            for t in types:
                                # 判断每一个结果
                                for v in value:
                                    # 如果有一个匹配了，就停止循环
                                    if t in v:
                                        semantics.append(v)
                                        semantic_output = lemma + '_' + v
                                        break
                                    # 否则就进行计数
                                    else:
                                        count_value += 1
                                # 如果计数等于value的长度，说明在这个循环中没有与value匹配的type，计数+=1并且进入下一个type的循环
                                if len(value) == count_value:
                                    count_types += 1
                            # 如果计数等于types的长度，说明所有循环中都没有符合条件的value值，直接输出第一项结果
                            if len(types) == count_types:
                                v = value[0]
                                semantics.append(v)
                                semantic_output = lemma + '_' + v
                        # 如果没有传入的类型，就默认第一项作为标注类型
                        else:
                            v = value[0]
                            semantics.append(v)
                            semantic_output = lemma + '_' + v
                    f.write(f"{semantic_output} ")
                # 如果lemma不在词典中，就直接输出lemma
                else:
                    f.write(f"{lemma} ")
            f.write('\n')

    with open(file_res_output,"w",encoding='utf-8') as f1:
        f1.write('标签\t含义\t频数\n')
        for tag,des in french_semantic_des_dict.items():
            if tag in semantics:
                num = semantics.count(tag)
                f1.write(f"{tag}\t{des}\t{num}\n")
            else:
                f1.write(f"{tag}\t{des}\t0\n")
    print(types)
    print(len(semantics))
    # print(semantics)

# 传入的文件是进行了语义标注后的文件
# 获取某个type对应的所有单词
def get_type_words(file_input,file_output,type):
    content = open(file_input,"r",encoding='utf-8').readlines()

    words = []
    for line in content:
        units = line.split(' ')
        for unit in units:
            if type in unit:
                word = unit.split('_')[0]
                words.append(word)

    # 不重复的词表
    words_unique = []
    for w in words:
        if w not in words_unique:
            words_unique.append(w)

    # 词表及频率
    words_freq = {}
    for each_w in words_unique:
        words_freq[each_w] = words.count(each_w)

    # 进行排序
    items = list(words_freq.items())
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    with open(file_output,"w",encoding='utf-8') as f:
        f.write('这项结果基于对' + type + '作为语义优先标注的结果而进行词频排序\n')
        f.write('单词\t频数\n')
        for key,value in sorted_items:
            f.write(f"{key}\t{value}\n")