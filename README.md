# Semantic-Textual-Similarity
Quantify the degree of similarity between two sentences

## Objective
The objective is to use a Natural Language Model that could quantify the similarity between two sentences and deploy the solution on cloud as an API endpoint.

## Methodology
The aim is to create a n-dimensional vector representations of sentence which could be quantified by a similarity metric such as cosine similarity to see how aligned these two sentences are with each other.

A pre-trained HuggingFace model **all-MiniLM-L6-V2** was used to create a 384 dimensional sentence embeddings and calculate the similarity score using cosine similarity. As the cosine similarity gives score between -1 and +1, scores less than 0 are equated to zero, whereas scores between 0 and 1 are kept as it is.

## Deployment Approach
The webapp was made using Flask and an endpoint is created and tested locally. The solution was deployed in Google Cloud Run and a request script is present to run inference.
