hotelData = LOAD '/user/data.txt' as (name:chararray, star:int, rooms:int, country:chararray, reviews:int, rating:int);
dataFormatted = FOREACH hotelData GENERATE name, star, rating;
dataFiltered = FILTER dataFormatted BY rating==5;
result = GROUP dataFiltered BY (name, star);
resultFormatted = FOREACH result GENERATE group as name;
dump resultFormatted;