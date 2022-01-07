SELECT
	count(0)
FROM (SELECT 
	    max(enrollment_date) enrollment_date,
		customer_id 
	  FROM dw.d_account
	  GROUP BY customer_id) sub
WHERE 
    enrollment_date BETWEEN start_enrollment_date AND end_enrollment_date;