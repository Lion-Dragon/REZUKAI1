from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Happy Women's Day!</title>
        <style>
            body { text-align: center; font-family: Arial, sans-serif; background-color: #ffe6f2; }
            h1 { color: #d63384; margin-top: 50px; }
            p { font-size: 18px; color: #555; }
            .flower { font-size: 50px; }
        </style>
    </head>
    <body>
        <h1>🌸 Chúc Mừng Ngày Quốc Tế Phụ Nữ 8/3! 🌸</h1>
        <p>Chúc bạn một ngày thật vui vẻ, hạnh phúc và tràn đầy yêu thương! 💖</p>
        <p class="flower">💐💐💐</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
