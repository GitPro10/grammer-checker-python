# grammer-checker


>To work in certain countries we have to replace one line with below code after installing gingerit because sometimes gingerit fails to fetch the correction because of Cloudflare antibot which blocks gingerit's request, so we have to bypass it.

### Install GingerIt
>Run the following command in terminal/command line

```console
pip install gingerit
```
For Linux
```console
pip3 install gingerit
```

### Bypass Cloudflare AntiBot
>In gingerit.py at `line no. 16`
#### Replace

```python
session = requests.Session()
```
#### With

```python
import cloudscraper
session = cloudscraper.create_scraper()
```

#### After that
>Run the following command in terminal/command line

```console
pip install cloudscraper
```
For Linux
```console
pip3 install cloudscraper
```
#### Where is `gingerit.py` file?
>Run the following command in terminal/command line

```console
pip show gingerit
```
For Linux
```console
pip3 show gingerit
```
>Then check the `Location`. Copy the `Location` value and go to that directory. There you will find a folder named `gingerit`, go to that directory. You will find `gingerit.py` there.





