# Smart Vision

**'Smart Vision'** is a human intrusion detection based system which detects unknown/uninvited person in the owner's house and notify the user via Call and SMS. 

## Description
'Smart Vision' is a human intrusion detection based system which makes use of **yolov3-tiny** model in detecting if an unknown or uninvited person tries to enter owner's room. Once the person is detected, it would send a automated emergency sms and also call the owner using twilio-API.A **log file**(with timestamps of the intrusion) along with the **video footage** is also generated for later investigation purposes. 

## Requirements
All the necessary python modules and libraries are mentioned in **requirements.txt** file. Make sure you have them installed(or install them if not present) before running the project.

## Installation
- Install all libraries mentioned in requirements.txt
- For twilio setup, please make a free account [here](https://www.twilio.com/try-twilio) and paste the obtained the account id and auth_token in call.py file.

Wohoo! You are done with the environment setup, it's time to test it now.
## Usage
- Run the following file and see the results by yourself.
- When the main window appears, click on 'Show Log' button to see the log file.
 ```python
main.py
```

## Want to Contribute?
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
