import json, datetime

def audit_log(event, payload):
    log = {
        "ts": datetime.datetime.utcnow().isoformat(),
        "event": event,
        "payload": payload
    }
    with open("compliance.log", "a") as f:
        f.write(json.dumps(log) + "\n")
