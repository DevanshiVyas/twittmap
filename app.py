from flask import Flask, render_template, request

app = Flask(__name__)

keywords = ["trump", "sanders", "election", "presendential"]

@app.route('/')
def index():
    coords = [
        [65.0390625, 51.83577752045248],
        [-97.734375, 34.59704151614417],
        [-77.03238901390978, 38.913188059745586],
        [-57.65624999999999, -12.211180191503985],
        [70.6640625, 21.94304553343818],
        [75.9375, 27.68352808378776],
        [-122.414, 37.776]
    ]
    query = request.args.get('q', None)
    return render_template("index.html", coords=coords, keywords=keywords, query=query)

if __name__ == "__main__":
    app.run(debug=True)
