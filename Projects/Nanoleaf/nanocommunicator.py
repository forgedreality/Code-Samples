# nanocommunicator
# TODO: Replace requests with aiohttp
import requests

async def make_request(request, data):
    if request == "get":
        controller_ip = data[0]
        controller_token = data[1]
        endpoint = data[2]

        return requests.get(f'http://{controller_ip}:16021/api/v1/{controller_token}/{endpoint}').json()

    elif request == "put":
        controller_ip = data[0]
        controller_token = data[1]
        endpoint = data[2]
        payload = data[3]

        return requests.put(f'http://{controller_ip}:16021/api/v1/{controller_token}/{endpoint}', payload)

    else:
        print("Problem with input.")
        return "Invalid input."


async def get_layout(controller):
    return await make_request('get', [controller.ip, controller.token, controller.endpoints["layout"]])


async def get_status(controller):
    return await make_request('get', [controller.ip, controller.token, controller.endpoints["state"]])


async def get_effects(controller):
    return await make_request('get', [controller.ip, controller.token, controller.endpoints["effectsList"]])
