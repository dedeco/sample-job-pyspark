# Run the job (local)
```bash
poetry run spark-submit \
  --master local \
  --py-files dist/angelou-*.whl \
  jobs/sample_job.py
```


# Submit the job to Dataproc
```bash
gcloud dataproc jobs submit pyspark \
  --cluster=cluster-sample \
  --region=us-central1 \
  --py-files dist/angelou-*.whl \
  jobs/sample_job.py
```