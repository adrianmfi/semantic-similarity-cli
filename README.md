# semantic-similarity-cli

## Summary:
semantic-similarity-cli is a command-line tool leveraging NLP models to compute semantic similarity directly from your terminal. All computations are done locally.

## How It Works
On first use, the tool downloads the Instructor embedding model. Similarity between a target string is then computed by embedding the target and input into vectors, and taking the cosine distance between them.

## Installation
Install using pip:
```bash
pip install semantic-similarity-cli
```

## Usage
Compare the similarity of input text to a given phrase:

```bash
semsim "Text to calculate similarity to"
```

Find the commits with message most similar to "refactor user or auth service"
```bash
git log --oneline -n 100 | semsim "refactor user or auth service" | sort -n -r | head
```

Filter commits based on a minimum similarity score (e.g., 0.6):
```bash
git log --oneline -n 100 | semsim "refactor user or auth service" | awk '$1 >= 0.6'
```

## License

MIT
