# Naive Bayes Classifier

This is a simple implementation of the Naive Bayes Classifier in Python. The program uses the [**"mushroom.training"**](https://drive.google.com/file/d/1P0iabGWF6E5yvkgMg4mbMfN4LbL-Y5Yh/view?usp=classroom_web&authuser=0) and [**"mushroom.test"**](https://drive.google.com/file/d/1aUyHcK5T4-h6OX9xJzy8xCbTGfzX3Vbw/view?usp=classroom_web&authuser=0) datasets to train and test the model.

## Installation

### Using Git (Recommended)

```bash
# Clone the repository
git clone https://github.com/Aashay-Thakur/Data-Mining.git
```

**OR**

> You can download the `run.bat` file from this [location](https://github.com/Aashay-Thakur/Data-Mining/blob/main/run.bat)
> Keep the file in a separate folder and run it.
> The program will be downloaded and install all the requirements automatically and run the program.
>
> **Note:** This method is only available for Windows users.
>
> -   Make sure you have Python installed on your system.
> -   Also make sure that venv is woking on your system.
>
> If the above instructions don't work, you can follow the manual installation below.

## Manual Installation

Use the datasets [**"mushroom.training"**](https://drive.google.com/file/d/1P0iabGWF6E5yvkgMg4mbMfN4LbL-Y5Yh/view?usp=classroom_web&authuser=0) and [**"mushroom.test"**](https://drive.google.com/file/d/1aUyHcK5T4-h6OX9xJzy8xCbTGfzX3Vbw/view?usp=classroom_web&authuser=0) as is.

> Make sure you haven't edited the whitespace between the columns (This could break the program)
> If you have, copy the whitespace from somewhere else in the file as is, and replace the one you edited.

Place the datasets into a folder **"/data"** in the same directory as the python file.

Also download the **requirements.txt** file from the [repository](https://github.com/Aashay-Thakur/Data-Mining/blob/main/requirements.txt) and place it in the same directory as the python file.

Your filestructure will be somthing like this.

```
current directory
│   readme.md
|   naive_bayes.py
|   requirements.txt
└─── data
    │   mushroom.test
    │   mushroom.training
```

Follow the instructions below to run the program. Once data is in place, run the following command in the terminal.

```powershell
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
call venv/bin/activate  # for cmd
venv/bin/activate       # for powershell

# Install the required packages
pip install -r requirements.txt

# Run the program
python naive_bayes.py

# Deactivate the virtual environment # Optional
deactivate
```

> Creating a virtual environment is optional, but it is recommended to avoid conflicts with other packages.
> If you are not using a virtual environment, you can skip the first two steps.

> **Note:** You don't have to create a virtual environment everytime you run the program.
>
> Skip the first two steps if you have already created a virtual environment.

Ensure that the files are converted into their respactive **".csv"** formats.
Make sure there are no repeating commas.
And you should get the output Accuracy and Standard Deviation of the model after choosing which dataset to run.
