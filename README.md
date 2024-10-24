# Project-4-Vietnamese-chatbot-using-LLM-RAG
LangChain, HuggingFace, Streamlit

In this project, I will create a locally running chatbot on a personal computer with a web interface using Streamlit. The chatbot will utilize a large language model and RAG technique, providing answers based on your PDF file (it could also be a Docs file, website, etc.).
* In this project i used:*
- Vietnamese LLM : https://huggingface.co/uonlp/Vistral-7B-Chat-gguf/blob/main/ggml-vistral-7B-chat-q5_0.gguf
- Vietnamese Embedding model: https://huggingface.co/dangvantuan/vietnamese-embedding

## Retrieval Augmented Generation (RAG)
- RAG uses a **retrieval model** to fetch relevant information from a database. This information is then combined with a **large language model (LLM)** to generate a response. This enables the model to answer questions or generate content based on up-to-date information, rather than relying solely on pre-trained data
### Retrieval Model
![image](https://github.com/user-attachments/assets/f48b4026-fdb1-4902-a23c-670c1c3e2ac0)
### RAG model
![image](https://github.com/user-attachments/assets/129a6169-3fc3-4df7-a6d5-72655785bce7)

**Limitations:**
1. Since it uses the Ctransformer library (model running on CPU), the performance is not high. You can use Transformer + Pytorch to run the model on GPU.
2.Chat memory has not been designed to improve accuracy in responses.
3. The evaluation setup for comparing performance has not been implemented.

