from pyspark.sql import SparkSession

def initialize_spark(app_name="Task2_Avg_Tenure_Left_vs_Stayed"):
    spark = SparkSession.builder.appName(app_name).getOrCreate()
    return spark

def load_data(spark, emp_file_path, dept_file_path):
    employees_df = spark.read.csv(emp_file_path, header=True, inferSchema=True)
    departments_df = spark.read.csv(dept_file_path, header=True, inferSchema=True)
    return employees_df, departments_df

def calculate_avg_tenure(df):
    # TODO: Implement logic to calculate average tenure for employees who left vs. stayed
    pass

def write_output(result_df, output_path):
    result_df.coalesce(1).write.csv(output_path, header=True, mode='overwrite')

def main():
    spark = initialize_spark()
    emp_file = "path/to/employees.csv"
    dept_file = "path/to/departments.csv"
    output_file = "path/to/output.csv"
    
    employees_df, departments_df = load_data(spark, emp_file, dept_file)
    result_df = calculate_avg_tenure(employees_df)
    
    write_output(result_df, output_file)
    spark.stop()

if __name__ == "__main__":
    main()
