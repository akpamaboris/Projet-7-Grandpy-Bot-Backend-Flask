from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from rake_nltk import Rake
rake_nltk_var = Rake(language="french")





def parser(str) :
    #je spécifie que les stopwords seront en Français
    stopWords = set(stopwords.words('french'))
    str1 = rake_nltk_var.extract_keywords_from_text(str)

    keyword_extracted = rake_nltk_var.get_ranked_phrases()
    str3 = finalResearch = ' '.join(keyword_extracted)

    words_you_remove = ["salut", "grandpy", "connais", "connait"]


    #je tokenize la phrase test, c'est à dire que je sépare une phrase, ou
    #un paragraphe dans des unités plus petites
    tokenizer = RegexpTokenizer(r'\w+')
    wordTokens = tokenizer.tokenize(str3)

    phrase_avec_filtre =[]
    for w in wordTokens:
        if w not in stopWords and w not in words_you_remove:
            phrase_avec_filtre.append(w)



    #ask what the user want
    searchRequest = phrase_avec_filtre

    #i change the list to a string
    finalResearch = ' '.join(searchRequest)

    return finalResearch
