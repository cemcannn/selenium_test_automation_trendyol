## Trendyol Automation

End to End test for Trendyol Shopping Site.

Prerequisites:
Clone repo to your local.

You can directly use venv in package or you can create new venv folder. 
If you want to use venv in package, you can activate it by typing in console, the path where the "activate.bat" file is located.
If you create new venv, innstall all the required libraries in requirements.txt using the pip command :

```python
pip install -r <requirement>
```

Download the current Chrome WebDriver (for Chrome) or Gecko Driver (for FireFox) from [here](https://www.selenium.dev/downloads/) and copy the path into related executable_path in \tests\conftest.py

Start the automation:
In terminal using the code below:
```python
py.test --browser-name <browsername>
```
(tests can be executed on browsers: Chrome, Firefox or IE, if you don't write any browser name, then it will start on Chrome browser.

Inside of Automation:
User login, search product in search bar, filter by name, submit product, checkout

A logfile will be created after tests are executed. Change the logfile path in fileHandler in \utilities\BaseClass.py

Test report:
A test report as report.html will be generated by running commandline:
```python
pytest --html=report.html
```

Test report will be created after tests are executed and it will include logfiles.
