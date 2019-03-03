mkdir test 
mv foo foo_1

for i in {1..3}
do
    echo $i
done
cat foo_1
