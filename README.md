# Web application with Ollama LLMs
This is a simple UI that utilizes FastAPI and Ngrok. 
![image](https://github.com/yelloejp/LLM_WebApp/assets/45250729/07288f24-1fd8-47ed-92a4-9418b50aa682)

# Installation and Setup
Before getting the porject up, make sure that you download ,,Ollama" and pull models to run LLMs on your local machine. 
Then, install ,,ngrok" and get an account for free trial.

1. Go to Ollama, download and install it : https://ollama.com/
2. Go to Ngrok, download and install it : https://ngrok.com/
3. Open a terminal and pull some models to your local machine (i.e. llama3). We will use llama3 and llama2:
   ```bash
   ollama pull llama3
   ```
4. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yelloejp/LLM_WebApp.git
   ```
5. Navigate to the project directory:
   ```bash
   cd LLM_WebApp
   ```
6. Install the required Python packages:
   ```bash
   pip install fastapi uvicorn ollama
   ```   
7. Start uvicorn on your local machine by running the following command:
   ```bash
   uvicorn src.main:app --reload --port 8080
   ```
8. Open a second terminal and Navigate to the project directory:
   ```bash
   cd LLM_WebApp
   ```
9. Run the following command in your terminal to install your ngrok authtoken and connect the ngrok agent to your account.
   You can simply copy the command line in your account details:
   ```bash
   ngrok config add-authtoken <TOKEN>
   ```
10. Start ngrok by running the following command:
      ```bash
      ngrok http 8080
      ```  
11. Then you you will get a ,,Forwarding" URL. This URL forwards any request and reeturn to your localhost. (i.e. https://1234-567-89-10.ngrok-free.app)
12. The Web application is available unter ,,/form" Path. (i.e. https://1234-567-89-10.ngrok-free.app/form)
