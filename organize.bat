@echo off
echo Moving files to organized structure...

if exist train.py move train.py src\train.py
if exist infer.py move infer.py src\infer.py
if exist embedding.py move embedding.py src\embedding.py
if exist utils.py move utils.py src\utils.py
if exist models.py move models.py models\models.py
if exist prepare_data.py move prepare_data.py scripts\prepare_data.py
if exist IMg.ipynb move IMg.ipynb notebooks\IMg.ipynb
if exist loaddata.ipynb move loaddata.ipynb notebooks\loaddata.ipynb

echo.
echo File organization complete!
echo.
