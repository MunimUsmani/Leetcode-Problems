DELETE p
FROM Person p
JOIN Person d
ON p.email = d.email AND p.id > d.id;
