# serve mvp w flask

zillow api needs key. 

get your key and run `export ZILLOW_KEY="whatever"` before trying to run it

## This is currently running on `HouseMvp-env.9zyhxaxxek.us-east-1.elasticbeanstalk.com `. 

send requests of the form `{'address': string_of_address, 'predicants': [1,2,3]}` 

Honeslty just look in `TEST_REQUESTS.ipynb` for usage. 

- (note: `predicants` is actually not being used, so it'll be factored out in next version) 

I broke my pandas/python install because i was using global dependency state (like a _neanderthal_), but it worked on aws (somehow), so i'm not gonna get it back up to run locally until i've dockerized it 



