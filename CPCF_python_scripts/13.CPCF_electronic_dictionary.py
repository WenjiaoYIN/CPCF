#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

# 每次查询一个中文词条时，使用一次该类
class CPCF_electronic_dictionary():
    def __init__(self,chinese_word):
        self.chinese_word = chinese_word

    # step 1: 匹配含有该中文单词的所有句子，并导出且统计数量:文件为_all_results.txt
    # 同时进行抽样：抽取出中文字符数<=20的句子：文件为_sample.txt
    # 同时导出替换了该词汇的文件：文件为_all_results_replaced.txt
    def get_1_all_sentences(self,chinese_word):
        self.chinese_word = chinese_word
        cfpc = open('CPCF_all_bilingual_utf-8.txt', "r", encoding='utf-8').readlines()

        # 所有含有该中文单词的句子
        count = 0
        with open('G:\\基于CPCF的词典\\' + str(chinese_word) + '_all_results.txt', "w", encoding='utf-8') as f:
            for each_line in cfpc:
                if str(chinese_word) in each_line:
                    f.write(each_line)
                    count += 1
            f.write('\n\n=================================================================\n')
            f.write(f"含有“{chinese_word}”的句子共有{count}句")

        # 中文字符<=20的句子
        with open('G:\\基于CPCF的词典\\' + str(chinese_word) + '_sample.txt', "w", encoding='utf-8') as f1:
            for each_line in cfpc:
                if str(chinese_word) in each_line:
                    chinese_line = each_line.split('|||')[0]
                    if len(chinese_line) <= 20:
                        f1.write(each_line)

        # 将所有中文单词替换为~且删除“|||”的句子，可直接用作例句
        with open('G:\\基于CPCF的词典\\' + str(chinese_word) + '_all_results_replaced.txt', "w", encoding='utf-8') as f2:
            for each_line in cfpc:
                if str(chinese_word) in each_line:
                    f2.write(each_line.replace(chinese_word, '~').replace('|||', ''))

    # step 2：获取一种或几种法文翻译的词频及其句子，基于已有的all_results_replaced文件
    # 最多可传入10种翻译方式
    def get_2_translation_freq(self,chinese_word, *french_translations):
        self.chinese_word = chinese_word
        self.french_translations = french_translations
        all_sentences = open('G:\\基于CPCF的词典\\' + str(chinese_word) + '_all_results_replaced.txt', "r",
                             encoding='utf-8').readlines()

        count = 0
        numbers = len(french_translations)
        with open('G:\\基于CPCF的词典\\' + str(chinese_word) + '_' + str(french_translations).replace('"',"'")[:200] + '.txt', "w",
                  encoding='utf-8') as f:
            for sentence in all_sentences:
                if numbers == 1:
                    if french_translations[0] in sentence or french_translations[0].upper() in sentence or \
                            french_translations[0].title() in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 2:
                    if french_translations[0] in sentence or french_translations[0].upper() in sentence or \
                            french_translations[0].title() in sentence \
                            or french_translations[1] in sentence or french_translations[1].upper() in sentence or \
                            french_translations[1].title() in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 3:
                    if french_translations[0] in sentence or french_translations[0].upper() in sentence or \
                            french_translations[0].title() in sentence \
                            or french_translations[1] in sentence or french_translations[1].upper() in sentence or \
                            french_translations[1].title() in sentence \
                            or french_translations[2] in sentence or french_translations[2].upper() in sentence or \
                            french_translations[2].title() in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 4:
                    if french_translations[0] in sentence or french_translations[0].upper() in sentence or \
                            french_translations[0].title() in sentence \
                            or french_translations[1] in sentence or french_translations[1].upper() in sentence or \
                            french_translations[1].title() in sentence \
                            or french_translations[2] in sentence or french_translations[2].upper() in sentence or \
                            french_translations[2].title() in sentence \
                            or french_translations[3] in sentence or french_translations[3].upper() in sentence or \
                            french_translations[3].title() in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 5:
                    if french_translations[0] in sentence or french_translations[0].upper() in sentence or \
                            french_translations[0].title() in sentence \
                            or french_translations[1] in sentence or french_translations[1].upper() in sentence or \
                            french_translations[1].title() in sentence \
                            or french_translations[2] in sentence or french_translations[2].upper() in sentence or \
                            french_translations[2].title() in sentence \
                            or french_translations[3] in sentence or french_translations[3].upper() in sentence or \
                            french_translations[3].title() in sentence \
                            or french_translations[4] in sentence or french_translations[4].upper() in sentence or \
                            french_translations[4].title() in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 6:
                    if french_translations[0] in sentence or french_translations[0].upper() in sentence or \
                            french_translations[0].title() in sentence \
                            or french_translations[1] in sentence or french_translations[1].upper() in sentence or \
                            french_translations[1].title() in sentence \
                            or french_translations[2] in sentence or french_translations[2].upper() in sentence or \
                            french_translations[2].title() in sentence \
                            or french_translations[3] in sentence or french_translations[3].upper() in sentence or \
                            french_translations[3].title() in sentence \
                            or french_translations[4] in sentence or french_translations[4].upper() in sentence or \
                            french_translations[4].title() in sentence \
                            or french_translations[5] in sentence or french_translations[5].upper() in sentence or \
                            french_translations[5].title() in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 7:
                    if french_translations[0] in sentence or french_translations[0].upper() in sentence or \
                            french_translations[0].title() in sentence \
                            or french_translations[1] in sentence or french_translations[1].upper() in sentence or \
                            french_translations[1].title() in sentence \
                            or french_translations[2] in sentence or french_translations[2].upper() in sentence or \
                            french_translations[2].title() in sentence \
                            or french_translations[3] in sentence or french_translations[3].upper() in sentence or \
                            french_translations[3].title() in sentence \
                            or french_translations[4] in sentence or french_translations[4].upper() in sentence or \
                            french_translations[4].title() in sentence \
                            or french_translations[5] in sentence or french_translations[5].upper() in sentence or \
                            french_translations[5].title() in sentence \
                            or french_translations[6] in sentence or french_translations[6].upper() in sentence or \
                            french_translations[6].title() in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 8:
                    if french_translations[0] in sentence or french_translations[0].upper() in sentence or \
                            french_translations[0].title() in sentence \
                            or french_translations[1] in sentence or french_translations[1].upper() in sentence or \
                            french_translations[1].title() in sentence \
                            or french_translations[2] in sentence or french_translations[2].upper() in sentence or \
                            french_translations[2].title() in sentence \
                            or french_translations[3] in sentence or french_translations[3].upper() in sentence or \
                            french_translations[3].title() in sentence \
                            or french_translations[4] in sentence or french_translations[4].upper() in sentence or \
                            french_translations[4].title() in sentence \
                            or french_translations[5] in sentence or french_translations[5].upper() in sentence or \
                            french_translations[5].title() in sentence \
                            or french_translations[6] in sentence or french_translations[6].upper() in sentence or \
                            french_translations[6].title() in sentence \
                            or french_translations[7] in sentence or french_translations[7].upper() in sentence or \
                            french_translations[7].title() in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 9:
                    if french_translations[0] in sentence or french_translations[0].upper() in sentence or \
                            french_translations[0].title() in sentence \
                            or french_translations[1] in sentence or french_translations[1].upper() in sentence or \
                            french_translations[1].title() in sentence \
                            or french_translations[2] in sentence or french_translations[2].upper() in sentence or \
                            french_translations[2].title() in sentence \
                            or french_translations[3] in sentence or french_translations[3].upper() in sentence or \
                            french_translations[3].title() in sentence \
                            or french_translations[4] in sentence or french_translations[4].upper() in sentence or \
                            french_translations[4].title() in sentence \
                            or french_translations[5] in sentence or french_translations[5].upper() in sentence or \
                            french_translations[5].title() in sentence \
                            or french_translations[6] in sentence or french_translations[6].upper() in sentence or \
                            french_translations[6].title() in sentence \
                            or french_translations[7] in sentence or french_translations[7].upper() in sentence or \
                            french_translations[7].title() in sentence \
                            or french_translations[8] in sentence or french_translations[8].upper() in sentence or \
                            french_translations[8].title() in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 10:
                    if french_translations[0] in sentence or french_translations[0].upper() in sentence or \
                            french_translations[0].title() in sentence \
                            or french_translations[1] in sentence or french_translations[1].upper() in sentence or \
                            french_translations[1].title() in sentence \
                            or french_translations[2] in sentence or french_translations[2].upper() in sentence or \
                            french_translations[2].title() in sentence \
                            or french_translations[3] in sentence or french_translations[3].upper() in sentence or \
                            french_translations[3].title() in sentence \
                            or french_translations[4] in sentence or french_translations[4].upper() in sentence or \
                            french_translations[4].title() in sentence \
                            or french_translations[5] in sentence or french_translations[5].upper() in sentence or \
                            french_translations[5].title() in sentence \
                            or french_translations[6] in sentence or french_translations[6].upper() in sentence or \
                            french_translations[6].title() in sentence \
                            or french_translations[7] in sentence or french_translations[7].upper() in sentence or \
                            french_translations[7].title() in sentence \
                            or french_translations[8] in sentence or french_translations[8].upper() in sentence or \
                            french_translations[8].title() in sentence \
                            or french_translations[9] in sentence or french_translations[9].upper() in sentence or \
                            french_translations[9].title() in sentence:
                        f.write(sentence)
                        count += 1
            f.write('\n\n=================================================================\n')
            f.write(
                f"含有“{french_translations}“的句子共有{count}句，占含有“{chinese_word}”句子的{(count / len(all_sentences)) * 100}%")

    # step3：获取除某些翻译外的句子，基于已有的all_results文件
    # 最多传入30种翻译方式
    def get_3_translation_except(self,chinese_word, *french_translations):
        self.chinese_word = chinese_word
        self.french_translations = french_translations
        all_sentences = open('G:\\基于CPCF的词典\\' + str(chinese_word) + '_all_results.txt', "r",
                             encoding='utf-8').readlines()[:-4]

        count = 0
        numbers = len(french_translations)
        with open('G:\\基于CPCF的词典\\' + str(chinese_word) + '_without_' + str(french_translations).replace('"',"'")[:200] + '.txt', "w",
                  encoding='utf-8') as f:
            for sentence in all_sentences:
                sentence = sentence.replace(chinese_word,"~").replace('|||',"")
                if numbers == 1:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and french_translations[0].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 2:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 3:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 4:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 5:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 6:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 7:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 8:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 9:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 10:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 11:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 12:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 13:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 14:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 15:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 16:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 17:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 18:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 19:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence \
                            and french_translations[18] not in sentence and french_translations[
                        18].upper() not in sentence and french_translations[18].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 20:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence \
                            and french_translations[18] not in sentence and french_translations[
                        18].upper() not in sentence and french_translations[18].title() not in sentence \
                            and french_translations[19] not in sentence and french_translations[
                        19].upper() not in sentence and french_translations[19].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 21:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence \
                            and french_translations[18] not in sentence and french_translations[
                        18].upper() not in sentence and french_translations[18].title() not in sentence \
                            and french_translations[19] not in sentence and french_translations[
                        19].upper() not in sentence and french_translations[19].title() not in sentence \
                            and french_translations[20] not in sentence and french_translations[
                        20].upper() not in sentence and french_translations[20].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 22:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence \
                            and french_translations[18] not in sentence and french_translations[
                        18].upper() not in sentence and french_translations[18].title() not in sentence \
                            and french_translations[19] not in sentence and french_translations[
                        19].upper() not in sentence and french_translations[19].title() not in sentence \
                            and french_translations[20] not in sentence and french_translations[
                        20].upper() not in sentence and french_translations[20].title() not in sentence \
                            and french_translations[21] not in sentence and french_translations[
                        21].upper() not in sentence and french_translations[21].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 23:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence \
                            and french_translations[18] not in sentence and french_translations[
                        18].upper() not in sentence and french_translations[18].title() not in sentence \
                            and french_translations[19] not in sentence and french_translations[
                        19].upper() not in sentence and french_translations[19].title() not in sentence \
                            and french_translations[20] not in sentence and french_translations[
                        20].upper() not in sentence and french_translations[20].title() not in sentence \
                            and french_translations[21] not in sentence and french_translations[
                        21].upper() not in sentence and french_translations[21].title() not in sentence \
                            and french_translations[22] not in sentence and french_translations[
                        22].upper() not in sentence and french_translations[22].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 24:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence \
                            and french_translations[18] not in sentence and french_translations[
                        18].upper() not in sentence and french_translations[18].title() not in sentence \
                            and french_translations[19] not in sentence and french_translations[
                        19].upper() not in sentence and french_translations[19].title() not in sentence \
                            and french_translations[20] not in sentence and french_translations[
                        20].upper() not in sentence and french_translations[20].title() not in sentence \
                            and french_translations[21] not in sentence and french_translations[
                        21].upper() not in sentence and french_translations[21].title() not in sentence \
                            and french_translations[22] not in sentence and french_translations[
                        22].upper() not in sentence and french_translations[22].title() not in sentence \
                            and french_translations[23] not in sentence and french_translations[
                        23].upper() not in sentence and french_translations[23].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 25:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence \
                            and french_translations[18] not in sentence and french_translations[
                        18].upper() not in sentence and french_translations[18].title() not in sentence \
                            and french_translations[19] not in sentence and french_translations[
                        19].upper() not in sentence and french_translations[19].title() not in sentence \
                            and french_translations[20] not in sentence and french_translations[
                        20].upper() not in sentence and french_translations[20].title() not in sentence \
                            and french_translations[21] not in sentence and french_translations[
                        21].upper() not in sentence and french_translations[21].title() not in sentence \
                            and french_translations[22] not in sentence and french_translations[
                        22].upper() not in sentence and french_translations[22].title() not in sentence \
                            and french_translations[23] not in sentence and french_translations[
                        23].upper() not in sentence and french_translations[23].title() not in sentence \
                            and french_translations[24] not in sentence and french_translations[
                        24].upper() not in sentence and french_translations[24].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 26:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence \
                            and french_translations[18] not in sentence and french_translations[
                        18].upper() not in sentence and french_translations[18].title() not in sentence \
                            and french_translations[19] not in sentence and french_translations[
                        19].upper() not in sentence and french_translations[19].title() not in sentence \
                            and french_translations[20] not in sentence and french_translations[
                        20].upper() not in sentence and french_translations[20].title() not in sentence \
                            and french_translations[21] not in sentence and french_translations[
                        21].upper() not in sentence and french_translations[21].title() not in sentence \
                            and french_translations[22] not in sentence and french_translations[
                        22].upper() not in sentence and french_translations[22].title() not in sentence \
                            and french_translations[23] not in sentence and french_translations[
                        23].upper() not in sentence and french_translations[23].title() not in sentence \
                            and french_translations[24] not in sentence and french_translations[
                        24].upper() not in sentence and french_translations[24].title() not in sentence \
                            and french_translations[25] not in sentence and french_translations[
                        25].upper() not in sentence and french_translations[25].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 27:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence \
                            and french_translations[18] not in sentence and french_translations[
                        18].upper() not in sentence and french_translations[18].title() not in sentence \
                            and french_translations[19] not in sentence and french_translations[
                        19].upper() not in sentence and french_translations[19].title() not in sentence \
                            and french_translations[20] not in sentence and french_translations[
                        20].upper() not in sentence and french_translations[20].title() not in sentence \
                            and french_translations[21] not in sentence and french_translations[
                        21].upper() not in sentence and french_translations[21].title() not in sentence \
                            and french_translations[22] not in sentence and french_translations[
                        22].upper() not in sentence and french_translations[22].title() not in sentence \
                            and french_translations[23] not in sentence and french_translations[
                        23].upper() not in sentence and french_translations[23].title() not in sentence \
                            and french_translations[24] not in sentence and french_translations[
                        24].upper() not in sentence and french_translations[24].title() not in sentence \
                            and french_translations[25] not in sentence and french_translations[
                        25].upper() not in sentence and french_translations[25].title() not in sentence \
                            and french_translations[26] not in sentence and french_translations[
                        26].upper() not in sentence and french_translations[26].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 28:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence \
                            and french_translations[18] not in sentence and french_translations[
                        18].upper() not in sentence and french_translations[18].title() not in sentence \
                            and french_translations[19] not in sentence and french_translations[
                        19].upper() not in sentence and french_translations[19].title() not in sentence \
                            and french_translations[20] not in sentence and french_translations[
                        20].upper() not in sentence and french_translations[20].title() not in sentence \
                            and french_translations[21] not in sentence and french_translations[
                        21].upper() not in sentence and french_translations[21].title() not in sentence \
                            and french_translations[22] not in sentence and french_translations[
                        22].upper() not in sentence and french_translations[22].title() not in sentence \
                            and french_translations[23] not in sentence and french_translations[
                        23].upper() not in sentence and french_translations[23].title() not in sentence \
                            and french_translations[24] not in sentence and french_translations[
                        24].upper() not in sentence and french_translations[24].title() not in sentence \
                            and french_translations[25] not in sentence and french_translations[
                        25].upper() not in sentence and french_translations[25].title() not in sentence \
                            and french_translations[26] not in sentence and french_translations[
                        26].upper() not in sentence and french_translations[26].title() not in sentence \
                            and french_translations[27] not in sentence and french_translations[
                        27].upper() not in sentence and french_translations[27].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 29:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence \
                            and french_translations[18] not in sentence and french_translations[
                        18].upper() not in sentence and french_translations[18].title() not in sentence \
                            and french_translations[19] not in sentence and french_translations[
                        19].upper() not in sentence and french_translations[19].title() not in sentence \
                            and french_translations[20] not in sentence and french_translations[
                        20].upper() not in sentence and french_translations[20].title() not in sentence \
                            and french_translations[21] not in sentence and french_translations[
                        21].upper() not in sentence and french_translations[21].title() not in sentence \
                            and french_translations[22] not in sentence and french_translations[
                        22].upper() not in sentence and french_translations[22].title() not in sentence \
                            and french_translations[23] not in sentence and french_translations[
                        23].upper() not in sentence and french_translations[23].title() not in sentence \
                            and french_translations[24] not in sentence and french_translations[
                        24].upper() not in sentence and french_translations[24].title() not in sentence \
                            and french_translations[25] not in sentence and french_translations[
                        25].upper() not in sentence and french_translations[25].title() not in sentence \
                            and french_translations[26] not in sentence and french_translations[
                        26].upper() not in sentence and french_translations[26].title() not in sentence \
                            and french_translations[27] not in sentence and french_translations[
                        27].upper() not in sentence and french_translations[27].title() not in sentence \
                            and french_translations[28] not in sentence and french_translations[
                        28].upper() not in sentence and french_translations[28].title() not in sentence:
                        f.write(sentence)
                        count += 1
                elif numbers == 30:
                    if french_translations[0] not in sentence and french_translations[0].upper() not in sentence and \
                            french_translations[0].title() not in sentence \
                            and french_translations[1] not in sentence and french_translations[
                        1].upper() not in sentence and french_translations[1].title() not in sentence \
                            and french_translations[2] not in sentence and french_translations[
                        2].upper() not in sentence and french_translations[2].title() not in sentence \
                            and french_translations[3] not in sentence and french_translations[
                        3].upper() not in sentence and french_translations[3].title() not in sentence \
                            and french_translations[4] not in sentence and french_translations[
                        4].upper() not in sentence and french_translations[4].title() not in sentence \
                            and french_translations[5] not in sentence and french_translations[
                        5].upper() not in sentence and french_translations[5].title() not in sentence \
                            and french_translations[6] not in sentence and french_translations[
                        6].upper() not in sentence and french_translations[6].title() not in sentence \
                            and french_translations[7] not in sentence and french_translations[
                        7].upper() not in sentence and french_translations[7].title() not in sentence \
                            and french_translations[8] not in sentence and french_translations[
                        8].upper() not in sentence and french_translations[8].title() not in sentence \
                            and french_translations[9] not in sentence and french_translations[
                        9].upper() not in sentence and french_translations[9].title() not in sentence \
                            and french_translations[10] not in sentence and french_translations[
                        10].upper() not in sentence and french_translations[10].title() not in sentence \
                            and french_translations[11] not in sentence and french_translations[
                        11].upper() not in sentence and french_translations[11].title() not in sentence \
                            and french_translations[12] not in sentence and french_translations[
                        12].upper() not in sentence and french_translations[12].title() not in sentence \
                            and french_translations[13] not in sentence and french_translations[
                        13].upper() not in sentence and french_translations[13].title() not in sentence \
                            and french_translations[14] not in sentence and french_translations[
                        14].upper() not in sentence and french_translations[14].title() not in sentence \
                            and french_translations[15] not in sentence and french_translations[
                        15].upper() not in sentence and french_translations[15].title() not in sentence \
                            and french_translations[16] not in sentence and french_translations[
                        16].upper() not in sentence and french_translations[16].title() not in sentence \
                            and french_translations[17] not in sentence and french_translations[
                        17].upper() not in sentence and french_translations[17].title() not in sentence \
                            and french_translations[18] not in sentence and french_translations[
                        18].upper() not in sentence and french_translations[18].title() not in sentence \
                            and french_translations[19] not in sentence and french_translations[
                        19].upper() not in sentence and french_translations[19].title() not in sentence \
                            and french_translations[20] not in sentence and french_translations[
                        20].upper() not in sentence and french_translations[20].title() not in sentence \
                            and french_translations[21] not in sentence and french_translations[
                        21].upper() not in sentence and french_translations[21].title() not in sentence \
                            and french_translations[22] not in sentence and french_translations[
                        22].upper() not in sentence and french_translations[22].title() not in sentence \
                            and french_translations[23] not in sentence and french_translations[
                        23].upper() not in sentence and french_translations[23].title() not in sentence \
                            and french_translations[24] not in sentence and french_translations[
                        24].upper() not in sentence and french_translations[24].title() not in sentence \
                            and french_translations[25] not in sentence and french_translations[
                        25].upper() not in sentence and french_translations[25].title() not in sentence \
                            and french_translations[26] not in sentence and french_translations[
                        26].upper() not in sentence and french_translations[26].title() not in sentence \
                            and french_translations[27] not in sentence and french_translations[
                        27].upper() not in sentence and french_translations[27].title() not in sentence \
                            and french_translations[28] not in sentence and french_translations[
                        28].upper() not in sentence and french_translations[28].title() not in sentence \
                            and french_translations[29] not in sentence and french_translations[
                        29].upper() not in sentence and french_translations[29].title() not in sentence:
                        f.write(sentence)
                        count += 1
            f.write('\n\n=================================================================\n')
            f.write(
                f"不含有{french_translations}的句子共有{count}句，占含有“{chinese_word}”句子的{(count / len(all_sentences)) * 100}%")

    # step4：将词条的多种释义进行标准化输出
    # 需要传入的是：义项、比例、例句*1
    # 发展@1. développement (81.77%) : 坚持新~理念。Maintenir le nouveau concept de développement.
    def get_4_entries(self,translation,ratio,example_sentence):
        self.translation = translation
        self.ratio = ratio
        self.example_sentence = example_sentence
        format = f"<b><font color='#1572A1'>{translation}</font></b> <sub>({ratio})</sub> : {example_sentence}"
        return str(format)

    # step5：每个词条建一个文件夹，最后统一合在一起就行
    # 普通词条，无需解释
    # <a href='dic://政府工作报告[例句1]'>例句</a>
    def get_5_electronic_dictionary_normal(self,chinese_word,*translations_sents):
        self.chinese_word = chinese_word
        self.translations_sents = translations_sents
        with open('G:\\基于CPCF的电子词典\\' + str(chinese_word) + '_electronic_dict.txt',"w",encoding='utf-8') as f:
            f.write(chinese_word)
            f.write('@')
            for translation_sent in translations_sents:
                index = translations_sents.index(translation_sent) + 1
                if translation_sent != translations_sents[-1]:
                    f.write(f"{index}. {translation_sent} <a href='dic://{chinese_word}[例句{index}]'>更多例句</a><br>")
                else:
                    f.write(f"{index}. {translation_sent} <a href='dic://{chinese_word}[例句{index}]'>更多例句</a>")

    # 需要加解释的缩写词条
    def get_5_electronic_dictionary_explain(self,chinese_word,explanation,*translations_sents):
        self.chinese_word = chinese_word
        self.explanation = explanation
        self.translations_sents = translations_sents
        with open('G:\\基于CPCF的电子词典\\' + str(chinese_word) + '_electronic_dict.txt',"w",encoding='utf-8') as f:
            # 词目
            f.write(chinese_word)
            f.write('@')
            f.write(f"即：<b><font color='#1572A1'>{explanation}</font></b>")
            f.write("<br>")
            for translation_sent in translations_sents:
                index = translations_sents.index(translation_sent) + 1
                if translation_sent != translations_sents[-1]:
                    f.write(f"{index}. {translation_sent} <a href='dic://{chinese_word}[例句{index}]'>更多例句</a><br>")
                else:
                    f.write(f"{index}. {translation_sent} <a href='dic://{chinese_word}[例句{index}]'>更多例句</a>")

    # step6：以输入的第一个translation作为词的义项，其他输入的参数为多种变位方式
    # 传入该单词的文件，并统计频数
    # 创建例句的文件
    # 政府工作报告[例句1]@共有例句14条：
    # 传入义项编号的数字
    def get_6_example_sentences(self,chinese_word,file_input,index):
        self.chinese_word = chinese_word
        self.file_input = file_input
        content = open(file_input,"r",encoding='utf-8').readlines()[:-4]
        number = len(content)

        with open('G:\\基于CPCF的电子词典\\【例句】'+ str(chinese_word) + '_' + str(index) + '_electronic_dict.txt',"w",encoding='utf-8') as f:
            f.write(chinese_word)
            f.write(f"[例句{index}]")
            f.write('@')
            f.write(f"<font color='#1572A1'>共有例句{number}条：</font><br>")
            for line in content:
                if line != content[-1]:
                    f.write(f"{content.index(line) + 1}. {line.strip()}<br>")
                else:
                    f.write(f"{content.index(line) + 1}. {line.strip()}")

    # 将without文件转换成例句格式
    def transfer_example_sentences(self,chinese_word,file_input):
        self.chinese_word = chinese_word
        self.file_input = file_input
        content = open(file_input,"r",encoding='utf-8').readlines()

        with open(file_input.replace('.txt','_replaced.txt'),"w",encoding='utf-8') as f:
            for line in content:
                f.write(line.replace(chinese_word,"~").replace('|||',''))

