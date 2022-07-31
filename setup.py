# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC Estabelecendo conectividade como Data Lake no S3, conectividade via IAM

# COMMAND ----------

aws_bucket_name = "datalake-passos"
mount_name = "datalake"
dbutils.fs.mount("s3a://%s" % aws_bucket_name, "/mnt/%s" % mount_name)

# COMMAND ----------

dbutils.fs.ls("/mnt/datalake")

# COMMAND ----------

dbutils.fs.put("/mnt/datalake/teste_s3_.txt", "teste escrita databricks aws s3")

# COMMAND ----------


