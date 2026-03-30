def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    dict={}
    for sentence in sentences :
        for word in sentence:
            try :
                dict[word]+=1
            except KeyError:
                dict[word]=1
    return dict