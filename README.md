# File Metadata Gathering Application

This application provides an API to download metadata for files stored in a GitHub repository. It supports two endpoints: one for fetching the metadata as JSON and another for downloading the metadata as a CSV file.

### Prerequisites

Before proceeding, make sure you have Docker installed on your system. If you don't have Docker installed, please follow the instructions for your operating system on the [Docker website](https://docs.docker.com/get-docker/).

### Cloning the Repository

To get started, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/pallavi-raiturkar/wmt-pallavi-raiturkar.git
cd wmt-pallavi-raiturkar
```

### Building the Docker image

With Docker installed and the repository cloned, you can build the Docker image using:

```bash
docker build -t wmt-pallavi-raiturkar-im .
```
### Running the Docker Container

After building the image, you have two options to run the container: in detached mode or in foreground mode. 

The container will automatically call the CSV endpoint and download the CSV file when it starts. The downloaded file will be named interview.csv and will be located in the current working directory on your host machine. The server will continue to be up following the download.

Note: When running the container, Docker might request access to your current directory or specified volume in order to save the interview.csv file to your system. Please ensure you grant the necessary permissions for Docker to access the directory where you wish to save the file.

#### Detached Mode

Run the container in detached mode (in the background) with the following command:

```bash
docker run --name wmt-pallavi-raiturkar-file-metadata-0.0.1 -p 80:80 -v $(pwd):/app -d wmt-pallavi-raiturkar-im
```

In detached mode, you can view the logs at any time using the following command:

```bash
docker logs wmt-pallavi-raiturkar-file-metadata-0.0.1
```

#### Foreground Mode

Alternatively, if you prefer to run the container in the foreground to see the logs directly in the terminal, omit the `-d` flag:

```bash
docker run --name wmt-pallavi-raiturkar-file-metadata-0.0.1 -p 80:80 -v $(pwd):/app wmt-pallavi-raiturkar-im
```

Running in foreground mode will allow you to see the output in real-time. To stop the container, you can use `Ctrl+C` in the terminal.

### Stopping the Container

If you ran the container in detached mode and you're finished, you can stop the running container using:

```bash
docker stop wmt-pallavi-raiturkar-file-metadata-0.0.1
```

### Removing the Container (Optional)

If you wish to remove the container after stopping it, use:

```bash
docker rm wmt-pallavi-raiturkar-file-metadata-0.0.1
```

### Additional Information

For more detailed information about the endpoints and how to interact with the API, please refer to the API documentation which is available at http://localhost/docs when the server is running.
