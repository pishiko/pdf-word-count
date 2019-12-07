# 手順メモ

## pdf to text
- qpdfで編集制限解除
    ```
    qpdf-9.1.0\bin\qpdf.exe --decrypt eiken\2019-1-1ji-1kyu.pdf out.pdf
    ```

- pdfminer付属スクリプトのpdf2txt.pyでテキスト化
    ```
    python pdf2txt.py -o out.txt in.pdf
    ```

- 2012年の1~3kyuのscriptでないデータはOCRで処理

    数が少ないのでGoogleDriveにアップロード→GoogleドキュメントでOCR→textファイルでDL

## text to csv
- textからごみを取る

    この辺を除去，置換
    ```python
    [
        "https?:\/\/[\w/:%#\$&\?\(\)~\.=\+\-]+",    #URL
        "cid",                                      #decode error
        "Grade [0-9]",
        "Start from the next page.",
        "copyright",
        "ID",
        "[^a-zA-Z’.,][a-zA-Z][^a-zA-Z’.,]",         #1文字だけ
        "No.",
        "Listening Test",
        "Part [0-9]"
    ]

    {
        "ﬁ": "fi",
        "ﬂ": "fl",
        "ﬀ": "ff",
        "ﬅ": "ft",
        "ﬆ": "st",
        "ﬃ": "ffi"
    }
    ```

- spacyで解析

    英語用自然言語処理ライブラリ
    
    [https://spacy.io/](https://spacy.io/)

- pandasとかで処理して出力

## おわり

# 環境

- qpdf-9.1.0

```
>conda list

attrs                     19.3.0                     py_0    conda-forge
ca-certificates           2019.11.27                    0
catalogue                 0.0.8                      py_0    conda-forge
certifi                   2019.11.28               py37_0
cffi                      1.13.2           py37hb32ad35_0    conda-forge
chardet                   3.0.4                 py37_1003    conda-forge
cryptography              2.8              py37hb32ad35_1    conda-forge
cymem                     2.0.3            py37h6538335_0    conda-forge
cython-blis               0.4.1            py37hfa6e2cd_0    conda-forge
en-core-web-sm            2.2.5                    pypi_0    pypi
idna                      2.8                   py37_1000    conda-forge
importlib_metadata        1.2.0                    py37_0    conda-forge
intel-openmp              2019.4                      245
jsonschema                3.2.0                    py37_0    conda-forge
libblas                   3.8.0                    14_mkl    conda-forge
libcblas                  3.8.0                    14_mkl    conda-forge
liblapack                 3.8.0                    14_mkl    conda-forge
mkl                       2019.4                      245
more-itertools            8.0.1                      py_0    conda-forge
murmurhash                1.0.0            py37h6538335_0    conda-forge
numpy                     1.17.3           py37hc71023c_0    conda-forge
openssl                   1.1.1d               he774522_3
pandas                    0.25.3           py37ha925a31_0
pdfminer                  20191125                 pypi_0    pypi
pip                       19.3.1                   py37_0    conda-forge
plac                      0.9.6                      py_1    conda-forge
preshed                   3.0.2            py37h6538335_1    conda-forge
pycparser                 2.19                     py37_1    conda-forge
pycryptodome              3.9.4                    pypi_0    pypi
pyopenssl                 19.1.0                   py37_0    conda-forge
pyrsistent                0.15.6           py37hfa6e2cd_0    conda-forge
pysocks                   1.7.1                    py37_0    conda-forge
python                    3.7.3                h510b542_1    conda-forge
python-dateutil           2.8.1                      py_0
pytz                      2019.3                     py_0
requests                  2.22.0                   py37_1    conda-forge
setuptools                42.0.2                   py37_0    conda-forge
six                       1.13.0                   py37_0    conda-forge
spacy                     2.2.3            py37he980bc4_0    conda-forge
sqlite                    3.30.1               hfa6e2cd_0    conda-forge
srsly                     0.2.0            py37h6538335_0    conda-forge
thinc                     7.3.0            py37he980bc4_0    conda-forge
tqdm                      4.40.0                     py_0    conda-forge
urllib3                   1.25.7                   py37_0    conda-forge
vc                        14.1                 h0510ff6_4
vs2015_runtime            14.16.27012          hf0eaf9b_0
wasabi                    0.4.0                      py_0    conda-forge
wheel                     0.33.6                   py37_0    conda-forge
win_inet_pton             1.1.0                    py37_0    conda-forge
wincertstore              0.2                   py37_1003    conda-forge
zipp                      0.6.0                      py_0    conda-forge
```