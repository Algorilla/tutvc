# Display the name of each data file and count of
# the number of distict occurences of each species
# in that file
for f in data/*.txt
do
    date
    echo $f
    grep -v Species $f | cut -d , -f 2 | sort | uniq -c | sort -n -r
done
