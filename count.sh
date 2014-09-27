# Display the name of each data file and count of
# the number of distict occurences of each species
# in that file
date
for filename in data/*.txt
do
    echo $filename
    grep -v Species $filename | cut -d , -f 2 | sort | uniq -c | sort -n
done
