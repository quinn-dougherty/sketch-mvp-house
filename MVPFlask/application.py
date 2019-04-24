''' attempting to do it not as RESTful '''
from flask import Flask, request, jsonify  # , response_class
import json
import pickle
import numpy as np
from typing import List, Tuple
import re
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
from pyzillow.pyzillowerrors import ZillowError
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

ZILLOW_KEY = os.environ['ZILLOW_KEY']


def addr_zip_split(raw_add: str) -> Tuple[str, str]:
    zippat = r'[0-9]{5}$'
    zipcode = re.search(zippat, raw_add).group()
    address = raw_add[:(len(raw_add) - len(zipcode) - 1)]
    return address, zipcode


def cityfunc(x: str) -> Tuple[float, float]:
    ''' Take an address and return an upper and lower bound on it's price '''
    print("TODO: IMPLEMENT address -> (lower, upper) bound FUNCTION")
    # TODO -- return df[df.city==parse_out_city_from_address(address)].min(),
    # df[df.city==parse_out_city_from_address(address)].max()
    return (0, 100000)


application = app = Flask(__name__)
app.config['TESTING'] = True
with open('src/RFR_mvp1.pkl', 'rb') as rp:
    rfr, report = pickle.load(rp)

print(report)


@app.route("/", methods=['POST'])
def get():
    lines = request.get_json(force=True)
    address_: str = lines['address']
    predictants: List[float] = lines['predictands']

    address, zipcode = addr_zip_split(address_)

    try:
        # doing this in try-except is crucial, because of the way zillow fails
        # when you give it an address that it doesn't want to / can't use
        zillow_data = ZillowWrapper(ZILLOW_KEY)
        deep_search_response = zillow_data.get_deep_search_results(
            address, zipcode)
        result = GetDeepSearchResults(deep_search_response)

        # ['home_size', 'home_size', 'last_sold_price']
        predictants: List[float] = [
            result.home_size,
            result.bedrooms,
            result.bathrooms]

        valuation: float = rfr.model.predict(np.array([predictants]))[0]

        outdat = {'upper_lower_bound_by_city': cityfunc(
            address), 'valuation': valuation}

        response = app.response_class(
            response=json.dumps(outdat),
            status=200,
            mimetype='application/json'
        )

        print(outdat)

        return response

    except ZillowError as e1:
        message = "address given not available in zillow api. Please try another address"
        print(message)

        return app.response_class(response=json.dumps({"FAIL": message}),
                                  status=200,
                                  mimetype='application/json'
                                  )


if __name__ == '__main__':
    app.run(debug=True)
