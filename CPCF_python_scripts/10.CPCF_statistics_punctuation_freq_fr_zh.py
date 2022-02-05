import re

# 传入文件为utf-8编码的txt格式，写入文件为txt格式
# 获得法文标点符号统计
def get_punctuation_fr(file_input,file_output):
    content_fr = open(file_input,"r", encoding='utf-8').readlines()

    punctuations_fr = ['.',';',':','!','?',',','-','–','—','«','»','/','’','…','...','(',')','[',']','"',"'"]

    with open(file_output,"w", encoding='utf-8') as f:
        f.write('标点符号\t频数\n')
        for punctuation_fr in punctuations_fr:
            if punctuation_fr in str(content_fr):
                if punctuation_fr == '.':
                    pattern = re.compile(r'\.')
                    result = pattern.findall(str(content_fr))
                    print(punctuation_fr, len(result))
                    f.write(f"{punctuation_fr}\t{len(result)}\n")
                elif punctuation_fr == '(':
                    pattern = re.compile(r'\(')
                    result = pattern.findall(str(content_fr))
                    print(punctuation_fr, len(result))
                    f.write(f"{punctuation_fr}\t{len(result)}\n")
                elif punctuation_fr == ')':
                    pattern = re.compile(r'\)')
                    result = pattern.findall(str(content_fr))
                    print(punctuation_fr, len(result))
                    f.write(f"{punctuation_fr}\t{len(result)}\n")
                elif punctuation_fr == '[':
                    pattern = re.compile(r'\[')
                    result = pattern.findall(str(content_fr))
                    print(punctuation_fr, len(result)-1)
                    f.write(f"{punctuation_fr}\t{len(result)-1}\n")
                elif punctuation_fr == ']':
                    pattern = re.compile(punctuation_fr)
                    result = pattern.findall(str(content_fr))
                    print(punctuation_fr, len(result)-1)
                    f.write(f"{punctuation_fr}\t{len(result)-1}\n")
                elif punctuation_fr == '?':
                    pattern = re.compile(r'\?')
                    result = pattern.findall(str(content_fr))
                    print(punctuation_fr, len(result))
                    f.write(f"{punctuation_fr}\t{len(result)}\n")
                elif punctuation_fr == '...':
                    pattern = re.compile(r'(\.{3})')
                    result = pattern.findall(str(content_fr))
                    print(punctuation_fr, len(result))
                    f.write(f"{punctuation_fr}\t{len(result)}\n")
                elif punctuation_fr == "'":
                    count = 0
                    for item in content_fr:
                        if "'" in item[1:-2]:
                            count += 1
                    all = len(content_fr) - count
                    pattern = re.compile(punctuation_fr)
                    result = pattern.findall(str(content_fr))
                    print(punctuation_fr, len(result)-2*all)
                    f.write(f"{punctuation_fr}\t{len(result)-2*all}\n")
                elif punctuation_fr == '"':
                    count = 0
                    for item in content_fr:
                        if "'" in item[1:-2]:
                            count += 1
                    all = 2*count
                    pattern = re.compile(punctuation_fr)
                    result = pattern.findall(str(content_fr))
                    print(punctuation_fr, len(result)-all)
                    f.write(f"{punctuation_fr}\t{len(result)-all}\n")
                else:
                    pattern = re.compile(punctuation_fr)
                    result = pattern.findall(str(content_fr))
                    print(punctuation_fr,len(result))
                    f.write(f"{punctuation_fr}\t{len(result)}\n")
            else:
                print(punctuation_fr)
                f.write(f"{punctuation_fr}\t0\n")

# 获得中文标点符号统计
def get_punctuation_zh(file_input,file_output):
    content_zh = open(file_input,"r", encoding='utf-8').readlines()

    punctuations_zh = ['。','；','：','！','？','，','-','—','“','”','/','……','......','（','）','[',']','、','‘','’','「','」',
                       '『','』','〔','〕','【','】','——','～','《','》','〈','〉','·']

    with open(file_output,"w", encoding='utf-8') as f:
        f.write('标点符号\t频数\n')
        for punctuation_zh in punctuations_zh:
            if punctuation_zh in str(content_zh):
                if punctuation_zh == '[':
                    pattern = re.compile(r'\[')
                    result = pattern.findall(str(content_zh))
                    print(punctuation_zh, len(result)-1)
                    f.write(f"{punctuation_zh}\t{len(result)-1}\n")
                elif punctuation_zh == ']':
                    pattern = re.compile(punctuation_zh)
                    result = pattern.findall(str(content_zh))
                    print(punctuation_zh, len(result)-1)
                    f.write(f"{punctuation_zh}\t{len(result)-1}\n")
                elif punctuation_zh == '......':
                    pattern = re.compile(r'(\.{6})')
                    result = pattern.findall(str(content_zh))
                    print(punctuation_zh, len(result))
                    f.write(f"{punctuation_zh}\t{len(result)}\n")
                else:
                    pattern = re.compile(punctuation_zh)
                    result = pattern.findall(str(content_zh))
                    print(punctuation_zh, len(result))
                    f.write(f"{punctuation_zh}\t{len(result)}\n")
            else:
                print(punctuation_zh)
                f.write(f"{punctuation_zh}\t0\n")