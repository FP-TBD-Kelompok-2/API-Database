from DB.utils.Neo4JConnection import Neo4jConnection
import yaml
import pandas as pd

with open("./app.yaml", "r") as stream:
    try:
        env = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

DB_URI = env["env_variables"]["CLOUD_NEO4J_URI"]
DB_USERNAME = env["env_variables"]["CLOUD_NEO4J_USERNAME"]
DB_PASSWORD = env["env_variables"]["CLOUD_NEO4J_PASSWORD"]


def open_conn():
    return Neo4jConnection(DB_URI, DB_USERNAME, DB_PASSWORD)


def cleaning_data(data):
    return pd.DataFrame(data).sort_values(by=['n.antutuScore']).to_json(orient='records')


def get_product_ranking():
    conn = open_conn()
    query = "MATCH (n) RETURN n.deviceId, n.deviceName, n.devicePrice, n.antutuScore, n.picUrl"
    raw_data = [dict(_) for _ in conn.query(query)]
    return cleaning_data(raw_data)




