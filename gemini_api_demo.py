"""
LangChain + Google Gemini API デモ
APIキーを使用したシンプルな実装
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
import os

def main():
    print("=== LangChain + Gemini API デモ ===\n")
    
    # 環境変数からAPIキーを取得
    # export GOOGLE_API_KEY="your-api-key" を実行するか、
    # 直接設定してください
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("⚠️  GOOGLE_API_KEYが設定されていません")
        print("\n以下のコマンドでAPIキーを設定してください:")
        print('export GOOGLE_API_KEY="your-api-key-here"')
        print("\nAPIキーは https://aistudio.google.com/app/apikey で取得できます")
        return
    
    # LangChainのChatGoogleGenerativeAIを初期化
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        google_api_key=api_key
    )
    
    # 会話の例
    messages = [
        SystemMessage(content="あなたは親切なAIアシスタントです。日本語で回答してください。"),
        HumanMessage(content="LangChainについて簡単に3文で説明してください。")
    ]
    
    print("質問: LangChainについて簡単に3文で説明してください。\n")
    print("回答:")
    
    try:
        # LLMを呼び出し
        response = llm.invoke(messages)
        print(response.content)
        
        print("\n" + "="*50)
        print("\n✅ デモ完了!")
        print("\n次は別の質問を試してみましょう:")
        
        # もう一つの例
        print("\n質問: Pythonの主な特徴を教えてください。\n")
        print("回答:")
        
        response2 = llm.invoke([
            SystemMessage(content="あなたは親切なAIアシスタントです。"),
            HumanMessage(content="Pythonの主な特徴を3つ教えてください。")
        ])
        print(response2.content)
        
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        print("\nAPIキーが正しいか確認してください")

if __name__ == "__main__":
    main()
