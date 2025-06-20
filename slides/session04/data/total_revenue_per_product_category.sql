SELECT
  p.category,
  SUM(od.line_total) AS total_revenue
FROM
  order_details od
  JOIN products p ON p.id = od.product_id
GROUP BY
  p.category
ORDER BY
  total_revenue DESC;