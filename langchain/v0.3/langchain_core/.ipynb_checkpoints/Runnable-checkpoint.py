from langchain_core.runnables import RunnableLambda

chain = RunnableLambda(lambda x: x*2)

chain.invoke()