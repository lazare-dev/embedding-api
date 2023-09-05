# Word Embedding App with ChromaDB

This application processes text data, trains word embeddings, and stores them in ChromaDB. It also provides an API to retrieve embeddings for given prompts.

## Getting Started

To run this application locally, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/embedding-app.git
   ```

2. Change your current directory to the project directory:

   ```bash
   cd embedding-app
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask application:

   ```bash
   python app.py
   ```

5. The app will be accessible at `http://localhost:5000`.

## Usage

### Processing Data and Training Embeddings

- Send a POST request to `/process-data` with a JSON body containing the data you want to process:

  ```json
  {
    "data": "q:\na:\nq:\na:\n..."
  }
  ```

  This will process the data and train word embeddings, storing them in ChromaDB.

### Retrieving Embeddings

- Send a POST request to `/get-embeddings` with a JSON body containing a prompt:

  ```json
  {
    "prompt": "your prompt here"
  }
  ```

  This will retrieve embeddings for the tokens in the prompt from ChromaDB.

## Technologies Used

- Python
- Flask (Python web framework)
- Gensim (Word2Vec)
- NLTK (Natural Language Toolkit)
- ChromaDB (Document Database)

## Docker Support

You can also run this app in a Docker container. Refer to the provided Dockerfile and docker-compose.yml for containerization.

## Contributing

If you'd like to contribute to this project, please fork the repository, create a new branch for your feature, make your changes, and create a pull request for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the ChromaDB team for providing the database and support.

```
