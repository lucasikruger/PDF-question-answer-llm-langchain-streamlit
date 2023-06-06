# PDF Question Answering Application

![Logo](src/logo.png)

This application is an AI-based solution built with Python and Streamlit. It utilizes various libraries like `PyPDF2`, `dotenv`, `FAISS` and OpenAI's `GPT-4` to provide answers to user queries about the content in a PDF document. Users can upload a PDF document and ask questions related to the document. The AI model scans the PDF, extracts relevant information, and responds to user queries in real time.

## Installation

You will need Docker to run this application. Docker makes it easy to create, deploy, and run applications by using containers. If you haven't installed Docker, please follow the instructions on the [official Docker website](https://docs.docker.com/get-docker/).

## Setup

### Step 1: Clone the repository

Clone the repository using the following command in your terminal:

```bash
git clone https://github.com/lucasikruger/PDF-question-answer-llm-langchain-streamlit
```

### Step 2: Set up the .env file

You will need to create a `.env` file to store your OpenAI API Key. Create a new file named `.env` **in the `./src` directory** of the project and add the following line to it:

```bash
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_openai_api_key` with your actual OpenAI API key.

### Step 3: Build and run the Docker container

Navigate to the project's root directory in your terminal and run the following command to build and run the Docker container:

```bash
docker-compose up
```

This command will build the Docker image and run the container. The Streamlit server is exposed on port `8501` of your machine. 

You can access the application by opening a web browser and visiting `http://localhost:8501`.

## Usage

To use the application, follow these steps:

1. Upload a PDF file by clicking the "Upload your PDF" button.
2. Enter your question about the content of the PDF in the "Write your question and press ENTER." text field.
3. The application will process your question, analyze the PDF content, and provide the most accurate answer it can find.

Here's an example of how the application looks and functions:

![Example Image](img.png)

---

## Support

If you encounter any issues or have any questions about this application, please open a GitHub issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

---

We hope you find this application useful, and we look forward to your contributions!