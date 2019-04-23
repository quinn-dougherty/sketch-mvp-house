''' attempting to do it not as RESTful ''' 
from flask import Flask, request, jsonify#, response_class
import json
import pickle
import numpy as np
from typing import List, Tuple

def cityfunc(x: str) -> Tuple[float, float]:
    ''' Take an address and return an upper and lower bound on it's price '''
    print("TODO: IMPLEMENT address -> (lower, upper) bound FUNCTION")
    # TODO -- return df[df.city==parse_out_city_from_address(address)].min(),  df[df.city==parse_out_city_from_address(address)].max()
    return (0, 100000)

application = app = Flask(__name__)

@app.route("/", methods=['POST'])      #<ligid>/<seqid>", methods=['POST']
def get():
    lines = request.get_json(force=True)
    address: str = lines['address'] # keys in file test_json_get.py
    predictants: List[float] = lines['predictands']

    with open('RFR_mvp_pick.pickle', 'rb') as rp:
        rfr, report = pickle.load(rp)


    valuation = rfr.model.predict(np.array([example_inp]))[0]

    outdat = {'upper_lower_bound_by_city': cityfunc(address), 'valuation': valuation}
    
    response = app.response_class(
            response=json.dumps(outdat), 
            status=200, 
            mimetype='application/json'
            )

    #response = Response(outdat, stat
    return response

if __name__=='__main__': 
    app.run(debug=True)

