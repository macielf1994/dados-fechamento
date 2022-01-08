DROP TABLE IF EXISTS stg.t_base_usuarios_device_fechamento_month_to_replace_date_to_replace_version_to_replace;
CREATE TABLE stg.t_base_usuarios_device_fechamento_month_to_replace_date_to_replace_version_to_replace AS
SELECT
	b.device_category, 
	b.device_model,
	c.product_category, 
	d.dbm_gender as gender,
    CASE
	    WHEN d.age <= 0 OR d.age IS NULL THEN 'N/D'
	    WHEN d.age BETWEEN 1 AND 18 THEN 'Ate 18 anos'
	    WHEN d.age BETWEEN 19 AND 24 THEN 'De 19 a 24'
	    WHEN d.age BETWEEN 25 AND 34 THEN 'De 25 a 34'
	    WHEN d.age BETWEEN 35 AND 44 THEN 'De 35 a 44'
	    WHEN d.age BETWEEN 45 AND 54 THEN 'De 45 a 54'
	    WHEN d.age BETWEEN 55 AND 64 THEN 'De 55 a 64'
	    WHEN d.age > 64 THEN '65 +'
    END AS "age",
    count(DISTINCT a.customer_id) AS unique_customers,
	sum(device_total) AS devices_total
FROM stg.t_customer_events_fechamento_month_to_replace_device_date_to_replace_version_to_replace a 
INNER JOIN dw.ft_events_device b 
	ON (a.customer_id = b.customer_id) AND (b.mmid = a.mmid)
INNER JOIN dw.d_preferential_card c 
	ON a.customer_id = c.customer_id
INNER JOIN dw.d_customer d 
	ON a.customer_id = d.customer_id 
GROUP BY 
    b.device_category, 
    b.device_model, 
    c.product_category, 
    d.dbm_gender,
    CASE
	    WHEN d.age <= 0 OR d.age IS NULL THEN 'N/D'
	    WHEN d.age BETWEEN 1 AND 18 THEN 'Ate 18 anos'
	    WHEN d.age BETWEEN 19 AND 24 THEN 'De 19 a 24'
	    WHEN d.age BETWEEN 25 AND 34 THEN 'De 25 a 34'
	    WHEN d.age BETWEEN 35 AND 44 THEN 'De 35 a 44'
	    WHEN d.age BETWEEN 45 AND 54 THEN 'De 45 a 54'
	    WHEN d.age BETWEEN 55 AND 64 THEN 'De 55 a 64'
	    WHEN d.age > 64 THEN '65 +'
    END;