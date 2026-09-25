from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud CI/CD Project</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                text-align: center;
                padding-top: 100px;
            }

            .container {
                background: white;
                width: 600px;
                margin: auto;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            }

            h1 {
                color: #2563eb;
            }

            .status {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>Cloud-Based CI/CD Pipeline</h1>

            <h2>Automated Application Deployment</h2>

            <p class="status">
                ● Application is Running
            </p>

            <p>
                This application is deployed using
                Docker, GitHub Actions and AWS.
            </p>

            <p>
                Version: <strong>2.0</strong>
            </p>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)