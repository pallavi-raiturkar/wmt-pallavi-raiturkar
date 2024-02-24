from typing import Any
import aiohttp
import asyncio

GITHUB_REPO_URL = "https://api.github.com/repos/BrainMonkey/sample-files/contents/"

async def download_files_from_github(github_repo_url: str) -> list[dict[str, bytes | Any]]:
    """
    Asynchronously downloads all files from a GitHub repository.

    Args:
        github_repo_url (str): The API URL of the repository to download files from.

    Returns:
        list: A list of dictionaries with file names as keys and content as values.
    """
    file_infos = await list_files_in_repo(github_repo_url)
    tasks = []
    async with aiohttp.ClientSession() as session:
        for file_info in file_infos:
            url = file_info['download_url']
            task = asyncio.create_task(download_file_from_github(session, url), name=file_info['name'])
            tasks.append((file_info['name'], task))  # Store the filename with its associated task

        # Wait for all tasks to complete
        files = []
        for name, task in tasks:
            content = await task
            files.append({"filename": name, "content": content})

    return files

async def download_file_from_github(session: aiohttp.ClientSession, url: str) -> bytes:
    """
    Asynchronously downloads a file from a GitHub URL using aiohttp session.

    Args:
        session (aiohttp.ClientSession): The aiohttp session to use for the request.
        url (str): The URL of the file to download from GitHub.

    Returns:
        bytes: The content of the file.
    """
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.read()

async def list_files_in_repo(github_repo_url: str) -> list:
    """
    Asynchronously lists files in the specified GitHub repository.

    Args:
        github_repo_url (str): The API URL of the repository to list files from.

    Returns:
        list: A list containing dictionaries with 'name' and 'download_url' of the files.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(github_repo_url) as response:
            response.raise_for_status()
            json_response = await response.json()
            files = []
            for file_info in json_response:
                if file_info['type'] == 'file' and file_info['name'].lower() != 'readme.md':
                    files.append({"name": file_info['name'], "download_url": file_info['download_url']})
            return files