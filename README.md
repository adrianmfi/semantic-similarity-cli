# cli-semantic-similarity

## Summary:
cli-semantic-similarity is a command-line tool leveraging NLP models to compute semantic similarity directly from your terminal. All computations are done locally.

## How It Works
On first use, the tool automatically downloads and installs the Instructor embedding model. This model is then used to compute the semantic similarity of text inputs.

## Installation
Install cli-semantic-similarity using pip:
```bash
pip install semantic-similarity
```

## Usage
Compare the similarity of input text to a given phrase:

```bash
semsim "Lorem ipsum"
```

Find the most similar commits to a specified sentence:
```bash
git log --oneline -n 100 | semsim "refactor rest controllers" | sort -n -r | head
```

Filter commits based on a minimum similarity score (e.g., 0.6):
```bash
git log --oneline -n 100 | semsim "refactor rest controllers" | awk '$1 >= 0.6'
```

## License

MIT
