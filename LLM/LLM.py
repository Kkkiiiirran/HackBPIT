from langchain import PromptTemplate, LLMChain
import chainlit as cl
from langchain import HuggingFaceHub

repo_id = "tiiuae/falcon-7b-instruct"
# Create the HuggingFaceHub object
llm = HuggingFaceHub(
huggingfacehub_api_token='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',
repo_id=repo_id,
model_kwargs={"temperature":0.3, "max_new_tokens":1024}
)

template = """ Task: write a specific answer to question related to exercise,workout, health and fitness only, giving reference to exercises.
Topic: Health, fitness, exercise and workout
Style: Academic
Tone: Normal
Audience: 18-25 year olds
Length: 1 paragraph
Format: Text
Here's the question. {question}
"""

@cl.on_chat_start
def main():
    # Instantiate the chain for that user session
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    # Store the chain in the user session
    cl.user_session.set("llm_chain", llm_chain)

@cl.on_message
async def main(message: cl.Message):
    # Retrieve the chain from the user session
    llm_chain = cl.user_session.get("llm_chain")  # type: LLMChain

    # Call the chain asynchronously
    res = await llm_chain.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])

    await cl.Message(content=res['text']).send()
