

add_params = {
    "date" : "20200701",
    "quantity" : "3"
}

add_resp = requests.post(url=f"{graph_url}/testgraph01", headers=graph_header, json=add_params)

print(add_resp.text)