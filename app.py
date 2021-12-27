from flask import Flask
from flask import request
from flask import Response
import asyncio
import pymazda
import configContext

#gunicorn --bind 0.0.0.0:5000 app:app

app = Flask(__name__)
cred = configContext.Config()


@app.route('/unlock', methods=['GET'])
async def unlock() -> None:
    key = request.args.get('key')
    if key != cred.api_key:
        return Response(status=403)

    client = pymazda.Client(cred.username, cred.password, "MNAO")
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
    return Response(status=200)


@app.route('/lock', methods=['GET'])
async def lock() -> None:
    key = request.args.get('key')
    if key != cred.api_key:
        return Response(status=403)

    client = pymazda.Client(cred.username, cred.password, "MNAO")

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
    return Response(status=200)


@app.route('/startEngine', methods=['GET'])
async def startEngine() -> None:
    key = request.args.get('key')
    if key != cred.api_key:
        return Response(status=403)

    client = pymazda.Client(cred.username, cred.password, "MNAO")


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
    return Response(status=200)


if __name__ == '__main__':
    app.run()