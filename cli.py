import sys
from InstructorEmbedding import INSTRUCTOR
import numpy as np
import argparse


def embed_query(instructor_model, text: str):
    instruction = "Represent the search term for retrieval of input from stdin"
    embeddings = instructor_model.encode([[instruction, text]])
    return embeddings[0]


def embed_stdin(instructor_model, text: str):
    instruction = "Represent input text for retrieval of input from stdin"
    embeddings = instructor_model.encode([[instruction, text]])
    return embeddings[0]


def main():
    try:
        parser = argparse.ArgumentParser(
            prog='semsim',
            description='Returns a similarity score for each line in the input, based on the similarity to a given string using an embedding model')

        parser.add_argument('query',
                            help="The string to compare with")
        parser.add_argument(
            '-m', '--model',
            choices=['hkunlp/instructor-xl', "hkunlp/instructor-large"],
            default='hkunlp/instructor-xl',
            help="Model to use")

        args = parser.parse_args()

        instructor_model = INSTRUCTOR(args.model)

        query_embedding = embed_query(instructor_model, args.query)

        if sys.stdin.isatty():
            print("Input: ")
        for line in sys.stdin:
            stdin_embedding = embed_stdin(instructor_model, line)
            similarity = np.dot(stdin_embedding, query_embedding)

            print(str(similarity) + "\t"+line.strip())
            if sys.stdin.isatty():
                print("Input: ")
    except KeyboardInterrupt:
        sys.exit(0)
