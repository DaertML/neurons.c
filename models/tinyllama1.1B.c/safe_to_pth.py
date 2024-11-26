from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

print('loading model...')

model_id = "/Users/pc/Desktop/llama2.c/tinyllama/llama2.c/micro-mistral"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="cpu",
)

print('saving model...')

# Save only the state dictionary
torch.save(model.state_dict(), "/Users/pc/Desktop/llama2.c/tinyllama/llama2.c/micro-mistral/consolidated.tiny.pth")
