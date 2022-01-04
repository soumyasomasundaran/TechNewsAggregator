import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

def create_doc(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    return doc

def filter_keywords(doc):
    keywords = []
    stopwords = list(STOP_WORDS)
    pos_tag = ['PROPN','AD','NOUN','VERB']
    
    for token in doc:
        if(token.text) in (stopwords, punctuation):
            continue
        if token.pos_ in pos_tag:
            keywords.append(token.text)
    return keywords        

def find_frequent_words(keywords):
    frequent_words = Counter(keywords)
    return frequent_words

def normalize_frequent_words(frequent_words,keywords):
    max_frequency = Counter(keywords).most_common(1)[0][1]
    for word in frequent_words.keys():
        frequent_words[word]=frequent_words[word]/max_frequency
    return frequent_words.most_common(5)

def weighing_sentences(frequent_words,doc):
    sent_strength= {}
    for sent in doc.sents:
        for word in sent:
            if word.text in frequent_words.keys():
                if sent in sent_strength.keys():
                    sent_strength[sent] += frequent_words[word.text]
                else:
                    sent_strength[sent] = frequent_words[word.text]
    return sent_strength


def token_to_string(summary_list):
    return".".join(str(i) for i in summary_list)


def summarize(content):
    doc = create_doc(content)
    keywords = filter_keywords(doc)
    frequent_words = find_frequent_words(keywords)
    frequent_words_normalized = normalize_frequent_words(frequent_words,keywords)
    weighed_sentences = weighing_sentences(dict(frequent_words_normalized),doc)
    summary_list = nlargest(3,weighed_sentences,key = weighed_sentences.get)
    summary  = token_to_string(summary_list)
    return  summary
       


    
def extract_entities(text):
    entity_list = []
    doc = create_doc(text)
    # creating a list of organization and people tokens
    organization_list = Counter(token.text for token in doc.ents if token.label_ == 'ORG')
    people_list = Counter(token.text for token in doc.ents if token.label_ == 'PERSON')
    entity_dictionary = {'People': people_list,'Organization':organization_list}
    for key,value in entity_dictionary.items():
        entity_list.extend([(key,)+tuple_value for tuple_value in value.most_common()])
    return entity_list