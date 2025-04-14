A Python FastAPI-based API that fetches and formats detailed information about a GitHub user's public repositories — perfect for developer portfolios, dashboards, or auto-generated project showcases.

---

## 🚀 Features

- 🔍 Extracts repo title, slug, description, README
- 🖼️ Prepares project data with image placeholders
- 🌐 Includes GitHub URL and live demo (if available)
- 🔧 Supports optional authentication using GitHub Token
- 📤 Ideal for integrating into a portfolio site

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **httpx**
- **GitHub REST API**
- **dotenv**

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Ankush2201/github_info_extract.git
cd github_info_extract
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create `.env` file:**

```bash
GITHUB_TOKEN=your_github_token_here
```

> Using a token increases your API rate limit from 60 to 5000 requests/hour.

---

## ⚙️ Usage

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

Open your browser:

- 📂 Swagger docs: `http://localhost:8000/docs`
- 🔗 Main endpoint: `http://localhost:8000/github-projects/<your-github-username>`

Example:

```bash
GET http://localhost:8000/github-projects/Ankush2201
```

---

## 📄 Example Response

```json
[
  {
    "id": 123456,
    "rank": null,
    "title": "ai-chatbot",
    "slug": "ai-chatbot",
    "description": "A chatbot using OpenAI's GPT-4 model to assist users.",
    "github_readme": "# AI Chatbot\n\nThis project is powered by...",
    "image": "/images/ai-chatbot",
    "technologies": [],
    "github": "https://github.com/Ankush2201/ai-chatbot",
    "liveDemo": "",
    "Featured_on_home_page": false
  }
]
```

---

## 🧪 Development

You can customize:

- Technologies parsing (from repo topics or README)
- Image URLs for display
- Slug formatting rules
- Add rank or homepage featured logic

---

## 👤 Author

**Ankush Pandey**  
📎 [GitHub](https://github.com/Ankush2201)  

