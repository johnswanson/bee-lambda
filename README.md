# Bee-Lambda

I wanted a physical button to press after I cleaned up my kitchen for my [beeminder goal](http://beeminder.com/jds02006/clean-counters). For obvious
reasons of coolness, and whatnot.

I bought an AWS IoT button. Basically you:

- put the button in configuration mode, by holding down the button for ~5 seconds
- connect to the button's wifi from your computer
- run through the button config process
- hook up the button to an AWS Lambda function

This repo is for that last part. AWS Lambda is pretty weird in that you have to send them a zip file containing your code
and *all* your dependencies, and everything has to be installed at the root of the zip file.

The `build` script will take care of that for you. Run `./build` to bundle the single dependency (`requests`) and `lambda_function.py` into `out.zip`.

Send that over to AWS, set the correct environment variables (`BEEMINDER_GOAL` and `BEEMINDER_AUTH_TOKEN`) for your lambda func, and you'll be good to go!
