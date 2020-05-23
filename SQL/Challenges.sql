select c.hacker_id, h.name, count(c.challenge_id) as counts
from hackers as h join challenges as c on h.hacker_id = c.hacker_id
group by c.hacker_id, h.name 
having counts = (select count(ch.challenge_id) from challenges as ch group by ch.hacker_id order by count(*) desc limit 1)
or counts not in (select count(ch2.challenge_id) from challenges as ch2 group by ch2.hacker_id having ch2.hacker_id <> c.hacker_id)
order by counts desc, c.hacker_id;
