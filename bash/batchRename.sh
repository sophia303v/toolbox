i=0
for f in *.png
do  
    echo "Renameb $f" 
    mv "$f"  $i.png
    i=$((i+1)) 
done
