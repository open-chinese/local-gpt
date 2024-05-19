import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, StoppingCriteria, StoppingCriteriaList
from datetime import datetime
from loguru import logger


# load model
ModelPath = '/data/models/Qwen1.5-4B-Chat'
device = "cuda" if torch.cuda.is_available() else "cpu"
logger.info("device ", device)
model = AutoModelForCausalLM.from_pretrained(
    ModelPath,
    # torch_dtype="auto",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
logger.warning('Model loaded successfully')
model.eval()
tokenizer = AutoTokenizer.from_pretrained(ModelPath)


# add stopping patterns
class KeywordsStoppingCriteria(StoppingCriteria):
    def __init__(self, keywords_ids: list):
        self.keywords = keywords_ids

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        if input_ids[0][-1] in self.keywords:
            return True
        return False


# stop_words = ['}', ' }', '\n']
# stop_ids = [tokenizer.encode(w)[0] for w in stop_words]
# stop_criteria = KeywordsStoppingCriteria(stop_ids)


class GPTService:

    @staticmethod
    def generate_text(messages, max_tokens=100, stop_words=None):
        stopping_criteria = None
        if stop_words:
            stop_ids = [tokenizer.encode(w)[0] for w in stop_words]
            stop_criteria = KeywordsStoppingCriteria(stop_ids)
            stopping_criteria = StoppingCriteriaList([stop_criteria])

        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = tokenizer([text], return_tensors="pt").to(device)

        t1 = datetime.utcnow()
        generated_ids = model.generate(
            model_inputs.input_ids,
            max_new_tokens=max_tokens,
            stopping_criteria=stopping_criteria

        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        # response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        logger.warning(response)
        t2 = datetime.utcnow()
        duration = (t2 - t1).total_seconds()
        logger.info('inference duration {0}'.format(duration))
        return response


if __name__ == '__main__':
    pass
