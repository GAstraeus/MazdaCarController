# CarStarter

This program is to handel web requests and process them into actions for a Mazda automobile. 

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
--------
[Default]  
api_key =   
username =   
password =   

### Useage 
GET Requests to server
* /unlock?key=<>
* /lock?key=<>
* /startEngine?key=<>