# nlp-spam-detector

Spam Detector 

Takeways:

1) A lot of NLP is just pre-processing data for use in existing Machine Learning algorithms. What's involved is how do we take a bunch of documents, feed them into ML algorithms input is a vector of numbers.
2) We can use any existing ML classifiers as long as you can make the text processing with the subtlety of language. 

Sci-kit learn 

Pre-processing:
https://archive.ics.uci.edu/ml/datasets/Spambase

Columns 1..48 (input)
- word-frequency measure - number of times word appears divided by number of words in document x 100

Last column is a label
- 1 = spam, 0 = not spam

One example of a "term-document matrix" - terms go along columns, documents (emails) go along rows