# step 7：将“基于CPCF的电子词典”文件夹中所有文件合并
# 存入“CPCF”文件夹中
def merge_electronic_dictionary():
    files = os.listdir('G:\\基于CPCF的电子词典')
    with open('CPCF_all_electronic_dictionary.txt',"w",encoding='utf-8') as f:
        for file in files:
            content = open('G:\\基于CPCF的电子词典\\' + file,"r",encoding='utf-8').readlines()
            for line in content:
                f.write(line)
                f.write('\n')


# 示例如下
if __name__ == '__main__':

    cpcf13 = CPCF_electronic_dictionary('决定性成就')
    cpcf13.get_1_all_sentences('决定性成就')
    cpcf13.get_2_translation_freq("决定性成就","la victoire décisive")
    cpcf13.get_2_translation_freq("决定性成就","succès décisif")
    cpcf13.get_2_translation_freq("决定性成就","accomplissements décisifs")
    entry1 = cpcf13.get_4_entries("la victoire décisive","33.33%","面对突如其来的新冠肺炎疫情、世界经济深度衰退等多重严重冲击，在以习近平同志为核心的党中央坚强领导下，全国各族人民顽强拼搏，疫情防控取得重大战略成果，在全球主要经济体中唯一实现经济正增长，脱贫攻坚战取得全面胜利，决胜全面建成小康社会取得~，交出一份人民满意、世界瞩目、可以载入史册的答卷。Face à l'apparition soudaine du COVID-19, à la récession profonde de l'économie mondiale et à d'autres chocs, notre peuple multiethnique, sous la ferme direction du Comité central du Parti rassemblé autour du camarade Xi Jinping, a mené une lutte opiniâtre. Des résultats stratégiques majeurs ont été obtenus dans la lutte contre le COVID-19, notre pays a été le seul parmi les principales économies du monde à réaliser une croissance positive, une victoire globale a été remportée dans la lutte contre la pauvreté, et des résultats substantiels ont été enregistrés pour remporter la victoire décisive de l'édification intégrale de la société de moyenne aisance. Ces accomplissements remarquables sont à la hauteur des attentes de notre peuple et méritent d'être inscrits dans les annales de l'histoire.")
    entry2 = cpcf13.get_4_entries("le succès décisif","33.33%","农村贫困人口减少1109万，贫困发生率降至0.6%，脱贫攻坚取得~。L'élimination de la pauvreté a remporté des succès décisifs : 11,09 millions de ruraux supplémentaires sont sortis de la pauvreté, et le taux de pauvreté a été réduit à 0,6 %.")
    entry3 = cpcf13.get_4_entries("l'accomplissement décisif","33.33%","脱贫攻坚历史使命如期完成，决胜全面建成小康社会取得~，实现第一个百年奋斗目标胜利在望。Nous avons accompli dans les délais prévus la mission historique d'éradiquer l'extrême pauvreté et réalisé des accomplissements décisifs dans l'édification intégrale de la société de moyenne aisance, et nous sommes sur la bonne voie de la réalisation de l'Objectif du premier Centenaire.")
    cpcf13.get_6_example_sentences("决定性成就","G:\\基于CPCF的词典\\决定性成就_('la victoire décisive',).txt",1)
    cpcf13.get_6_example_sentences("决定性成就","G:\\基于CPCF的词典\\决定性成就_('succès décisif',).txt",2)
    cpcf13.get_6_example_sentences("决定性成就","G:\\基于CPCF的词典\\决定性成就_('accomplissements décisifs',).txt",3)
    cpcf13.get_5_electronic_dictionary_normal("决定性成就",entry1,entry2,entry3)

    merge_electronic_dictionary()