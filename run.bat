@echo off

if not exist "data" (
    echo Creating data folder
    mkdir data
)

cd data

if exist "mushroom.test" (
    echo Found data/mushroom.test
) else (
    echo Downloading mushroom.test in data folder
    curl -o mushroom.test https://raw.githubusercontent.com/Aashay-Thakur/Data-Mining/main/data/mushroom.test    
)

if exist "mushroom.train" (
    echo Found data/mushroom.train
) else (
    echo Downloading mushroom.train in data folder
    curl -o mushroom.training https://raw.githubusercontent.com/Aashay-Thakur/Data-Mining/main/data/mushroom.training   
)

cd ..

if exist "requirements.txt" (
    echo Found requirements.txt
) else (
    echo Downloading requirements.txt
    curl -o requirements.txt https://raw.githubusercontent.com/Aashay-Thakur/Data-Mining/main/requirements.txt    
)

if exist "naive_bayes.py" (
    echo Found naive_bayes.py
) else (
    echo Downloading naive_bayes.py
    curl -o naive_bayes.py https://raw.githubusercontent.com/Aashay-Thakur/Data-Mining/main/naive_bayes.py    
)

if errorlevel 1 (
    echo An error occurred during the download
) else (
    echo Download complete
)

echo Initializing virtual environment
python -m venv venv
call venv/Scripts/activate
pip install -r requirements.txt

if errorlevel 1 (
    echo An error occurred during the installation
    pause
    exit /b 1
) else (
    echo Installation complete
)

echo Running the program
python naive_bayes.py
echo.
echo Deactivating virtual environment
call deactivate
echo.
echo Now that the files have been downloaded and the virtual environment has been set up, you can run the program by executing the following commands:
echo.
echo venv\Scripts\activate
echo python naive_bayes.py
echo.
echo You can deactivate the virtual environment by executing the following command:
echo.
echo deactivate
echo.
pause