import logging
import sys

from transformers import T5Tokenizer, T5ForConditionalGeneration

logging.getLogger().setLevel(logging.CRITICAL)


def get_keywords(inputs, beams=3, tokens=4096):

    if isinstance(inputs, str):
        inputs = [inputs]

    model = T5ForConditionalGeneration.from_pretrained(
        "Voicelab/vlt5-base-keywords")
    tokenizer = T5Tokenizer.from_pretrained("Voicelab/vlt5-base-keywords")
    task_prefix = "Keywords: "

    for sample in inputs:
        input_sequences = [task_prefix + sample]
        input_ids = tokenizer(
            input_sequences, return_tensors="pt", truncation=True, padding="max_length", max_length=512
        ).input_ids
        output = model.generate(input_ids, max_new_tokens=tokens,
                                no_repeat_ngram_size=1, num_beams=beams)
        predicted = tokenizer.decode(output[0], skip_special_tokens=True)
        return predicted


if __name__ == '__main__':
    text = sys.argv[1]
    beams = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    tokens = int(sys.argv[3]) if len(sys.argv) > 3 else 4096
    keywords = get_keywords(text, beams, tokens)
    print(keywords)
