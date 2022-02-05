# 传入文件为utf-8编码的txt格式，写入文件为txt格式
# 传入词性赋码后的文件
# 法文词性统计
def pos_freq_fr(file_input_pos,file_output):
    content_fr = open(file_input_pos,"r",encoding = 'utf-8').readlines()

    freq = []
    for each_line in content_fr:
        structure = each_line.split(' ')[:]
        for each in structure:
            try:
                pos = each.split('_')[1]
                freq.append(pos)
            except IndexError:
                pass

    freq_dict = {}
    for each_pos in freq:
        freq_dict[each_pos] = freq.count(each_pos)

    items = list(freq_dict.items())
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    with open(file_output,"w",encoding = 'utf-8') as f:
        f.write(f"POS\t\t频数\t\t占比\t\t\n")
        for each_item in sorted_items:
            f.write(f"{each_item[0]}\t\t{each_item[1]}\t\t{(each_item[1]/len(freq))*100}%\n")

# 中文词性统计
def pos_freq_zh(file_input_pos,file_output):
    content_zh = open(file_input_pos,"r",encoding = 'utf-8').readlines()

    freq = []
    for each_line in content_zh:
        structure = each_line.split(' ')[:]
        for each in structure:
            try:
                pos = each.split('_')[1]
                freq.append(pos)
            except IndexError:
                pass

    freq_dict = {}
    for each_pos in freq:
        freq_dict[each_pos] = freq.count(each_pos)

    items = list(freq_dict.items())
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

    with open(file_output,"w",encoding = 'utf-8') as f:
        f.write(f"POS\t\t频数\t\t占比\n")
        for each_item in sorted_items:
            f.write(f"{each_item[0]}\t\t{each_item[1]}\t\t{(each_item[1]/len(freq))*100}%\n")