# ref-seek
## About
API to get metadata about related to a Reference Sequence using MD5 checksum id.

## Downloading the client
You can download and use this client code on your local computer in two ways. 
1. Clone this repository on your local machine using git CLI
```bash
$ git clone https://github.com/ajay-p-sharma/ref-seek.git
```
2. Download the client code using the link https://github.com/ajay-p-sharma/ref-seek/archive/master.zip

## Installation
The client is written using python3.8. It will work best with python3.8 or higher. After you have downloaded the client code from github, do the follwing

```bash
$ cd <cloned project directory>
```
#### Create virtual environment using python3
```bash
$ python3 -m venv env
```
#### Activate virtual environment
```bash
$ source env/bin/activate
```
#### Install project dependencies
```bash
$ cat requirements.txt | xargs -n 1 pip install
```
## To run the client locally
```bash
$ python main.py
```
To test go to url http://localhost:5000/. You should see a HTML page with some information.
For instructions on how to use the client go to http://localhost:5000/api/

## Running tests
To run tests use following command:
```bash
$ python -m unittest tests.GetRefTests
```


