from src.utils import Spinner
import json
import requests
spinner = Spinner()

def main(): 
    url_loc = "http://127.0.0.1:5000/"
    aws_loc = "http://HouseMvp-env.9zyhxaxxek.us-east-1.elasticbeanstalk.com"

    good_address = "3400 Pacific Ave., Marina Del Rey, CA, 90292"
    bad_address = "7543 Heron Hill Dr. Downingtown Michigan 19335"

    spinner.start()
    data = {'address': good_address}
    r = requests.post(aws_loc, data=json.dumps(data))
    spinner.stop()

    print(f"good address responded: {r}.\nthe content of the resonse was {r.json()}")

    spinner.start()
    data = {'address': bad_address}
    r = requests.post(aws_loc, data=json.dumps(data))
    spinner.stop()

    print(f"the bad address responded: {r}.\nthe content of the resonse was {r.json()}")
    pass

if __name__=='__main__': 
    main()
