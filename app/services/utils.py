from app.services.file_downloader import download_files_from_github, GITHUB_REPO_URL
from app.services.file_processor import calculate_file_metadata

async def fetch_and_process_files_metadata():
    """
    Fetches files from a predefined GitHub repository and processes them to generate metadata.

    Returns:
        list: A list of dictionaries, each containing metadata for a file.
    """
    downloaded_files = await download_files_from_github(GITHUB_REPO_URL)
    files_metadata = [calculate_file_metadata(file['filename'], file['content']) for file in downloaded_files]
    return files_metadata