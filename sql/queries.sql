-- Total Funds

SELECT COUNT(*)
FROM fund_master;

-- Funds by Fund House

SELECT
fund_house,
COUNT(*) AS total_schemes
FROM fund_master
GROUP BY fund_house
ORDER BY total_schemes DESC;

-- Average NAV

SELECT
AVG(nav) AS average_nav
FROM nav_history;

-- Highest NAV

SELECT
MAX(nav) AS highest_nav
FROM nav_history;

-- Lowest NAV

SELECT
MIN(nav) AS lowest_nav
FROM nav_history;