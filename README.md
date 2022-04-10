# CarStarter

This program can be used to manage and control your Mazda veichle. 
It can connect to Apple Shortcuts app, Smart Speakers, and other programs using web requests to control and manage data avout your Mazda veichle.
Currently you are able to lock, unlock, start the engine, and get status information on your veichle

## For Blog Post and example useage see: https://www.georgeaboudiwan.ga/projects/automated-engine-starter  
 

### Project Setup
This project requires python3 and rust 
1. Install Rust - Instructions can be found at https://www.rust-lang.org/tools/install
1. Set up a virtual env 
    ```shell script
    python3 -m venv venv
    ```

1. Activate venv
    ```shell script
    source venv/bin/activate
    ```

1. Install packages from requirements.txt
    ```shell script
    pip install -r requirements.txt
    ```

1. Run program using gunicorn
    ```shell script
    gunicorn --bind 0.0.0.0:5000 app:app
    ```
   
### Config File Setup  
Copy the config setup from below into a file config.ini   
the api_key is the key required to be passed as a parameter with requests to the program  
username and password are the login credentials to the MyMazda account  
```
 [Default]  
 api_key =   
 username =   
 password =
```

## Dockerfile Setup
To build and use this program in a docker container change the path on line 3 of the Dockerfile to be the path of this program
Build the container by running the command:
```bash
docker build -t car-starter  .
```
Run the container using the command
```bash
docker run -d -p 5000:5000 car-starter
```

### API Useage 
GET Requests to server
* /unlock?key=<>
* /lock?key=<>
* /startEngine?key=<>
* /status?key=<>

### Useage 
To use the api you must send a get request to the running server
The get request takes a parameter of key which is the api key you set in your config file. 

GET Requests to server
* example_api.com/unlock?key=<>
* example_api.com/lock?key=<>
* example_api.com/startEngine?key=<>