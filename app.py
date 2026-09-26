import html
import os

from flask import Flask, jsonify, redirect, render_template_string, request, url_for

app = Flask(__name__)

# In-memory deployment data
deployments = [
    {
        "id": 1,
        "application": "Cloud CI/CD App",
        "environment": "Production",
        "version": "2.0",
        "status": "Deployed",
    }
]

# Git commit ID used by the application footer
COMMIT = os.getenv("GIT_SHA", os.getenv("GITHUB_SHA", "local"))[:7]


@app.route("/")
def home():
    return render_template_string(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Cloud Deployment Tracker</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: #f4f7fb;
                    margin: 0;
                    padding: 40px;
                }

                .container {
                    max-width: 1000px;
                    margin: auto;
                    background: white;
                    padding: 35px;
                    border-radius: 15px;
                    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
                }

                h1 {
                    color: #2563eb;
                    text-align: center;
                    margin-bottom: 10px;
                }

                .subtitle {
                    text-align: center;
                    color: #555;
                    margin-bottom: 30px;
                }

                form {
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    gap: 15px;
                    margin-bottom: 30px;
                }

                input,
                select,
                button {
                    padding: 12px;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    font-size: 14px;
                }

                button {
                    background: #2563eb;
                    color: white;
                    border: none;
                    cursor: pointer;
                    grid-column: span 2;
                }

                button:hover {
                    background: #1d4ed8;
                }

                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }

                th,
                td {
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: center;
                }

                th {
                    background: #2563eb;
                    color: white;
                }

                .status {
                    font-weight: bold;
                }

                .api-link {
                    margin-top: 25px;
                    text-align: center;
                }

                .api-link a {
                    color: #2563eb;
                    text-decoration: none;
                }

                footer {
                    margin-top: 30px;
                    padding-top: 15px;
                    border-top: 1px solid #ddd;
                    text-align: center;
                    color: #666;
                    font-size: 13px;
                }

                @media (max-width: 700px) {
                    form {
                        grid-template-columns: 1fr;
                    }

                    button {
                        grid-column: span 1;
                    }

                    body {
                        padding: 15px;
                    }
                }
            </style>
        </head>

        <body>
            <div class="container">

                <h1>☁️ Cloud Deployment Tracker</h1>

                <p class="subtitle">
                    Dynamic Flask application delivered through Git and CI/CD
                </p>

                <h2>Add Deployment</h2>

                <form method="POST" action="{{ url_for('add_deployment') }}">

                    <input
                        type="text"
                        name="application"
                        placeholder="Application name"
                        maxlength="50"
                        required
                    >

                    <select name="environment" required>
                        <option value="">Select environment</option>
                        <option value="Development">Development</option>
                        <option value="Staging">Staging</option>
                        <option value="Production">Production</option>
                    </select>

                    <input
                        type="text"
                        name="version"
                        placeholder="Version (e.g. 2.1)"
                        maxlength="20"
                        required
                    >

                    <select name="status" required>
                        <option value="">Select status</option>
                        <option value="Pending">Pending</option>
                        <option value="Deployed">Deployed</option>
                        <option value="Failed">Failed</option>
                    </select>

                    <button type="submit">Add Deployment</button>

                </form>

                <h2>Deployment Records</h2>

                <table>
                    <tr>
                        <th>ID</th>
                        <th>Application</th>
                        <th>Environment</th>
                        <th>Version</th>
                        <th>Status</th>
                    </tr>

                    {% for deployment in deployments %}
                    <tr>
                        <td>{{ deployment["id"] }}</td>
                        <td>{{ deployment["application"] }}</td>
                        <td>{{ deployment["environment"] }}</td>
                        <td>{{ deployment["version"] }}</td>
                        <td class="status">{{ deployment["status"] }}</td>
                    </tr>
                    {% endfor %}
                </table>

                <div class="api-link">
                    <a href="/api/deployments">
                        View JSON API → /api/deployments
                    </a>
                </div>

                <footer>
                    Cloud-Based CI/CD Pipeline |
                    Running Commit: <strong>{{ commit }}</strong>
                </footer>

            </div>
        </body>
        </html>
        """,
        deployments=deployments,
        commit=COMMIT,
    )


@app.route("/deployments", methods=["POST"])
def add_deployment():
    application = request.form.get("application", "").strip()
    environment = request.form.get("environment", "").strip()
    version = request.form.get("version", "").strip()
    status = request.form.get("status", "").strip()

    valid_environments = {"Development", "Staging", "Production"}
    valid_statuses = {"Pending", "Deployed", "Failed"}

    if (
        not application
        or not version
        or environment not in valid_environments
        or status not in valid_statuses
    ):
        return (
            "Invalid input. Provide application, version, "
            "a valid environment, and a valid status.",
            400,
        )

    # Limit lengths to keep the stored data reasonable
    if len(application) > 50 or len(version) > 20:
        return "Application name or version is too long.", 400

    deployments.append(
        {
            "id": len(deployments) + 1,
            "application": html.escape(application),
            "environment": environment,
            "version": html.escape(version),
            "status": status,
        }
    )

    return redirect(url_for("home"))


@app.route("/api/deployments")
def api_deployments():
    return jsonify(deployments)


@app.route("/health")
def health():
    return {
        "status": "ok",
        "commit": COMMIT,
    }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)