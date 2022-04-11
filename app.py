from flask import Flask
from flask import request
from flask import Response
import json
import pymazda
import configContext
import logging

app = Flask(__name__)
credentials = configContext.Config()
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')

@app.route('/unlock', methods=['GET'])
async def unlock() -> None:
    logging.info("Running Unlock")
    key = request.args.get('key')
    if key != credentials.api_key:
        logging.error("Authentication Failure Key:{}".format(key))
        return Response(status=403)

    client = pymazda.Client(credentials.username, credentials.password, "MNAO")
    vehicles = await client.get_vehicles()
    await client.validate_credentials()

    http_status = 200

    try:
        for vehicle in vehicles:
            vehicle_id = vehicle["id"]

            status = await client.get_vehicle_status(vehicle_id)

            res = await client.unlock_doors(vehicle_id)
            logging.info("Unlocked Doors")
    except Exception as e:
        logging.error("Error Connecting to Mazda: {}".format(e))
        http_status = 501

    await client.close()
    return Response(status=http_status)


@app.route('/lock', methods=['GET'])
async def lock() -> None:
    logging.info("Running Lock")
    key = request.args.get('key')
    if key != credentials.api_key:
        logging.error("Authentication Failure Key:{}".format(key))
        return Response(status=403)

    client = pymazda.Client(credentials.username, credentials.password, "MNAO")

    vehicles = await client.get_vehicles()
    await client.validate_credentials()

    http_status = 200

    try:
        for vehicle in vehicles:
            vehicle_id = vehicle["id"]

            status = await client.get_vehicle_status(vehicle_id)

            res = await client.lock_doors(vehicle_id)
            logging.info("Locked Doors")
    except Exception as e:
        logging.error("Error Connecting to Mazda: {}".format(e))
        http_status = 501

    await client.close()
    return Response(status=http_status)


@app.route('/startEngine', methods=['GET'])
async def startEngine() -> None:
    logging.info("Running Start Engine")
    key = request.args.get('key')
    if key != credentials.api_key:
        logging.error("Authentication Failure Key:{}".format(key))
        return Response(status=403)

    client = pymazda.Client(credentials.username, credentials.password, "MNAO")

    vehicles = await client.get_vehicles()
    await client.validate_credentials()

    http_status = 200

    try:
        for vehicle in vehicles:
            vehicle_id = vehicle["id"]

            status = await client.get_vehicle_status(vehicle_id)
            await client.start_engine(vehicle_id)

            logging.info("Started Engine")
    except Exception as e:
        logging.error("Error Connecting to Mazda: {}".format(e))
        http_status = 501

    await client.close()
    return Response(status=http_status)


@app.route('/status', methods=['GET'])
async def status() -> None:
    logging.info("Running Status")
    key = request.args.get('key')
    if key != credentials.api_key:
        logging.error("Authentication Failure Key:{}".format(key))
        return Response(status=403)

    client = pymazda.Client(credentials.username, credentials.password, "MNAO")

    vehicles = await client.get_vehicles()
    await client.validate_credentials()

    http_status = 200
    car_status = {}

    try:
        for vehicle in vehicles:
            vehicle_id = vehicle["id"]

            car_status = await client.get_vehicle_status(vehicle_id)

            logging.info("Got Status: {}".format(json.dumps(car_status)))
    except Exception as e:
        logging.error("Error Connecting to Mazda: {}".format(e))
        http_status = 501

    await client.close()
    return Response(status=http_status, response=json.dumps(car_status))

@app.route('/checkCar', methods=['GET'])
async def checkCar() -> None:
    logging.info("Running Check Car")
    key = request.args.get('key')
    if key != credentials.api_key:
        logging.error("Authentication Failure Key:{}".format(key))
        return Response(status=403)

    client = pymazda.Client(credentials.username, credentials.password, "MNAO")

    vehicles = await client.get_vehicles()
    await client.validate_credentials()

    http_status = 200
    car_status = {}

    try:
        for vehicle in vehicles:
            vehicle_id = vehicle["id"]

            car_status = await client.get_vehicle_status(vehicle_id)
            await client.close()
            logging.info("Got Status: {}".format(json.dumps(car_status)))
    except Exception as e:
        logging.error("Error Connecting to Mazda: {}".format(e))
        http_status = 501
        return Response(status=http_status, response=json.dumps(car_status))

    response = {"doors_open" : False, "locks_open" : False, "windows_open" : False}

    for door,door_status in car_status["doors"].items():
        if door == "fuelLidOpen":
            continue
        if door_status == True:
            response["doors_open"] = True

    for lock, lock_status in car_status["doorLocks"].items():
        if lock_status == True:
            response["locks_open"] = True

    for window, window_status in car_status["windows"].items():
        if window_status == True:
            response["windows_open"] = True

    logging.info("Car Check Found: {}".format(response))
    return Response(status=http_status, response=json.dumps(response))


if __name__ == '__main__':
    app.run()
