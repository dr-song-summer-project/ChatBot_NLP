from _ast import While
from collections import defaultdict
import nltk
import pandas as pd
from soynlp.normalizer import *
import numpy as np
from openpyxl import Workbook
import openpyxl

MAXSIZE = 10
Bpoint = True
path_sample = 'src/sample_data_preprocessed_4100.xlsx'

wb = Workbook()
wb = openpyxl.load_workbook('src/sample_annotation.xlsx')
sheet1 = wb.active


def read_file(file_paths):  # ==파일 읽어오기
    df_ = pd.read_excel(file_paths)
    numpy = pd.DataFrame.to_numpy(df_)
    return df_, numpy


def classify(text_Q, text_A):
    correct = True
    print('질문 = '+text_Q)
    print('답변 = ' + text_A)
    while correct:
        ant_Q = input("질문 요약문을 입력하세요 : ")
        if ant_Q != '':
            correct = False
        else:
            correct = True

    correct = True
    while correct:
        ant_A = input("답변 요약문을 입력하세요 : ")
        if ant_A != '':
            correct = False
        else:
            correct = True

    if ant_Q == 'q' or ant_A == 'q':
        return False
    Query.append((text_Q, ant_Q))
    Answer.append((text_A, ant_A))
    # 엑셀 append
    sheet1.append([text_Q, ant_Q, text_A, ant_A])
    wb.save('src/sample_annotation.xlsx')
    return True

# =============================================================

text_df, text_df_np = read_file(path_sample)  # 학습할 데이터

# =============================================================

data = pd.DataFrame()
standard = pd.DataFrame()
data['querys'] = text_df['질문']
data['answers'] = text_df['답변']

data = data[data['querys'].notna()]
data = data[data['answers'].notna()]

# =============================================================
Qst = data['querys'].values.tolist()
Ans = data['answers'].values.tolist()
# =============================================================
Query = []
Answer = []
# =============================================================

#for i in range(0, len(data['querys']), 10):

f = open('src/마지막인덱스.txt', 'r')
idx = f.readline()
i = int(idx)
f.close()

while True:
    print(i,'번')
    Bpoint = classify(Qst[i], Ans[i])
    if Bpoint == False:
        break
    i = i + 1

wb.close()

f = open('src/마지막인덱스.txt', mode='wt', encoding='utf-8')
f.write(str(i))
f.close()
