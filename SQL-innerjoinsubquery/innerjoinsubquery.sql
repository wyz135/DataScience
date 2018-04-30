USE DSTRAINING
GO

SELECT A.StationID, NoStart, NoEnd
FROM
(SELECT StationID, COUNT(StartStation) as NoStart
 FROM station20180429 as S LEFT JOIN journey20180429 as J
 ON S.StationID = J.StartStation
 GROUP BY StationID) as A
INNER JOIN
(SELECT StationID, COUNT(EndStation) as NoEnd
 FROM station20180429 as S LEFT JOIN journey20180429 as J
 ON S.StationID = J.EndStation
 GROUP BY StationID) as B
 ON A.StationID = B.StationID