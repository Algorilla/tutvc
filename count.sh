# Display the name of each filename file and count of
# the number of distinct occurences of each species
# in that file
for filename in data/*.txt
do
    echo $filename
    grep -v Species $filename | cut -d , -f 2 | sort | uniq -c | sort -n -r
done
