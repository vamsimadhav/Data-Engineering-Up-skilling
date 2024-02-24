__Chapter 3 Exercises__
1) Retrieve the actor ID, first name, and last name for all actors. Sort by last name and then by first name.   
```
select actor_id, first_name, last_name
from actor_info
order by last_name, first_name;
```
2) Retrieve the actor ID, first name, and last name for all actors whose last name equals 'WILLIAMS' or 'DAVIS'.
```
select actor_id, first_name, last_name
from actor_info
where last_name = 'WILLIAMS' or last_name = 'DAVIS';
```
3) Write a query against the rental table that returns the IDs of the customers who rented a film on July 5, 2005 (use the rental.rental_date column,
   and you can use the date() function to ignore the time component). Include a single row for each distinct customer ID.
   ```
   
   ```

4) Fill in the blanks (denoted by <#>) for this multitable query to achieve the following results:
```
select c.email, r.return_date 
from customer c 
inner join rental r
on c.customer_id = r.customer_id 
where date(r.rental_date) = '2005-06-14' 
order by r.return_date,c.email;
```
