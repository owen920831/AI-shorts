import ollama

# 設定 Gemma 模型
gemma = ollama.Client("gemma:7b")

# 輸入問題
question = input("請輸入您的問題：")

# 使用 Gemma 回答問題
response = gemma.predict(question)

# 輸出回答
print(response["answer"])
