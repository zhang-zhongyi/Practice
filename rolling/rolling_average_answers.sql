-- Name: Zhongyi (Troy) Zhang
WITH 
daily AS (
  SELECT 
  	  DATE(transaction_time) AS transaction_date,
      SUM(transaction_amount) AS daily_amount
  FROM transactions
  WHERE DATE(transaction_time) BETWEEN '2021-01-01' AND '2021-01-31'
  GROUP BY 1 
),
rolling AS (
  SELECT 
      transaction_date,
      AVG(daily_amount) OVER (ORDER BY transaction_date
      ROWS BETWEEN 2 PRECEDING AND CURRENT ROW )
      AS rolling_average
  FROM daily
)
SELECT 
	*
FROM rolling
WHERE transaction_date = '2021-01-31'