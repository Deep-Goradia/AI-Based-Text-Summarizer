import re
import heapq
import nltk

# Download necessary resources (one-time)
nltk.download('punkt')
nltk.download('stopwords')

class Summarizer:
    def __init__(self):
        self.stopwords = set(nltk.corpus.stopwords.words('english'))

    def summarize(self, text, num_sentences=3):
        # Split into sentences
        sentences = nltk.sent_tokenize(text)

        # Tokenize words
        words = re.findall(r'\w+', text.lower())

        # Frequency of words (ignoring stopwords)
        freq = {}
        for word in words:
            if word not in self.stopwords:
                freq[word] = freq.get(word, 0) + 1

        # Score sentences
        sentence_scores = {}
        for sent in sentences:
            for word in nltk.word_tokenize(sent.lower()):
                if word in freq:
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + freq[word]

        # Pick top N sentences
        summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

        return summary_sentences
