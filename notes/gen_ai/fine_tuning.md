# BERT 
- Bert Tokenizer
    1. Converts Raw text into format which Bert can understand. 
    2. Uses the WordPiece algorithm to break text into smaller subword units.
        1. "playing" → ["play", "##ing"]
        2. "unknownword" → ["unk", "##nown", "##word"] - Tokens with ## represent subwords (continuations of the word). 

    3.  [CLS] classification token added at start. [SEP] added at the end or between multiple sentences.
    4. [PAD] tokens  added after sequences are truncated. 

    5. Attention mask is used to indicate which tokens are real and which are padding.


# Fine Tuning Bert Model. 
- for param in model.bert.parameters():
    param.requires_grad = False

    1. fine tuning happens in above, i.e Only the classification head (or other unfreezed layers) will be trained and  parameter values will not be updated during backpropagation.
    2. output of below code 
        for name, param in model.named_parameters():
        print(f"{name}: Trainable={param.requires_grad}")

    - bert.embeddings.word_embeddings.weight: Trainable=False
      bert.encoder.layer.0.attention.self.query.weight: Trainable=False
     
    classifier.weight: Trainable=True
    classifier.bias: Trainable=True
    3. 