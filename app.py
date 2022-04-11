from flask import Flask
from flask import request
from flask import Response
import json
import pymazda
import configContext

app = Flask(__name__)
credentials = configContext.Config()


@app.route('/unlock', methods=['GET'])
async def unlock() -> None:
    key = request.args.get('key')
    if key != credentials.api_key:
        return Response(status=403)

    client = pymazda.Client(credentials.username, credentials.password, "MNAO")
    vehicles = await client.get_vehicles()
    await client.validate_credentials()

    http_status = 200

    try:
        for vehicle in vehicles:
            vehicle_id = vehicle["id"]

            status = await client.get_vehicle_status(vehicle_id)
            print(status)

            res = await client.unlock_doors(vehicle_id)
            print(res)
    finally:
        http_status = 501

    await client.close()
    return Response(status=http_status)


@app.route('/lock', methods=['GET'])
async def lock() -> None:
    key = request.args.get('key')
    if key != credentials.api_key:
        return Response(status=403)

    client = pymazda.Client(credentials.username, credentials.password, "MNAO")

    vehicles = await client.get_vehicles()
    await client.validate_credentials()

    http_status = 200

    try:
        for vehicle in vehicles:
            vehicle_id = vehicle["id"]

            status = await client.get_vehicle_status(vehicle_id)
            print(status)

            res = await client.lock_doors(vehicle_id)
            print(res)
    finally:
        http_status = 501

    await client.close()
    return Response(status=http_status)


@app.route('/startEngine', methods=['GET'])
async def startEngine() -> None:
    key = request.args.get('key')
    if key != credentials.api_key:
        return Response(status=403)

    client = pymazda.Client(credentials.username, credentials.password, "MNAO")


    vehicles = await client.get_vehicles()
    await client.validate_credentials()

    http_status = 200

    try:
        for vehicle in vehicles:
            vehicle_id = vehicle["id"]

            status = await client.get_vehicle_status(vehicle_id)
            print(status)

            await client.start_engine(vehicle_id)

    finally:
        http_status = 501

    await client.close()
    return Response(status=http_status)


@app.route('/status', methods=['GET'])
async def status() -> None:
    key = request.args.get('key')
    if key != credentials.api_key:
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
            print(car_status)

    finally:
        http_status = 501

    await client.close()
    return Response(status=http_status, response=json.dumps(car_status))

@app.route('/checkCar', methods=['GET'])
async def checkCar() -> None:
    key = request.args.get('key')
    if key != credentials.api_key:
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
            print(car_status)
            await client.close()
    finally:
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

    return Response(status=http_status, response=json.dumps(response))
if __name__ == '__main__':
    app.run()
