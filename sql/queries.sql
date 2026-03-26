-- StreamWatch: OTT Analytics Queries
-- Database: streamwatch_db

-- 1. Total shows per platform
SELECT platform, COUNT(*) AS total_shows
FROM ott_titles
GROUP BY platform;

-- 2. Movies vs Series breakdown
SELECT platform, type, COUNT(*) AS count,
       ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(PARTITION BY platform), 1) AS percentage
FROM ott_titles
GROUP BY platform, type;

-- 3. Top 5 genres per platform
SELECT platform, genre, COUNT(*) AS title_count
FROM ott_titles
GROUP BY platform, genre
ORDER BY title_count DESC
LIMIT 5;

-- 4. Yearly release trend
SELECT platform, release_year, COUNT(*) AS releases
FROM ott_titles
WHERE release_year >= 2015
GROUP BY platform, release_year
ORDER BY release_year;
