select sum(c.Population)
from City as c join Country as d on c.CountryCode = d.Code
where d.continent = "Asia";
