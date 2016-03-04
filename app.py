from flask import Flask, render_template, request
from elasticsearch import Elasticsearch, exceptions

app = Flask(__name__)
es = Elasticsearch()

keywords = ["trump", "sanders", "election", "presendential"]

@app.route('/')
def index():
    query = request.args.get('q', '')
    res = es.search(
        index="faaltu",
        body={
            "query": {"match": {"text": query}},
            "size": 750 # max document size
        })
    coords = []
    if res["hits"]["hits"]:
        coords = [r["_source"]["coordinates"] for r in res["hits"]["hits"]]
    return render_template("index.html", coords=coords, keywords=keywords, query=query)

if __name__ == "__main__":
    app.run(debug=True)
