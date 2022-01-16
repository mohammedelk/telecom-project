import numpy as np
import pandas as pd


def create_db_from_csv(csv_path, conn):
    data_arr = csv_to_arr(csv_path)
    for destination, source, in data_arr:
        conn.query("merge (n1: Node{ nLabel :\"" + destination + "\" })"
        "merge (n2: Node{ nLabel :\"" + source + "\" })"
        "merge (n1)-[:CHILD_OF]->(n2)")


def csv_to_arr(csv_path):
    df = pd.read_csv(csv_path)
    arr_tree = df[['Site', 'Farend']].to_numpy()
    return np.array(arr_tree)
