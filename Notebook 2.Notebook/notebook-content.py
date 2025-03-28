# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "f0517a22-d1b5-4100-8265-02028efa07ad",
# META       "default_lakehouse_name": "Lakehouse_DirectLake",
# META       "default_lakehouse_workspace_id": "786e362b-a2cd-4b4a-9376-657fe192db64",
# META       "known_lakehouses": [
# META         {
# META           "id": "f0517a22-d1b5-4100-8265-02028efa07ad"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Azure storage access info
blob_account_name = "azureopendatastorage"
blob_container_name = "holidaydatacontainer"
blob_relative_path = "Processed"
blob_sas_token = r""

# Allow SPARK to read from Blob remotely
wasbs_path = 'wasbs://%s@%s.blob.core.windows.net/%s' % (blob_container_name, blob_account_name, blob_relative_path)
spark.conf.set(
  'fs.azure.sas.%s.%s.blob.core.windows.net' % (blob_container_name, blob_account_name),
  blob_sas_token)
print('Remote blob path: ' + wasbs_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Read Parquet file into a DataFrame.
df = spark.read.parquet(wasbs_path)
print(df.printSchema())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Save as delta table 
spark.conf.set("spark.sql.parquet.vorder.enabled", "true")
df.write.format("delta").saveAsTable("holidays")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
