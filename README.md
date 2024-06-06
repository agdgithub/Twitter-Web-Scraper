# Twitter Web Scraper

Twitter Web Scraper is a Selenium script that can read the Twitter home page (on your local 
computer) and fetch the top 5 trending topics under “What’s Happening” 
section from the homepage. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install 

```bash
pip install -r requirements.txt
```

Setup Chrome driver path in app.py

```python
driver_path = 'C:\\Users\\agd\\Downloads\\chromedriver-win64\\chromedriver.exe'
```

Insert your Twitter username and password
```python
39  username.send_keys("Your_username")
49  password.send_keys("Your_password")
```

MongoDB Connection
```
mongodb+srv://daberaoakshay1:6ufKPdL0R1iXg9dv@cluster0.7lpipcb.mongodb.net/
```


## Run

```bash
python main.py
```

In browser open
```bash
http://127.0.0.1:5000/
```

## Screenshots

![127 0 0 1_5000 - Personal - Microsoft​ Edge 06-06-2024 14_46_50](https://github.com/agdgithub/Twitter-Web-Scraper/assets/98071875/6a665984-d5a6-4d9a-b7c3-5c7de630ba7a)

![127 0 0 1_5000_run-script - Personal - Microsoft​ Edge 06-06-2024 14_47_45](https://github.com/agdgithub/Twitter-Web-Scraper/assets/98071875/c96eb0c8-c2fd-4e25-ac0b-4503f6e980b8)




