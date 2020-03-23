# create and setup utils
mkdir utils/
cd utils/

wget http://nlp.stanford.edu/data/glove.6B.zip
unzip glove.6B.zip
rm glove.6B.100d.txt glove.6B.zip glove.6B.50d.txt glove.6B.200d.txt

cd ..

# create required directories
mkdir -p images/snapshot
mkdir saved_model/
mkdir -p dataset/edited
mkdir -p dataset/original
