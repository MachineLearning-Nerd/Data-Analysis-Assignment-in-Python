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

    # print(" Chnaged Replaceable Text")
    # print(changed_replaceable_text)
    print(len(changed_replaceable_text))

    # changed_replaceable_text = list(set(changed_replaceable_text))
    

    print(changed_replaceable_text)
    print(replaceable_text)

    count = 1
    reference_text = []
    for i, ival in enumerate(replaced_text):
        for val in replaceable_text:
            if val in ival:
                # print('%%'*50)
                # print('\n')
                # print(replaced_text[i])
                # print('\n')
                # print(val)
                temp_text = []
                for i_text, c_text in enumerate(changed_replaceable_text):
                    tt_val = val.replace('et al.', '').replace('e.g., ', '')
                    # print(c_text, val, tt_val, i)
                    # print(c_text in tt_val)
                    if c_text in val or c_text in tt_val:
                        temp_text.append(i_text+1)
                        # print(c_text)
                replaced_text[i] = replaced_text[i].replace(val, '{}'.format(temp_text))
                # print('\n')
                # print(replaced_text[i])

    # for i in range(len(replaced_text)):
    #     print(replaced_text[i])
    #     print(full_text[i])
    #     print('\n')

    reference = []
    reference_start = False
    for val in replaced_text:
        # print(val)
        if 'Reference' in val:
            reference_start = True
        if reference_start:
            reference.append(val)
    # print(reference)
    # print(reference_text)

    new_reference = []
    replace_characters = [')', '(', '.', 'eg',  'et', 'and', 'Pers']
    for val in reference_text:
        # val = '(Moore, 1996; Bushong, 2002)'
        print(val)
        n_val = val
        for ch in replace_characters:
            if ch in n_val:
                n_val = n_val.replace(ch, '')
        
        n_val = n_val.replace(',', ' ').replace(';', ' end_of ').split(' ')
        t_val = []
        for temp in n_val:
            # if len(temp) < 3 or temp.isdigit():
            if len(temp) < 3 :
                pass
            else:
                t_val.append(temp)
        print(t_val)

        
        # temp_ref = []
        # for i, ref in enumerate(reference):
        #     temp_flag = []
        #     for temp in t_val:
        #         if temp.lower() in ref.lower() and temp.isdigit() == False: 
        #             temp_flag.append('is_there')
        #         elif temp.lower() in ref.lower() and temp.isdigit(): 
        #             temp_flag.append('is_there')
        #             if 'not_there' not in temp_flag and len(temp_flag) != 0:
        #                 print(ref)
        #         else:
        #             temp_flag.append('not_there')
        #     if 'not_there' not in temp_flag and len(temp_flag) != 0:
        #         print(ref)
                    
        temp_ref = []
        for i, temp in enumerate(t_val):
            # print(i, temp)
            for ref in reference:
                if  temp =='end_of':
                    temp_ref = list(set(temp_ref))
                    # print(temp_ref)
                if temp.lower() in ref.lower() and temp.isdigit() == False : 
                    temp_ref.append(ref)
                    # print(temp_ref)
                    break
                elif temp.lower() in ref.lower() and temp.isdigit() : 
                    # print(i)
                    if t_val[i-1].lower() in ref.lower():
                        temp_ref = list(set(temp_ref))
                        # print(temp_ref)
                    # else:
                    #     temp_ref.remove(temp_ref[-1])
                        # print("****:::"*10, ref)
        print(temp_ref)
        # break





        

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
