# TinyTuya-Cleaner

> This Python script was created in a [Jupyter Notebook](https://jupyter.org/) (`.ipynb`)

## Description

The exports available from [TinyTuya](https://github.com/jasonacox/tinytuya) are very large and extensive.
However, you usually don't need that much information to add them to [HomeAssistant](https://www.home-assistant.io/), for example.
Since you only need the name of the device, the device id, the local key and the Mac, this simple Python script filters out this information.

The devices are also sorted alphabetically by name.
For Mac addresses, all lowercase letters are replaced with uppercase letters.

## Get the `devices.json` from TinyTuya

First create a Python environment. For example with [Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-python).

```ba
conda create --name tinytuya_env python=3.10
```

```bash
conda activate tinytuya_env
```

Install TinyTuya:

```bash
python -m pip install tinytuya
```

Find a list of [Tuya](https://iot.tuya.com/) devices in the local network:

```bash
python -m tinytuya scan
```

A device id from this list is required for the next step.

Get local keys and more:

```bash
python -m tinytuya wizard
```

## Run

> This Python script must be executed in the same folder in which the TinyTuya exports are located!

In order for the Python script to run correctly under **Linux**, the [Pandas library must be installed](https://pandas.pydata.org/docs/getting_started/install.html#installing-from-pypi) beforehand:

```Shell
pip install pandas
```

> Additional packages may need to be installed. Confirm this with `y`. The `json` library may also need to be installed.

You can then execute the Python script as follows:

```Shell
python3 TinyTuyaCleaner.py
```

A file named `tuya-devices.json` was created.
