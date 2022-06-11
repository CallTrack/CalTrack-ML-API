# CalTrack-ML-API

CalTrack-ML-API is an API that functions to process our Machine Learning model by prediction through image uploaded by user when the user hit /predict route API.

This project uses several libraries/packages that allow this API to be formed, including:
- **Flask**: Flask is a web framework, it’s a Python module that lets you develop web applications easily. It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.
- **psycopg2**: Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection).
- **tensorflow**: TensorFlow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.
- **keras**: Keras is an API designed for human beings, not machines. Keras follows best practices for reducing cognitive load: it offers consistent & simple APIs, it minimizes the number of user actions required for common use cases, and it provides clear & actionable error messages. It also has extensive documentation and developer guides.
- **cors**: a module to enable cors options in server configuration.

This repository contains several files that are very important to run the API succesfully whether it in localhost or Cloud (through cloud run)
- **main.py**: Main application to run the web server, all routes are defined in this files such as main route ('/') and route for prediction and run the machine learning model ('/predict')
- **my_model_92.h5**: Machine learning model with .h5 extensions
- **Dockerfile**: Docker configuration for running the app in cloud
- **requirements.txt**: This file contains all dependencis/requirements that are needed for the application to run in cloud

## Run the API
### Run Locally
Several tools you need to install:
- PostgreSQL: https://www.postgresql.org/
- git: https://git-scm.com/
- Postman: https://www.postman.com/
- Python3: https://www.python.org/downloads/

1. Make new project folder, change the directory to the new folder and then git clone this repository
   ```bash
   git clone https://github.com/CallTrack/CalTrack-ML-API.git
   ```
2. Open your IDE (VSCode or Pycharm) and then open the folder that contains this repository
3. Create virtual environment with this command :
   ```bash
   python -m venv
   ```
4. Install all requirements that are needed (you can see in the requirements.txt file)
5. Run the main.py files with this command :
  ```bash
  python main.py
  ```
  or if you are using pycharm, just run it by simply clicking the run button on top-right of the IDE
6. To create database and tables for test this API, you can just simply take a look at this doc : https://github.com/CallTrack/CalTrack-API-Express/edit/master/README.md
7. Test the API routes using postman. for upload image in the postman, you have to change the body to form-data and upload any images that you want

### Run in the Cloud
1. Create new project in GCP
2. Open Cloud Shell
3. Git clone the repository
   ```bash
   git clone https://github.com/CallTrack/CalTrack-ML-API.git
   ```
4. Heading to the project by using this command :
   ```bash
   cd CalTrack-ML-API
   ```
5. Build container based on the dockerfile, make sure you are still in the directory where the dockerfile is there, use this command to build the container
   ```bash
   gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/any-name-with-lowercase
   ```
6. Wait and make sure the container is created, if you want to check it just simply heading to 'container registry' in GCP
7. Find Cloud Run service by searching it
8. Click 'Create New Service'
9. Fill all option based on your needed
10. Upload image container
11. On the connection part choose your CloudSQL service name
12. Click 'deploy'
13. Wait and there will be an URL created for you
14. Test the API using postman
