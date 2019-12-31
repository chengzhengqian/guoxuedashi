for file in `ls -1 ./txt`
do
    echo $file
    inputfile=./txt/$file
    outputfile=./mobi/$file.mobi
    if [ -f "$outputfile" ]; then
	echo "$outputfile exist"
    else
	ebook-convert $inputfile $outputfile
    fi

done
	    
