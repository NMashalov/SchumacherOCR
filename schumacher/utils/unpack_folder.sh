for file in *.djvu; do
    pdfname="${file%.djvu}.pdf"
    if [ ! -f  $pdfname ]; then
        ddjvu -format=pdf -quality=85 -verbose "$file"  pdfname > /dev/null
    fi
done

echo > image_folders.txt

for file in *.pdf ; do
    image_dirname="${file%.*}"
    if [ ! -d $image_dirname ]; then 
        mkdir -p $image_dirname
        gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r300 -sOutputFile="${image_dirname}/Pic%d.png" $file > /dev/null
        echo $image_dirname >> image_folders.txt
    fi
done