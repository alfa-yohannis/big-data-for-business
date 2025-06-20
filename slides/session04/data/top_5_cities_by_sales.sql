SELECT
  c.city,
  SUM(o.total) AS total_sales
FROM
  customers c
  JOIN orders o ON c.id = o.customer_id
GROUP BY
  c.city
ORDER BY
  total_sales DESC
LIMIT
  5;