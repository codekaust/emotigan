# create and setup utils
mkdir utils/
cd utils/

wget http://nlp.stanford.edu/data/glove.6B.zip
unzip glove.6B.zip

# create required directories
mkdir -p images/snapshot
mkdir saved_model/