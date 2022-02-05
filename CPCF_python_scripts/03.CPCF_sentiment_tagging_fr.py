# 获取法语情感分析结果
def get_emotions_fr(file_input_pos,file_input_original,file_input_french_sentiment_dict,file_output):
    # 此处传入的是CPCF中经过词性赋码后的法文文本
    content_fr = open(file_input_pos, "r", encoding='utf-8').readlines()
    # 此处传入的是CPCF中没有任何赋码的法文文本
    content_fr_original = open(file_input_original, "r", encoding='utf-8').readlines()

    # 加载情感词典并建成字典
    # 情感词典为：CPCF_reference文件夹中的french_sentiment_dict.txt
    french_emotions = open(file_input_french_sentiment_dict).readlines()[1:]
    words_emotions = {}
    for line in french_emotions:
        word = line.split('\t')[0]
        emos = line.split('\t')[1]
        emotions = {}
        positivity = int(emos[1])
        joy = int(emos[3])
        fear = int(emos[5])
        sadness = int(emos[7])
        angry = int(emos[9])
        surprise = int(emos[11])
        disgust = int(emos[13])
        emotions['positivity'] = positivity
        emotions['joy'] = joy
        emotions['fear'] = fear
        emotions['sadness'] = sadness
        emotions['angry'] = angry
        emotions['surprise'] = surprise
        emotions['disgust'] = disgust
        words_emotions[word] = emotions

    with open(file_output, "w", encoding='utf-8') as f:
        for sentence in content_fr:
            sentence_original = content_fr_original[content_fr.index(sentence)]
            total = []
            positivity = 0
            joy = 0
            fear = 0
            sadness = 0
            angry = 0
            surprise = 0
            disgust = 0
            positivity_words = []
            joy_words = []
            fear_words = []
            sadness_words = []
            angry_words = []
            surprise_words = []
            disgust_words = []
            units = sentence.split(' ')
            for unit in units:
                lemma = unit.split('_')[-1]
                if lemma in words_emotions.keys():
                    emotion = words_emotions[lemma]
                    if emotion['positivity'] == 1:
                        positivity += 1
                        positivity_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
                    if emotion['joy'] == 1:
                        joy += 1
                        joy_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
                    if emotion['fear'] == 1:
                        fear += 1
                        fear_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
                    if emotion['sadness'] == 1:
                        sadness += 1
                        sadness_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
                    if emotion['angry'] == 1:
                        angry += 1
                        angry_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
                    if emotion['surprise'] == 1:
                        surprise += 1
                        surprise_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
                    if emotion['disgust'] == 1:
                        disgust += 1
                        disgust_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
            # 算法：每句话中单项情感的词的个数/带有情感的词的总个数
            try:
                d_positivity = positivity/len(total)
                d_joy = joy/len(total)
                d_fear = fear/len(total)
                d_sadness = sadness/len(total)
                d_angry = angry/len(total)
                d_surprise = surprise/len(total)
                d_disgust = disgust/len(total)
            except ZeroDivisionError:
                d_positivity = 0
                d_joy = 0
                d_fear = 0
                d_sadness = 0
                d_angry = 0
                d_surprise = 0
                d_disgust = 0
            f.write(sentence_original)
            f.write(f"positivity: {d_positivity}, joy: {d_joy}, fear: {d_fear}, sadness: {d_sadness}, "
                    f"angry: {d_angry}, surprise: {d_surprise}, disgust: {d_disgust}\n")
            f.write(f"positivity words\t{positivity_words}\njoy words\t{joy_words}\nfear words\t{fear_words}\nsadness words\t{sadness_words}\n"
                    f"angry words\t{angry_words}\nsurprise words\t{surprise_words}\ndisgust words\t{disgust_words}\n\n")

def get_emotions_res_fr(file_input_pos,file_input_original,file_input_french_sentiment_dict,file_output):
    content_fr = open(file_input_pos, "r", encoding='utf-8').readlines()
    content_fr_original = open(file_input_original, "r", encoding='utf-8').readlines()

    # 加载情感词典并建成字典
    french_emotions = open(file_input_french_sentiment_dict).readlines()[1:]
    words_emotions = {}
    for line in french_emotions:
        word = line.split('\t')[0]
        emos = line.split('\t')[1]
        emotions = {}
        positivity = int(emos[1])
        joy = int(emos[3])
        fear = int(emos[5])
        sadness = int(emos[7])
        angry = int(emos[9])
        surprise = int(emos[11])
        disgust = int(emos[13])
        emotions['positivity'] = positivity
        emotions['joy'] = joy
        emotions['fear'] = fear
        emotions['sadness'] = sadness
        emotions['angry'] = angry
        emotions['surprise'] = surprise
        emotions['disgust'] = disgust
        words_emotions[word] = emotions

    with open(file_output, "w", encoding='utf-8') as f:
        total_positivity = 0
        total_joy = 0
        total_fear = 0
        total_sadness = 0
        total_angry = 0
        total_surprise = 0
        total_disgust = 0
        for sentence in content_fr:
            total = []
            positivity = 0
            joy = 0
            fear = 0
            sadness = 0
            angry = 0
            surprise = 0
            disgust = 0
            positivity_words = []
            joy_words = []
            fear_words = []
            sadness_words = []
            angry_words = []
            surprise_words = []
            disgust_words = []
            units = sentence.split(' ')
            for unit in units:
                lemma = unit.split('_')[-1]
                if lemma in words_emotions.keys():
                    emotion = words_emotions[lemma]
                    if emotion['positivity'] == 1:
                        positivity += 1
                        positivity_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
                    if emotion['joy'] == 1:
                        joy += 1
                        joy_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
                    if emotion['fear'] == 1:
                        fear += 1
                        fear_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
                    if emotion['sadness'] == 1:
                        sadness += 1
                        sadness_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
                    if emotion['angry'] == 1:
                        angry += 1
                        angry_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
                    if emotion['surprise'] == 1:
                        surprise += 1
                        surprise_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
                    if emotion['disgust'] == 1:
                        disgust += 1
                        disgust_words.append(lemma)
                        if lemma not in total:
                            total.append(lemma)
            # 算法：每句话中单项情感个数/7项情感总个数
            try:
                d_positivity = positivity/len(total)
                d_joy = joy/len(total)
                d_fear = fear/len(total)
                d_sadness = sadness/len(total)
                d_angry = angry/len(total)
                d_surprise = surprise/len(total)
                d_disgust = disgust/len(total)
            except ZeroDivisionError:
                d_positivity = 0
                d_joy = 0
                d_fear = 0
                d_sadness = 0
                d_angry = 0
                d_surprise = 0
                d_disgust = 0
            if d_positivity != 0:
                total_positivity += 1
            if d_joy != 0:
                total_joy += 1
            if d_fear != 0:
                total_fear += 1
            if d_sadness != 0:
                total_sadness += 1
            if d_angry != 0:
                total_angry += 1
            if d_surprise != 0:
                total_surprise += 1
            if d_disgust != 0:
                total_disgust += 1

        f.write(f"类别\t行数\n")
        f.write(f"positivity\t{total_positivity}\njoy\t{total_joy}\nfear\t{total_fear}\nsadness\t{total_sadness}\n"
                f"angry\t{total_angry}\nsurprise\t{total_surprise}\ndisgust\t{total_disgust}\n")