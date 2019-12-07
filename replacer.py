import re

def replacesub(txt):
    
    nglist = [
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

    repdict = {
        "ﬁ": "fi",
        "ﬂ": "fl",
        "ﬀ": "ff",
        "ﬅ": "ft",
        "ﬆ": "st",
        "ﬃ": "ffi"
    }

    for k,v in repdict.items():
        txt = re.sub(k,v,txt)

    txt = re.sub("|".join(nglist),'',txt)
    txt = re.sub("[^a-zA-Z’., ]+", ' ', txt)
    txt = re.sub(" {2,}",' ',txt)
    return txt

if __name__ == "__main__":
    pass

