# BERT 
- Discriminative model
    - meaning that it is used to classify or label text
- Works on Masked Language Modelling. 
    - Before feeding word sequences into BERT, 15% of the words in each sequence are replaced with a [MASK] token.
    - The model then attempts to predict the original value of the masked words, based on the context provided by the other, non-masked, words in the sequence
- A [CLS] token is inserted at the beginning of the first sentence and a [SEP] token is inserted at the end of each sentence.
- When training the BERT model, Masked LM and Next Sentence Prediction are trained together

- Usecases 
    - Classification tasks - Sentiment analysis. 
    - NER 
    - Answering questions  

# GPT 
- Generative model 
    - Generate new text based on patterns learned from data, rather than classifying existing data like a discriminative model would do. 
- Works on Casual Language modelling
