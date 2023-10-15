# translation-from-english-to-dutch

The project is code to solve a sequence-to-sequence problem of translation. Specifically, the translating the sentences from English to Dutch. 

The Github repository contains two Jupyter Notebook scripts, which were used to solve the translation problem. The name and a short summary of the Jupyter Notebook can be seen below:
- **‘English-to-Dutch.ipy’**: to solve the problem to code employs two approaches that have been implemented using the … library. The two approaches which are used are: Graphical Recurrent Unit (Recurrent Neural Network) and transformer Architecture. The theory and methodology of these two methods will be discussed below.

# english-to-dutch.ipynb

Methods
- **Sentence Vectorisation**: representation of the entire sentence is or phrase in the entire sentence or phrase a vector in a continuous vector space. The goal of the stage is the represent the sentence/ phrase in a continuous vector space. Sentences with similar meanings will be closer together in the vector space than sentences with a completely different meaning. Sentence vectorisation represents the sentence and represents it numerically. 
- **Gated Recurrent Unit** (GRU):  is type of Recurrent Neural Network (RNN) architecture. A RNN has a folded layer which allows the network to consider previous information. A RNN architecture is effective for sequential problems and varying inputs. A GRU improves upon the traditional RNN architecture by ‘solving’ the vanishing gradient problem. The GRU solves the vanishing gradient problem through the gating mechanism. The GRU introduces two new gates: the update gate and reset gate. The update gate which decides how much of the previous hidden state is retained versus how much of the new candidate state is considered making it more effective in capturing long-term dependencies in sequence. The reset gate decides the extent to which the previous hidden state is used to compute the new candidate state. The diagram below shows roughly how the GRU works in terms of that there are multiple endoer and decords working to sequentially operate to generate a translation.

<h5 align="center"><ins>Source: Sequence-to-Sequence Translation Using Attention</ins> </h5>

![image](https://github.com/10Dennisw/translation-from-english-to-dutch/assets/119337144/e9f3e46f-7aca-4f3d-9bf8-f68b02950896)

- **Transformer**: is an architecture used for many natural language processing tasks. The transformer architecture contains an encoder, decoding and positional encoder to ensure that the unique position is taken into account. Below I have outlined the numerous key features of the Transformer architecture:
  - **Attention Mechanism**: the core idea behind the transformer is the self-attention mechanism, which allows the transformer network to account for the importance of the different words relative to the given word.
  - **Architecture**: 
    - Encoder**: Encodes the input sequence  multi-head self-attention mechanism and position-wise-forward network
    - **Decoder**: Generates the output centre  multi-head attention layer
  - **Multi-Head Attention**: by using multiple sets the network can focus on different parts of the input tasks or reasons.
  - **Positional Encoding**: which will consider the position of the word in the sequence.
  - **Feed-forward Networks**: after the attention mechanisms in both the encoder and decoder, the Transformer has feed-forward neural network that operate independently on each position.
  - **Normalization and Residual Connections**: Each sub-layer in the encoder and decoder contains a residual connection followed by layer normalisation. This trains deeper networks and reduces model complexity.

<h5 align="center"><ins>Source: Attention Is All You Need (Vaswani et al. , 2017) </ins> </h5>

<p align="center">
  <img src="https://github.com/10Dennisw/translation-from-english-to-dutch/assets/119337144/366e7db8-3bf4-4dc7-b03e-3c950dc7695f" alt="Image">
</p>
  
## Sources
- Attention Is All You Need (Vaswani et al. , 2017)
- Deep Learning with Python, Second Edition (François Chollet, 2021)
- Sequence-to-Sequence Translation Using Attention
  - https://www.mathworks.com/help/deeplearning/ug/sequence-to-sequence-translation-using-attention.html 
