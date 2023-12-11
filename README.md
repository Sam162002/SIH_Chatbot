# CaguiBot

This Telegram Bot was constucted by me and Kuber Vajpayee(https://github.com/kuber2001) for the Smart India Hackathon 2022 Finale. 
It contains code for the deployed Flask server of the Telegram CaguiBot. The conversational AI integrated
with our CaGui App to provide AI based counselling for high school students.

# Introduction

Google Dialogflow is a conversational AI platform developed by Google. It allows developers to build and deploy chatbots and other conversational interfaces for various applications. Dialogflow provides a variety of tools for creating and managing conversational experiences, including a natural language understanding engine, pre-built agents, and integrations with other Google services such as Google Assistant and Google Cloud Speech-to-Text.
It uses a flow-based programming model, where developers can create conversational flows by defining intents and entities, which are used to map user inputs to specific actions or responses. Dialogflow also provides a web-based console for testing and debugging the conversational interfaces, as well as analytics and monitoring features.

Flask is a lightweight web framework for Python that provides useful tools and features for creating web applications. It is classified as a microframework because it does not require particular tools or libraries. It has a small and easy-to-extend core.

ngrok.io is a service and command-line tool that enables developers to expose their local web servers to the internet. It creates a secure tunnel from a public endpoint to a locally running web service. ngrok allows you to access your local web server, running on your development machine, from anywhere in the world.
One of the main use cases for ngrok is testing webhooks and APIs that are hosted on a local development environment.

# TechStack

- Google Dialogflow
- Python Flask
- ngrok.io
- External APIs


## Run Locally

### To construct the Google Dialogflow bot

1.	Go to the DialogFlow ES console
2.	Create a new Project
3.	Import the zip file provided in the repository
4.	Create the Flask Server and enable webhook services in Dialogflow providing the Webhook url of ngrok

### Deploy the Flask Server

Clone the project

```bash
  git clone https://github.com/Demogorgon24242/CaguiBot
```

Go to the project directory

```bash
  cd CaguiBot
```

Install libraries

```python
  pip install -r requirements.txt
```

Run python file

```bash
  python app.py
```

Go to ngrok.io (after creating and setting up the software)

```
  ngrok http (app.server.py port destination)
```

## Note :- This is for testing only not for deployment
