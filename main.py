import glob
from subprocess import call
from replacer import replacesub
from pathlib import Path
import sys
import spacy
import pandas as pd
import re

#SPACE PUNCT PRON X

def counter(df,num=""):
    df['lemma'].value_counts().to_csv(num+"out.csv")
    

def main(num="1"):
    txts = " ".join(files2txts(num2files(num),num))
    df = textminer(txts,num)
    counter(df,num)

def textminer(text,num=""):
    nlp = spacy.load('en_core_web_sm')
    nlp.max_length = 2000000
    doc = nlp(text)

    lemma = []
    pos = []
    df = pd.DataFrame()

    for token in doc:
        lemma.append(token.lemma_)
        pos.append(token.pos_)

    df['lemma'] = lemma
    df['pos'] = pos
    df.to_csv(num+'tokens.csv',index=False)
    return df

def files2txts(files,num):
    l = files

    txts = []

    ls12 = glob.glob("2012txts\*-{}kyu*.pdf".format(num))
    for l12 in ls12:
        with open(l12,'r',errors="ignore",encoding='utf-8') as f:
            raw = f.read()
            txts.append(replacesub(raw))

    for fname in l:
        print("*START {}".format(fname))
        call(["qpdf-9.1.0\\bin\\qpdf.exe", "--decrypt", fname , "tmp.pdf"])
        call(["python","pdf2txt.py","-o","tmp.out","tmp.pdf"])
        with open("tmp.out", "r", errors="ignore", encoding='utf-8') as f:
            txts.append(replacesub(f.read()))
    return txts

def num2files(num:str):
    l = glob.glob("eiken\*-{}kyu*.pdf".format(num))
    #l = [f for f in l if not "2012" in f]   #remove 2012
    return l

def output():
    classs = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "p1",
        "p2"
    ]

    dfs = []

    for num in classs:
        df = pd.read_csv(num+"tokens.csv")
        df = df[df["pos"].apply(lambda x: not(x == "SPACE" or x == "PUNCT" or x == "PRON" or x == "X"))]
        df = df[df["lemma"].apply(lambda x: not(x == "-PRON-" or x== "’" or x=="s" or "." in x or x=="’s" or x=="www.eiken.or.jp" or x=="http"))]
        df['lemma'].value_counts().to_csv(num+"kyu-counts.csv")

        print(df)
        dfs.append(df)
    
    df_concat = pd.concat(dfs)
    df_concat['lemma'].value_counts().to_csv("all-counts.csv")

if __name__ == "__main__":

    # classs = [
    #     "1",
    #     "2",
    #     "3",
    #     "4",
    #     "5",
    #     "p1",
    #     "p2"
    # ]
    # for c in classs:
    #     main(c)
    output()
