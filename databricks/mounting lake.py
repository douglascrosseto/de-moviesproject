# Databricks notebook source
# DBTITLE 1,Mounting raw layer
dbutils.fs.mount(
    source = 'wasbs://raw@adlsmovieseastus2.blob.core.windows.net/',
    mount_point = '/mnt/raw',
    extra_configs = {'fs.azure.account.key.adlsmovieseastus2.blob.core.windows.net' : dbutils.secrets.get('adb-secret-scope', 'adlsmovieseastus2-secret-access-key')}
)

# COMMAND ----------

# DBTITLE 1,Mounting bronze layer
dbutils.fs.mount(
    source = 'wasbs://bronze@adlsmovieseastus2.blob.core.windows.net/',
    mount_point = '/mnt/bronze',
    extra_configs = {'fs.azure.account.key.adlsmovieseastus2.blob.core.windows.net' : dbutils.secrets.get('adb-secret-scope', 'adlsmovieseastus2-secret-access-key')}
)

# COMMAND ----------

# DBTITLE 1,Mounting silver layer
dbutils.fs.mount(
    source = 'wasbs://silver@adlsmovieseastus2.blob.core.windows.net/',
    mount_point = '/mnt/silver',
    extra_configs = {'fs.azure.account.key.adlsmovieseastus2.blob.core.windows.net' : dbutils.secrets.get('adb-secret-scope', 'adlsmovieseastus2-secret-access-key')}
)

# COMMAND ----------

# DBTITLE 1,Mounting gold layer
dbutils.fs.mount(
    source = 'wasbs://gold@adlsmovieseastus2.blob.core.windows.net/',
    mount_point = '/mnt/gold',
    extra_configs = {'fs.azure.account.key.adlsmovieseastus2.blob.core.windows.net' : dbutils.secrets.get('adb-secret-scope', 'adlsmovieseastus2-secret-access-key')}
)
