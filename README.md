# neurons.c
Collection of C codes to run different types of neural nets in plain C.

![alt text](image.webp "Fast Neurons in C")


# Introduction
This repository will contain many repos; I am not fluent enough in git to do the merging of forks from other repos into this. I am just looking for a way to improve the ecosystem and organize my local code changes.

# Cloned repos
- llama2.c: https://github.com/karpathy/llama2.c
- llama3.c: https://github.com/jameswdelancey/llama3.c

# Models
- llama2: ✔️
- llama3: ✔️
- llama3.1: ❌
- llama3.2: ✔️
- tinyllama: ✔️
- AMD-LLaMA: ❌
- Mistral 7B: ❌

# Motivation
A similar motivation of what brought projects like llm.c and llama2.c by Andrej Karpathy. I find the llama.cpp and ggml repos a bit too complex; they implement a whole stack from scratch to be used for many types of models and extend the functionalities.

This repo is looking for a way of having new implementations written in plain C to run inference.

The main objective is inference.

Each type of model should have its own separate folder. The main reason im moving forward with this is because my cloned repos are getting a lot of updates. I also see that, as an example, llama2.c repo is 1 year old without getting many updates, and having plenty of pull requests and issues. I also dont know if this will get anywhere, i'll use it at least to organize my local changes.

# Motivation 2
I am tired of filling my hard disk with pytorch bloat :(
