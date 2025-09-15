import pandas as pd
import sqlite3
conn = sqlite3.connect("data.sqlite")

products = pd.read_sql("""
SELECT *
  FROM products;
""", conn)
print(products)

products_ordered = pd.read_sql("""
SELECT *
  FROM products
  ORDER BY productName;
""", conn)
print(products_ordered)

products_desc = pd.read_sql("""
SELECT *
  FROM products
  ORDER BY productName DESC;
""", conn)
print(products_desc)

product_length = pd.read_sql("""
SELECT productName, length(productDescription) AS description_length
  FROM products
 ORDER BY description_length;
""", conn)
print(product_length)

product_length_2 = pd.read_sql("""
SELECT productName
  FROM products
 ORDER BY length(productDescription);
""", conn)

vendors = pd.read_sql("""
SELECT productVendor, productName, MSRP
  FROM products
 ORDER BY productVendor, productName;
""", conn)
print(vendors)

count_distinct = pd.read_sql("""
SELECT COUNT(DISTINCT productVendor) AS num_product_vendors,
       COUNT(DISTINCT productName) AS num_product_names
  FROM products;
""", conn)
print(count_distinct)

cast_integer = pd.read_sql("""
SELECT productName, quantityInStock
  FROM products
 ORDER BY CAST(quantityInStock AS INTEGER);
""", conn).head(10)
print(cast_integer)

limit_5 = pd.read_sql("""
SELECT *
  FROM orders
 LIMIT 5;
""", conn)
print(limit_5)

longest_10_comments = pd.read_sql("""
SELECT *
  FROM orders
 ORDER BY length(comments) DESC
 LIMIT 10;
""", conn)
print(longest_10_comments)

limit_and_where = pd.read_sql("""
SELECT *
  FROM orders
 WHERE status = "Cancelled"
 ORDER BY length(comments) DESC
 LIMIT 10;
""", conn)
print(limit_and_where)

using_in = pd.read_sql("""
SELECT *
  FROM orders
 WHERE status IN ("Cancelled", "Resolved")
 ORDER BY length(comments) DESC
 LIMIT 10;
""", conn)
print(using_in)

first_five = pd.read_sql("""
SELECT DISTINCT customerNumber, orderDate
  FROM orders
 ORDER BY orderDate
 LIMIT 5;
""", conn)
print(first_five)

newest_unfulfilled = pd.read_sql("""
SELECT *
  FROM orders
 WHERE shippedDate = ""
   AND status != "Cancelled"
 ORDER BY orderDate DESC
 LIMIT 10;
""", conn)
print(newest_unfulfilled)

longest_fulfillment_time = pd.read_sql("""
SELECT *,
       julianday(shippedDate) - julianday(orderDate) AS days_to_fulfill
  FROM orders
 WHERE shippedDate != ""
 ORDER BY days_to_fulfill DESC
 LIMIT 1;
""", conn)
print(longest_fulfillment_time)

conn.close()