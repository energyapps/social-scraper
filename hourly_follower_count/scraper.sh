echo 'begin. Python script should create a file called social_data_temp.csv. If the process breaks it will not be created. '
python /home/ec2-user/scrape/followers-hourly.py
echo 'python run, temp social data created (if it didnt break)'
echo
echo 'now we will rename the previous hours data as "old"'
mv /home/ec2-user/scrape/social_data.csv /home/ec2-user/scrape/social_data_old.csv
echo 'if there is a new data file called social_data_temp.csv it will be renamed social_data.csv'
mv /home/ec2-user/scrape/social_data_temp.csv /home/ec2-user/scrape/social_data.csv
echo 'initiate transfer of new file to s3 server. if no file there, will throw an error'
/home/ec2-user/bin/s3cmd put /home/ec2-user/scrape/social_data.csv s3://energy2/social/
echo 'transfered file to s3. now will check to make sure that there is a social_data.csv file for it to use next time.'
# if there was an error, there will be no social_data.csv file. This is why we keep the old file on hand. 
# If it failed we will be able to restore the previous functioning data file to iterate on next time.
if [ -f /home/ec2-user/scrape/social_data.csv ]; then
    echo "data file exists. process was a success"
else
    echo "data file does not exist. Restore previous version of data."
    mv /home/ec2-user/scrape/social_data_old.csv /home/ec2-user/scrape/social_data.csv
fi
echo 'process complete'
