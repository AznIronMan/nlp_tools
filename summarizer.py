import logging
import sys

from transformers import pipeline

logging.getLogger().setLevel(logging.CRITICAL)


def summarizer(text, max=None, min=None, threshold=32, curve=0.1):

    word_count = text.count(" ")

    print(word_count)

    if word_count < threshold:
        return text

    if max != None and type(max) == str:
        max_length = int(max)
    if min != None and type(min) == str:
        min_length = int(min)

    if max == None or max == 0 or type(max) != int:
        max_length = round(word_count - (word_count * curve))
    else:
        max_length = max

    if min == None or max == 0 or type(min) != int:
        min_length = round(word_count * curve)
    else:
        min_length = min

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    summary = summarizer(text, max_length=max_length,
                         min_length=min_length, do_sample=False)

    return summary[0]['summary_text']


if __name__ == '__main__':
    import sys
    text = sys.argv[1]
    max = sys.argv[2] if len(sys.argv) > 2 else None
    min = sys.argv[3] if len(sys.argv) > 3 else None
    threshold = int(sys.argv[4]) if len(sys.argv) > 4 else 32
    curve = float(sys.argv[5]) if len(sys.argv) > 5 else 0.1
    summary = summarizer(text, max, min, threshold, curve)
    print(summary)
