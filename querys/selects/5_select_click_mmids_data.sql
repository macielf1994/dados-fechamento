-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

SELECT
    fel.mmid,
    dmnm.master_name,
    fel.link_content,
    count(DISTINCT fel.customer_id) AS unique_clicks,
    sum(fel.link_total) AS total_clicks
FROM
    dw.ft_events_link fel
INNER JOIN dw.d_master_name_map dmnm 
    ON fel.mmid = dmnm.mmid
WHERE dmnm.sent_date BETWEEN start_date_to_replace AND end_date_to_replace
    AND fel.mmid IN (
    mmid_list_to_replace
        )
GROUP BY 
    fel.mmid, 
    dmnm.master_name, 
    dmnm.sent_date, 
    fel.link_content, 
    fel.dbm_link_name;