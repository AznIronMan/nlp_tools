import logging
logging.getLogger().setLevel(logging.CRITICAL)

import sys
from transformers import pipeline

logging.getLogger().setLevel(logging.CRITICAL)

def get_highest_emotion_score(output):
    # Use the 'max' function with a key function that returns the 'score' of each dictionary
    highest_emotion = max(output[0], key=lambda emotion: emotion['score'])
    return highest_emotion['label']

def get_emotion(text):
    classifier = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    emotion = get_highest_emotion_score(classifier(text))
    return emotion

if __name__ == '__main__':
    text = sys.argv[1]
    emotion = get_emotion(text)
    print(emotion)