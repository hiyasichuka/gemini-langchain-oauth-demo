"""
シンプルなLangChain + Geminiのデモ
OAuth認証なしで動作します
"""
from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage, SystemMessage

def main():
    # 環境変数からプロジェクトIDを取得
    # export GOOGLE_CLOUD_PROJECT="your-project-id" を実行してください
    
    print("=== LangChain + Gemini シンプルデモ ===\n")
    
    # LangChainのChatVertexAIを初期化
    # デフォルト認証（gcloud auth application-default login）を使用
    llm = ChatVertexAI(
        model_name="gemini-2.5-flash",
        temperature=0.7,
    )
    
    # 会話の例
    messages = [
        SystemMessage(content="あなたは親切なAIアシスタントです。"),
        HumanMessage(content="LangChainについて簡単に説明してください。")
    ]
    
    print("質問: LangChainについて簡単に説明してください。\n")
    print("回答:")
    
    # LLMを呼び出し
    response = llm.invoke(messages)
    print(response.content)
    
    print("\n" + "="*50)
    print("\nデモ完了!")

if __name__ == "__main__":
    main()
