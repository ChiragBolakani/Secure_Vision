# Secure Vision
##https://youtu.be/t4bRtTj07Bw

**'Secure Vision'** is a human intrusion detection based system which detects unknown/uninvited person in the owner's house and notify the user via Call and SMS. 

## Description
**'Secure Vision'** is a human intrusion detection based system which makes use of **yolov3-tiny** model in detecting if an unknown or uninvited person tries to enter owner's room. Once the person is detected, it would send a automated emergency sms and also call the owner using twilio-API. A **log file** (with timestamps of the intrusion) along with the **video footage** is also generated for later investigation purposes. 

## Requirements
All the necessary python modules and libraries are mentioned in **requirements.txt** file. Make sure you have them installed(or install them if not present) before running the project.

## Installation
- Install all libraries mentioned in requirements.txt

Wohoo! You are done with the environment setup, it's time to test it now.
## Usage
- Run the below file and see the results by yourself.
- When the main window appears, click on 'Show Log' button to see the log file.
 ```python
main.py
```
![Screenshot from 2021-01-10 10-31-35](https://user-images.githubusercontent.com/62014238/104116094-85ecda00-533b-11eb-8b8c-c54dd97445f6.png)
![Screenshot from 2021-01-10 10-37-06](https://user-images.githubusercontent.com/62014238/104116101-9a30d700-533b-11eb-838e-7937415c22ad.png)
![Screenshot from 2021-01-10 10-45-47](https://user-images.githubusercontent.com/62014238/104116114-c187a400-533b-11eb-870f-d0178f3a9246.png)
![Screenshot from 2021-01-10 10-37-31](https://user-images.githubusercontent.com/62014238/104116108-af0d6a80-533b-11eb-9ea1-d23ee76b4888.png)
## Want to Contribute?
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
