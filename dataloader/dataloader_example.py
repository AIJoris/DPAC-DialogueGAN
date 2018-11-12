from dp_corpus import DPCorpus
from dp_data_loader import DPDataLoader

corpus = DPCorpus(vocabulary_limit=5000)
train_dataset = corpus.get_train_dataset()
train_data_loader = DPDataLoader(train_dataset)

for (batch, (context, reply)) in enumerate(train_data_loader):
    print(context)
    print(reply)

    print(' '.join(corpus.ids_to_tokens(context[0]))) # Padding tokens are ignored
    print(' '.join(corpus.ids_to_tokens(reply[0]))) # Padding tokens are ignored
    break