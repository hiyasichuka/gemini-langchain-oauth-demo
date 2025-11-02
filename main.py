from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from langchain_google_vertexai import VertexAI

app = FastAPI()

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
REDIRECT_URI = "http://localhost:8000/oauth2callback"

user_sessions = {}

@app.get("/")
def index():
    return {"message": "LangChain + Gemini OAuth example. Visit /login"}

@app.get("/login")
def login():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
    )
    auth_url, state = flow.authorization_url(prompt="consent", include_granted_scopes="true")
    user_sessions["state"] = state
    return RedirectResponse(auth_url)

@app.get("/oauth2callback")
def oauth2callback(request: Request):
    state = user_sessions.get("state")
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
        state=state,
    )
    flow.fetch_token(authorization_response=str(request.url))
    credentials = flow.credentials
    user_sessions["credentials"] = credentials
    return RedirectResponse("/chat")

@app.get("/chat")
def chat():
    creds = user_sessions.get("credentials")
    if not creds:
        return {"error": "Not authenticated"}

    llm = VertexAI(model_name="gemini-1.5-pro", credentials=creds)
    response = llm.invoke("こんにちは、あなたは誰ですか？")
    return {"response": response}
