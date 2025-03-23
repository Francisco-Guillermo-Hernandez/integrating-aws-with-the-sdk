

```bash
pip install -r requirements.txt
```


```bash
source_bucket=$(aws s3api list-buckets --output text --query 'Buckets[?contains(Name, `source-images`) == `true`] | [0].Name')

destination_bucket=$(aws s3api list-buckets --output text --query 'Buckets[?contains(Name, `destination-images`) == `true`] | [0].Name') ;

printf "\nSource bucket: $source_bucket\nDestination bucket: $destination_bucket\n\n"

```


```bash 
python main.py $source_bucket $destination_bucket
```