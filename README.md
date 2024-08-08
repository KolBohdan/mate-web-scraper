# Mate Academy Web scraper
## Description
The scraper gathers the following information for each course:

- Course name
- Short description
- Course type (full-time or flex)
- Number of Modules
- Number of Topics
- Course Duration

After that scraper write information about courses to `courses.csv`

## How to run
1. You should have a driver installed for your browser.
You can find how to install driver on selenium [doc](https://selenium-python.readthedocs.io/installation.html)
in module ```1.5. Drivers```. For example, [chrome driver](https://sites.google.com/chromium.org/driver/).


2. Clone the repo:
```shell
git clone https://github.com/KolBohdan/mate-web-scraper
```
Make sure that you are in the `mate_web_craper` folder:
```shell
cd mate_web_scraper
```
3. Create venv:

For Windows users:
```shell
python -m venv venv
source venv/Scripts/activate
```
For macOS/Linux users:
```shell
python3 -m venv venv
source venv/bin/activate
```
4. Install requirements:
```shell
pip install -r requirements.txt
```
5. Run parse.py:
```bash
python app/parse.py
```
Wait a little bit for the scraper to collect all the information.
Than you will got ```courses.csv``` file