import streamlit as st
from langchain_community.llms import CTransformers
from langchain.text_splitter import CharacterTextSplitter
import pdfplumber
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from html_chatbot import css, botHTCN_template, user_template


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        with pdfplumber.open(pdf) as pdf_reader:
            for page in pdf_reader.pages:
                text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=400,
        chunk_overlap=50,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name='dangvantuan/vietnamese-embedding')
    db = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return db

def get_conversation_chain(db):
    llm = CTransformers(model='models/ggml-vistral-7B-chat-q5_0.gguf', model_type="llama", max_new_tokens= 512, temperature=0 )
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever = db.as_retriever()
    )
    return conversation_chain

def handle_userinput(user_question):
    if st.session_state.conversation is not None:
        response = st.session_state.conversation.invoke({'question': user_question,'chat_history': [] })
        st.write(botHTCN_template.replace("{{MSG}}", response['answer']), unsafe_allow_html=True)


def main():
    st.set_page_config(page_title = "Chatbot cố vấn học tập HTCN", page_icon = ":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    # if "question_count" not in st.session_state:
    #     st.session_state.question_count = 0
    question_count = 0

    st.header("Chatbot cố vấn học tập HTCN :books:")
    user_question = st.text_input("Hãy hỏi các câu hỏi liên quan đến ngành Kỹ thuật Hệ thống Công nghiệp hoặc các quy định, chính sách của trường:")
    if user_question:
        question_count += 1
        if question_count > 1:
            st.session_state.conversation = None
        handle_userinput(user_question)

    #st.write(user_template.replace("{{MSG}}","Chào Long"), unsafe_allow_html=True)
    st.write(botHTCN_template.replace("{{MSG}}","Chào bạn"), unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Tài liệu của bạn")
        pdf_docs = st.file_uploader(
            "Tải các file PDF của bạn lên đây và nhấn 'Xử lý'", accept_multiple_files=True)
        if st.button("Xử lý"):
            with st.spinner("Đang xử lý"):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                db = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversation_chain(db)

if __name__ == '__main__':
    main()