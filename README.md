# CarStarter

This program is to handel web requests and process them into actions for a Mazda automobile.  

For Blog Post See: https://www.georgeaboudiwan.ga/projects/automated-engine-starter  
 

The program is capable of locking and unlocking an automobile as well as starting the vehicle

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

1. Install packages from requirements.txt
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
