import os
import re
from deep_translator import GoogleTranslator
from deep_translator import MyMemoryTranslator

# get all files in the current path
working_directory = os.getcwd()
enable_translate = False
source_language = "english"
target_language = "simp_chinese"

# tranlate english to chinese
def translate_to_chinese(line: str):
    try:
        # translator = GoogleTranslator(source='en', target='zh-CN')
        translator = MyMemoryTranslator(source='en', target='zh-CN')
        result = translator.translate(line)
    except Exception as e:
        print('translate error: ' + e)
        return translate_to_chinese(line)
    else:        
        print('the sentences that need to be translated are: ' + line)
        print('the results that need to be translated are: ' + result)
        return result
        # return line + r'\n' + result

# 我意识到这是一个假的批量接口，😵
# tranlate english to chinese
def translate_to_chinese_batch(line_list: list[str]):
    try:
        # translator = GoogleTranslator(source='en', target='zh-CN')
        translator = MyMemoryTranslator(source='en', target='zh-CN')
        result_list = translator.translate_batch(line_list)
        # return a dict, key is line_list, value is result_list
        result = dict(zip(line_list, result_list))
    except Exception as e:
        print('translate error: ' + e)
        return translate_to_chinese_batch(line_list)
    else:        
        print('the sentences that need to be translated are: ' + line_list)
        print('the results that need to be translated are: ' + result_list)
        return result

# 游戏内有一些表达式不应该被翻译，使用这个方法正则判断
def is_english_and_punctuation(s):
    pattern = r'[#$[]()]'
    return not bool(re.match(pattern, s))

# write a method for converting the string from 'english.yml' to 'simp_chinese.yml'
def convert_file(file_path: str, file_name: str):
    new_file_name =  file_name.replace(source_language + '.yml', target_language + '.yml')
    new_file_path = file_path.replace(os.path.join('localization', source_language), os.path.join('localization', target_language))

    if not os.path.isdir(new_file_path):
        os.makedirs(new_file_path, exist_ok=True)

    old_file = os.path.join(file_path, file_name)
    new_file = os.path.join(new_file_path, new_file_name)

    with open(old_file, 'r', encoding='utf-8') as src_file, open(new_file, 'w', encoding='utf-8') as dest_file:
        # if file content is null, skip it
        if not src_file.readable():
            return
        
        if not dest_file.writable():
            return

        src_content = {}
        desc_list = []
        i = -1
        # dest_file.write(src_file.readline())
        for line in src_file:
            i = i + 1
            # 文件第一行替换
            if 'l_' + source_language + ':' in line:
                src_content[i] = {'content': line.replace('l_' + source_language + ':', 'l_' + target_language + ':')}
                continue
            # 直接添加空行之类的特殊行
            if ':' not in line:
                src_content[i] = {'content': line}
                continue

            start_with = line.index(':')

            if len(line) < start_with + 4:
                src_content[i] = {'content': line}
                continue

            # 从引号开始截取需要翻译的内容
            desc = line[start_with + 4 : -2]

            if not is_english_and_punctuation(desc):
                src_content[i] = {'content': line}
                continue

            src_content[i] = {
                'content': line,
                'desc': desc
            }
            desc_list.append(desc)
            # dest_file.write(line.replace(desc, translate_to_chinese(desc)))
            continue

        if enable_translate:
            result_dict = translate_to_chinese_batch(desc_list)
            for [key, value] in src_content.items():
                if 'desc' in value:
                    dest_file.write(value['content'].replace(value['desc'], result_dict[value['desc']]))
                else:
                    dest_file.write(value['content'])
        else:
            dest_file.writelines([src_content[value]['content'] for value in src_content])

    print('file name being save to ' + new_file + ' ...')
    return


def get_all_files(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(source_language + '.yml'):
                file_list.append(os.path.join(root, file))
            else:
                print('this file is special file - ' + os.path.join(root, file))
    return file_list

# print(response.text)

# 判断是否为mod目录
# determine if descriptor.mod file exists in the current folder
descriptor_path = os.path.join(working_directory, 'descriptor.mod')
if False == os.path.isfile(descriptor_path):
    print('file not exists')
    exit()

# 判断源文件夹存在吗？
english_path = os.path.join(working_directory, 'localization', source_language)
if False == os.path.isdir(english_path):
    print('directory not exists')
    exit()

# 如果简中文件夹已经存在，跳过转换
# simp_chinese_path = os.path.join(working_directory, 'localization', 'simp_chinese')
# if True == os.path.isdir(simp_chinese_path):
#     print('directory already exists')
#     exit()
# else:
#     os.mkdir(simp_chinese_path)

progress_file_content = []
# generate a progress file to record the progress of the translation
if os.path.isfile(os.path.join(working_directory, 'translate_progress.txt')):
    with open(os.path.join(working_directory, 'translate_progress.txt'), 'r', encoding='utf-8') as progress_file:
        progress_file_content = progress_file.readlines()

# 开始转换文件
# iterate through all files in the folder and sub folders

files = get_all_files(english_path)
for file in files:
    # load the save progress, skip the file that has been translated
    for line in progress_file_content:
        if file == line.strip('\n'):
            continue

    convert_file(os.path.dirname(file), os.path.basename(file))
    # save translate progress to a file
    with open(os.path.join(working_directory, 'translate_progress.txt'), 'a', encoding='utf-8') as progress_file:
        progress_file.write(file + '\n')
