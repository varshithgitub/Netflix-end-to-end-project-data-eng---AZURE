# Databricks notebook source
# MAGIC %md
# MAGIC ### Array parameter 

# COMMAND ----------

files = [
            {
                'sourcefolder' : 'netflix_directors',
                'targetfolder' : 'netflix_directors'

            },
            
            {
                
                'sourcefolder' : 'netflix_cast',
                'targetfolder' : 'netflix_cast'

            },

            {
                'sourcefolder' : 'netflix_countries',
                'targetfolder' : 'netflix_countries'

            },

            {
                'sourcefolder' : 'netflix_category',
                'targetfolder' : 'netflix_category'

            }

]

# COMMAND ----------

# MAGIC %md
# MAGIC ### Job utility to return the array 

# COMMAND ----------

dbutils.jobs.taskValues.set(key="myarray", value=files)