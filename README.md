# DAW (Diseño de Aplicaciones Web) Event Tracker

I've decided to make this little app that shows in the terminal all the events my user has in the moodle platform.

_Requirements_

* BeautifulSoup4

## Usage
To this app to work you will have to login atleast once. Then press `F12` to enter the Inspector, go to the **Network** tab and refresh once.

Copy the cURL form the first entry and paste it here: https://curl.trillworks.com/ then copy `cookies` and `headers`

Open app.py with a text editor and replace in `line 41` with your cookies and headers. Save and execute app.py:

```
python3 app.py
```
