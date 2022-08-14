# [COMPSCI235] List of New Zealand Prime Ministers

## Description

This repository is for Lab 5 COMPSCI235 at The University of Auckland, Semester 2, 2022.

The rest of the lab exercise can be found from [here](https://github.com/changx03/cs235_lab_code).

## Check solutions

To check the solutions, `checkout` the corresponding branch.

## Getting started

### For `venv`

Creating virtual environment using `venv`:

```bash
python3 -m venv venv
.\venv\Scripts\activate
# On Linux: run "source ./venv/bin/activate" instead
pip install -r requirements.txt
```

### For Anaconda

Creating virtual environment using Anaconda:

```bash
conda create --name cs235_lab5 python=3.9
conda activate cs235_lab5
conda install --file requirements.txt
```

### For PyCharm

When using PyCharm, set the virtual environment using 'File'->'Settings' and select 'Project:COMPSCI-235' from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment.

## Start server

Once the virtual environment is activated.

```bash
flask run
```

Open the page from your browser: http://localhost:8000

## Tasks

Download the list of tasks from `Assignment` -> `Lab Report 5` from the Canvas page.
