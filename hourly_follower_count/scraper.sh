#!/bin/bash -ex
SOCIAL_DATA_PATH=/var/www/energy.gov/htdocs/sites/prod/files/api/social

if [ ! -d "$SOCIAL_DATA_PATH" ]; then
  mkdir $SOCIAL_DATA_PATH
fi

echo 'begin. Python script should create a file called social_data_temp.csv. If the process breaks it will not be created. '
python followers-hourly.py
echo 'python run, temp social data created (if it didnt break)'
echo

echo 'now we will rename the previous hours data as "old"'
mv social_data.csv social_data_old.csv

echo 'if there is a new data file called social_data_temp.csv it will be renamed social_data.csv'
mv social_data_temp.csv social_data.csv
cp -f social_data.csv $SOCIAL_DATA_PATH/social_data.csv

# if there was an error, there will be no social_data.csv file. This is why we keep the old file on hand. 
# If it failed we will be able to restore the previous functioning data file to iterate on next time.
if [ -f social_data.csv ]; then
    echo "data file exists. process was a success"
else
    echo "data file does not exist. Restore previous version of data."
    mv social_data_old.csv social_data.csv
fi
echo 'process complete'
