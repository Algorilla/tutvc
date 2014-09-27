# Display the name of each data file and count of
# the number of distict occurences of each species
# in that file
for filename in data/*.txt
do
    date
    echo $filename
    grep -v Species $filename | cut -d , -f 2 | sort | uniq -c | sort -n -r
done
