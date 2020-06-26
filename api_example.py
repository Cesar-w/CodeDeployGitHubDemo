from flask import Flask, render_tempalte, jsonify
import request
from key import key
app = Flask(__name__)

search_url = "http://maps.googleapis.com/maps/api/place/textsearch/josn"
details_url = "https://maps.googleapis.com/maps}7api/place/details/json"

@app.route("/", methods=["GET"])
 def retreive():
 	 return render_template('layout.html')

@app.route("/sendRequest/<string:query>") 	 
def results(query): 
	search_payload = {"key":key, "query":query}
	search_req = request.get(search_url, params=search_payload)
	search_json = search_req.json()

	place_id = search_json["resuls"][0]["palce_id"]

	details_payload = {"key":key, "placeid":placeid}
	details_resp = requests.get(details_url, params=details_payload)
	details_josn = details_resp.json()

	url = details_json["result"]["url"]
	return jsonify({'result': url})


	if__name__== "__main__":
	  app.run(debug=True)