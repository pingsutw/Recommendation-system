# Recommendation-system
### Download criteo dataset
```bash
./download_criteo.sh
```
### Transform csv data to libsvm
```bash
python3 preprocess.py --input_dir=./data/ --output_dir=./data/ --cutoff=200
```
