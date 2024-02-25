import pytest
import aiohttp
from app.services.file_downloader import download_files_from_github, download_file_from_github, list_files_in_repo, GITHUB_REPO_URL

@pytest.mark.asyncio
async def test_list_files_in_repo():
    # Testing list_files_in_repo to ensure it retrieves file information correctly.
    file_infos = await list_files_in_repo(GITHUB_REPO_URL)
    assert isinstance(file_infos, list)
    assert len(file_infos) > 0  # Assuming the repo contains files
    assert all("name" in file_info and "download_url" in file_info for file_info in file_infos)

@pytest.mark.asyncio
async def test_download_file_from_github():
    # Testing download_file_from_github with a known file URL.
    async with aiohttp.ClientSession() as session:
        file_info = {
            "name": "sample_file_0.txt",
            "download_url": "https://raw.githubusercontent.com/BrainMonkey/sample-files/main/sample_file_0.txt"
        }
        content = await download_file_from_github(session, file_info['download_url'])
        assert content  # Content should not be empty

@pytest.mark.asyncio
async def test_download_files_from_github():
    # Testing download_files_from_github to ensure it returns correct structures.
    files = await download_files_from_github(GITHUB_REPO_URL)
    assert isinstance(files, list)
    assert len(files) > 0  # Assuming the repo contains files
    assert all(isinstance(file, dict) for file in files)
    assert all("filename" in file and "content" in file for file in files)