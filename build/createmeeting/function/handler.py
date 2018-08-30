import pyqrcode
import json
import uuid
import base64

def handle(req):
    result = {}
    json_req = json.loads(req)

    meeting_title = json_req["name"] + "/@Loc-" + json_req["location"] + "@" + json_req["date"] +"@"+ json_req["time"]
    result["title"] = meeting_title

    generated_uuid = meeting_title + " " + str(uuid.uuid4())
    result["id"] = generated_uuid

    img = pyqrcode.create(generated_uuid)

    img.png('code.png', scale=6, module_color=[0, 0, 0, 128])
    with open("code.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    result["img"] = encoded_string

    print json.dumps(result)

