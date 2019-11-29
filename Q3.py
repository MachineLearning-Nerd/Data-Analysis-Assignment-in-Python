# CMT114 Coursework
# student number:

import docx
import os, sys
import time

def contain_numbers(text):
    list_text = text[1:-1].split(' ')
    if len(list_text) == 1:
        return False
    for val in list_text:
        if val.isdigit() and len(val)==4:
            return True
    return False


def change_style(filepath, style='IEEE'):
    f = open(filepath, 'rb')
    document = docx.Document(f)
    f.close()
    full_text = []
    for p in document.paragraphs:
        full_text.append(p.text)
    # print(full_text)
    replaced_text = []
    replaced_text = list(full_text)
    # print(replaced_text)

    replaceable_text = []
    for i, text in enumerate(full_text):
        if '(' in text and ')' in text:
            curl_index_open = 0
            curl_index_close = 0 
            while(1):
                curl_index_open = text.find('(', curl_index_close, -1)
                curl_index_close = text.find(')', curl_index_open, -1)
                if curl_index_close == -1 or curl_index_open == -1:
                    break
                else:
                    temp_text = text[curl_index_open:curl_index_close+1]
                    if contain_numbers(temp_text):
                        replaceable_text.append(temp_text)

    changed_replaceable_text = []
    for new_r_val in replaceable_text:
        new_r_val = new_r_val.replace('et al.', '').replace('e.g., ', '').replace('(', '').replace(')', '')
        new_r_val = new_r_val.split('; ')
        for string_val in new_r_val:
            if string_val not in changed_replaceable_text:
                changed_replaceable_text.append(string_val)

    # print(len(changed_replaceable_text))
    # print(changed_replaceable_text)
    # print(replaceable_text)

    for i, ival in enumerate(replaced_text):
        for val in replaceable_text:
            if val in ival:
                temp_text = []
                for i_text, c_text in enumerate(changed_replaceable_text):
                    tt_val = val.replace('et al.', '').replace('e.g., ', '')
                    if c_text in val or c_text in tt_val:
                        temp_text.append(i_text+1)
                replaced_text[i] = replaced_text[i].replace(val, '{}'.format(temp_text))

    # for i in range(len(replaced_text)):
    #     print(replaced_text[i])
    #     print(full_text[i])
    #     print('\n')
    # return

    reference = []
    reference_start = False
    for val in replaced_text:
        # print(val)
        if 'Reference' in val:
            reference_start = True
        if reference_start:
            reference.append(val)

    new_reference = []
    for val in changed_replaceable_text:
        v_split = val.replace('and','').replace(',', '').split()
        for rf in reference:
            if v_split[0].lower() in rf.lower() and v_split[1].lower() in rf.lower():
                new_reference.append(rf)







        

    # remove this when you add your code
    # YOUR CODE HERE
    # YOUR CODE HERE
    # YOUR CODE HERE

# ---- DO NOT CHANGE THE CODE BELOW ----
if __name__ == "__main__":
    if len(sys.argv)<3: raise ValueError('Provide filename and style as input arguments')
    filepath, style = sys.argv[1], sys.argv[2]
    print('filepath is "{}"'.format(filepath))
    print('target style is "{}"'.format(style))
    change_style(filepath, style)
