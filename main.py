from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel
from typing import List, Optional
import base64
import logging
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GITHUB_API = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

class Project(BaseModel):
    id: int
    rank: Optional[int] = None
    title: str
    slug: str
    description: str
    github_readme: str
    image: str
    technologies: List[str]
    github: str
    liveDemo: str
    Featured_on_home_page: bool = False


@app.get("/github-projects/{username}", response_model=List[Project])
async def get_github_projects(username: str):
    async with httpx.AsyncClient() as client:
        try:
            repos_response = await client.get(
                f"{GITHUB_API}/users/{username}/repos?per_page=100",
                headers=HEADERS
            )
            repos_response.raise_for_status()
            repos = repos_response.json()

            if not isinstance(repos, list):
                logger.error(f"Unexpected response: {repos}")
                raise HTTPException(status_code=500, detail="Unexpected GitHub response format.")

            projects = []

            for repo in repos:
                if not isinstance(repo, dict):
                    logger.warning(f"Skipping malformed repo entry: {repo}")
                    continue

                repo_name = repo.get("name", "")
                readme_url = f"{GITHUB_API}/repos/{username}/{repo_name}/readme"
                content = "README not available"

                try:
                    readme_response = await client.get(readme_url, headers=HEADERS)
                    if readme_response.status_code == 200:
                        readme_data = readme_response.json()
                        content = base64.b64decode(readme_data.get("content", "")).decode("utf-8")
                except Exception as e:
                    logger.warning(f"Could not fetch README for {repo_name}: {e}")

                project = Project(
                    id=repo.get("id", 0),
                    title=repo_name,
                    slug=repo_name.lower().replace(" ", "-"),
                    description=repo.get("description") or "No description provided",
                    github_readme=content,
                    image=f"/images/{repo_name}",
                    technologies=[],  # Placeholder, can parse topics/languages later
                    github=repo.get("html_url", ""),
                    liveDemo=repo.get("homepage") or "",
                    Featured_on_home_page=False
                )
                projects.append(project)

            return projects

        except httpx.HTTPStatusError as http_exc:
            logger.error(f"GitHub API error: {http_exc}")
            raise HTTPException(status_code=http_exc.response.status_code, detail="GitHub API error.")
        except Exception as e:
            logger.error(f"Unhandled exception: {e}")
            raise HTTPException(status_code=500, detail="Internal server error.")
