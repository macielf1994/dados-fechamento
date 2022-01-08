SELECT
	count(0) as new_registereds
FROM (SELECT 
	    max(enrollment_date) enrollment_date,
		customer_id 
	  FROM dw.d_account
	  GROUP BY customer_id
	  ) sub
WHERE 
    enrollment_date BETWEEN start_date_to_replace AND end_date_to_replace;