from flask import Flask, request, jsonify
import re
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import chromadb
from werkzeug.exceptions import BadRequest, InternalServerError

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Initialize ChromaDB client
chroma_client = chromadb.HttpClient(host="chroma-server-hostname", port=chroma_server-port)

def process_text(text):
    # Tokenize text and remove punctuation
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens if word.isalpha()]
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

def train_word_embeddings(data):
    qa_pairs = re.split(r'\n\n+', data)
    qa_pairs = [qa.split('\n') for qa in qa_pairs if qa]
    sentences = [process_text(qa_pair[0][2:]) for qa_pair in qa_pairs]
    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)
    return model

@app.route('/process-data', methods=['POST'])
def process_data():
    try:
        data = request.json['data']
        word_embedding_model = train_word_embeddings(data)

        # Save word embeddings to ChromaDB
        for word, vector in zip(word_embedding_model.wv.index_to_key, word_embedding_model.wv.vectors):
            # Store word and vector in ChromaDB
            chroma_client.set_vector(collection_name="word_embeddings", key=word, vector=vector.tolist())

        return jsonify({'message': 'Data processed, embeddings trained, and stored in ChromaDB.'})

    except Exception as e:
        raise InternalServerError(f"An error occurred during data processing: {str(e)}")

@app.route('/get-embeddings', methods=['POST'])
def get_embeddings():
    try:
        prompt = request.json['prompt']
        prompt_tokens = process_text(prompt)

        # Retrieve embeddings for prompt tokens from ChromaDB
        embeddings = []
        for token in prompt_tokens:
            vector = chroma_client.get_vector(collection_name="word_embeddings", key=token)
            embeddings.append(vector)

        return jsonify({'prompt': prompt, 'embeddings': embeddings})

    except KeyError:
        raise BadRequest('Invalid request. Missing "prompt" in the request JSON.')

    except Exception as e:
        raise InternalServerError(f"An error occurred during embeddings retrieval: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
