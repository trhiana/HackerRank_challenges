select Country.continent, floor(avg(City.population))
from City join Country on City.CountryCode = Country.Code 
group by Country.continent;
