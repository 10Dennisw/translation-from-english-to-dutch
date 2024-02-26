from google.cloud import storage
import torch 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_loaded= False

BUCKET_NAME = 'translator_model'

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

def translate(text, model, tokenizer):
  '''
  inputs: text: source texts
  model: the fine-tuned model
  tokenizer: the tokenizer used to tokenize the source texts, corresponding to the model
  output: the decoded translated text
  '''
  inputs = tokenizer(text, return_tensors="pt", max_length=30, truncation=True) # tokenizing the input sentence

  # Setting the model in evaluation mode
  model.eval()
  # Generating translation in the form of tokens using fine-tuned model
  outputs = model.generate(inputs['input_ids'], max_length=30, num_beams=4, early_stopping=True)
  # Decoding the outputs to generate a sentence
  translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
  return translated_text # Returning the decoded translation

def generating_translate_sent(request):
    global model_loaded
    
    # will load the model if not already loaded
    if model_loaded is False:
        model_name = "Helsinki-NLP/opus-mt-en-nl"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

        download_blob(
            BUCKET_NAME,
            "models/translator_model.pth",
            "/tmp/translator_model.pth", # where to download the model
        )

        state_dict = torch.load('/tmp/translator_model.pth', map_location=torch.device('cpu'))
        model.load_state_dict(state_dict)
        model_loaded = True

    translated_sent=translate(request, model, tokenizer)

    print(request)
    print(f"-->{translated_sent}")