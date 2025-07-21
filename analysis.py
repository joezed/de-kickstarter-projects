# Databricks notebook source
# MAGIC %md
# MAGIC # Kickstarter Projects Analysis  
# MAGIC
# MAGIC In here, all analysis will take place, as well as explanations.

# COMMAND ----------

# Import required libraries for analysis

import pandas as pd
import matplotlib as plt
import seaborn as sb
import sklearn

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1 - Data Loading and Inspection  
# MAGIC
# MAGIC To start with, it's important to first check the table, get information on each column and see it's breakdown and to get an idea of the depth of the data we have to work with.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMPORARY VIEW kickstarter_projects
# MAGIC USING csv
# MAGIC OPTIONS (
# MAGIC   path = "dbfs:/data/kickstarter_projects.csv",
# MAGIC   header = "true",
# MAGIC   inferSchema = "true"
# MAGIC );
# MAGIC
# MAGIC SELECT * FROM kickstarter_projects LIMIT 10;

# COMMAND ----------


