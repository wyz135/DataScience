Problem: Given two tables, stations.csv and journey.csv, one that list stations, and the other that logs journeys respectively,
write a SQL query that returns a table that list each station, along with the total number of journey started and ended.

The solution is to ultilize an inner join of subquery, which each uses a left join on the station id with the start and end stations.
