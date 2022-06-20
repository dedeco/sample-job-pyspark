# Run the job (local)
```bash
poetry run spark-submit \
  --master local \
  --py-files dist/angelou-*.whl \
  jobs/sample_job.py
```

# Submit to Dataproc

## Create Dataproc cluster
Create the cluster with [python dependencies](./scripts/initialize-cluster.sh) and submit the job

```bash
export REGION=us-central1;
gcloud dataproc clusters create cluster-sample \
--region=${REGION} \
--initialization-actions=gs://andresousa-experimental-scripts/initialize-cluster.sh
```

## Submit/Run job 
```bash
gcloud dataproc jobs submit pyspark \
  --cluster=cluster-sample \
  --region=us-central1 \
  --py-files dist/angelou-*.whl \
  jobs/sample_job.py
```