import asyncio
from aiohttp import web
import os

PORT = int(os.environ.get("PORT", 8000))

# =========================
# 🏠 HOMEPAGE
# =========================
HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>tgr-hash homepage</title>
    <link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            font-family: 'Pixelify Sans', sans-serif;
            background: #0f0f0f;
            color: white;
            text-align: center;
        }

        h1 {
            margin-top: 20vh;
            font-size: 120px;
        }

        .subtitle {
            font-size: 18px;
            margin-top: -20px;
            margin-bottom: 40px;
            color: #cccccc;
        }

        .buttons {
            margin-top: 40px;
        }

        .btn {
            display: inline-block;
            margin: 10px;
            padding: 15px 30px;
            border: 2px solid white;
            color: white;
            text-decoration: none;
            font-size: 24px;
        }

        .btn:hover {
            background: white;
            color: black;
        }
    </style>
</head>
<body>
    <h1>tgr-hash</h1>
    <h2 class="subtitle">This site is my homepage. It's only redirects to all of my other work.</h2>
    
    <div class="buttons">
        <a href="/games/games.html" class="btn">Games</a>
        <a href="https://chat-s0cb.onrender.com" target="_blank" class="btn">Chat</a>
        <a href="/documents/viewer.html" target="_blank" class="btn">Other Work</a>
    </div>
    <div class="buttons">
        <a href="/games/repos.html" class="btn">My Code</a>
        <a href="https://google.com" target="_blank" class="btn">Placeholder</a>
    </div>
</body>
</html>
"""

async def home(request):
    return web.Response(text=HOME_HTML, content_type="text/html")

# =========================
# 💬 CHAT REDIRECT
# =========================
async def chat_redirect(request):
    # OPTION 1: redirect to your existing deployed chat
    return web.HTTPFound("https://chat-s0cb.onrender.com")

    # OPTION 2 (better later):
    # return web.Response(text=CHAT_HTML, content_type="text/html")

# =========================
# 🚀 MAIN APP
# =========================
app = web.Application()

app.router.add_get("/", home)
app.router.add_get("/chat", chat_redirect)

# serve games folder
app.router.add_static('/games/', path='./static', name='games')
app.router.add_static('/documents/', path='./documents', name='documents')

web.run_app(app, port=PORT)
