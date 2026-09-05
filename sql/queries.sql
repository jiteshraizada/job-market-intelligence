--total companies--
SELECT count(*)
from companies;

---total jobs---
SELECT count(*) as total_jobs
from jobs;

---total skills---
SELECT count(*) as Total_Skills
from skills;

---jobs by company---
SELECT c.company_name,
count(j.job_pk) as total_jobs
from companies c join jobs j
on c.company_id = j.company_id
GROUP by company_name
ORDER by total_jobs desc;

---jobs by category---
SELECT category,
count(*) as total_jobs
from jobs
GROUP BY category
ORDER by total_jobs desc;

---jobs by level---
SELECT level,
count(*) as total_jobs
from jobs
GROUP by level
order by total_jobs DESC;

--most demanded skills---
SELECT 
s.skill_name,
count(DISTINCT js.job_pk) as job_count
from skills s 
join job_skills js
on s.skill_id = js.skill_id
group by s.skill_name
order by job_count desc;

--work mode--
select
work_mode,
count(*) as total_jobs
from jobs
group by work_mode
order by total_jobs;

--top locations--
SELECT
location,
work_mode,
count(*) as total_jobs
from jobs
where location is not NULL
group by location
order by total_jobs DESC
limit 15;

--job category as per company--
SELECT
    c.company_name,
    j.category,
    COUNT(*) AS total_jobs
FROM companies AS c
JOIN jobs AS j
    ON c.company_id = j.company_id
GROUP BY c.company_name, j.category
ORDER BY total_jobs DESC;

--companies as per data job--
SELECT
c.company_name,
count(*) as data_jobs
from companies as c
join jobs as j
on c.company_id = j.company_id
where j.category = 'Data'
group by c.company_name
order by data_jobs DESC;

--companies as per finance job--
SELECT
c.company_name,
count(*) as finance_jobs
from companies as c
join jobs as j on 
c.company_id=j.company_id
where j.category = 'Finance'
GROUP by c.company_name
order by finance_jobs DESC;

--job level as per category--
SELECT
    category,
    level,
    COUNT(*) AS total_jobs
FROM jobs
where level!= 'Unspecified'
GROUP BY category, level
ORDER BY category, total_jobs DESC;

--level and jobs--
SELECT
level,
count(*) as total_jobs
from jobs 
group by level
order by total_jobs DESC;

--companies as per intern jobs--
SELECT
c.company_name,
count(*) as intern_jobs
from companies as c join jobs as j
on c.company_id = j.company_id
where level = 'Intern'
GROUP by c.company_name
order by intern_jobs desc;

--companies as per senior jobs--
SELECT
c.company_name,
count(*) as senior_jobs
from companies as c
join jobs as j
on c.company_id = j.company_id
where level = 'Senior'
group by c.company_name
order by senior_jobs desc;

--intern jobs as per category and company--
SELECT
	c.company_name,
    j.category,
    COUNT(*) AS intern_jobs
FROM jobs as j join companies as c
on j.company_id = c.company_id
WHERE j.level = 'Intern'
GROUP BY j.category
ORDER BY intern_jobs DESC;

--skills as per data jobs--
SELECT
	s.skill_name,
	count(distinct j.job_pk) as data_jobs
from skills as s
JOIN job_skills as js
	on s.skill_id = js.skill_id
join jobs as j
	on js.job_pk = j.job_pk
where j.category = 'Data'
group by skill_name
order by data_jobs desc;

--skills as per finance jobs--
SELECT
	s.skill_name,
	count(distinct j.job_pk) as finance_jobs
from skills as s
JOIN job_skills as js
	on s.skill_id = js.skill_id
join jobs as j
	on js.job_pk = j.job_pk
where j.category = 'Finance'
group by skill_name
order by finance_jobs desc;

--skills in both Data and Finance Jobs--
SELECT
s.skill_name,
count(case when j.category = 'Data'
then j.job_pk end) as data_jobs,
count(case when j.category = 'Finance'
then j.job_pk end) as finance_jobs
from skills as s join job_skills as js
on s.skill_id= js.skill_id
join jobs as j on 
js.job_pk = j.job_pk
where j.category in ('Data','Finance')
group by s.skill_name
HAVING COUNT(DISTINCT CASE
WHEN j.category = 'Data' THEN j.job_pk
END) > 0 AND
COUNT(DISTINCT CASE 
WHEN j.category = 'Finance' 
THEN j.job_pk END) > 0
order by (data_jobs + finance_jobs) desc;

--skills req along sql--
select
s.skill_name,
count(j.job_pk) as total_jobs
from skills as s 
join job_skills as js on
s.skill_id = js.skill_id
join jobs as j on
js.job_pk = j.job_pk
where j.job_pk in(
SELECT
j2.job_pk
from job_skills as js2
join jobs as j2
on js2.job_pk = j2.job_pk
join skills as s2
on js2.skill_id = s2.skill_id
where skill_name = 'SQL'
)
and s.skill_name != 'SQL'
Group by s.skill_name
order by total_jobs desc;

--skills req along power bi--
SELECT
    s.skill_name,
    COUNT(DISTINCT js.job_pk) AS job_count
FROM skills AS s
JOIN job_skills AS js
    ON s.skill_id = js.skill_id
WHERE js.job_pk IN (
    SELECT js2.job_pk
    FROM job_skills AS js2
    JOIN skills AS s2
        ON js2.skill_id = s2.skill_id
    WHERE s2.skill_name = 'Power BI'
)
AND s.skill_name != 'Power BI'
GROUP BY s.skill_id, s.skill_name
ORDER BY job_count DESC;

--top 5 skills req by companies for data jobs--
with skill_count as (
select 
distinct c.company_name,
s.skill_name,
COUNT(DISTINCT j.job_pk) AS job_count
from skills as s join
job_skills as js on
s.skill_id = js.skill_id
join jobs as j on
js.job_pk = j.job_pk
join companies as c
on j.company_id = c.company_id
where j.category = 'Data'
GROUP BY
    c.company_name,
    s.skill_name
ORDER BY
    c.company_name,
    job_count DESC
),
ranked_skills as(
select 
company_name,
skill_name,
job_count,
row_number() OVER (
PARTITION by company_name
order by job_count DESC
) as skill_rank
from skill_count
)
SELECT
company_name,
skill_name,
job_count,
skill_rank
from ranked_skills
where skill_rank <= 5
order by company_name,skill_rank;

--top 5 skills for each job category--
with skill_count as (
SELECT
j.category,
s.skill_name,
count(j.job_pk) as job_count
from skills as s JOIN
job_skills as js on
s.skill_id = js.skill_id
JOIN jobs as j on
js.job_pk = j.job_pk
group by j.category,s.skill_name
),
skill_rank as (
SELECT
category,
skill_name,
job_count,
row_number() OVER(
PARTITION by category
order by job_count DESC) as Skill_rank
from skill_count
)
SELECT
category,
skill_name,
job_count,
Skill_rank
FROM skill_rank
where Skill_rank <=5
order by category,Skill_rank;

--category by companies--
SELECT
c.company_name,
j.category,
count(j.job_pk) as total_jobs
from jobs as j join 
companies as c on
j.company_id=c.company_id
group by c.company_name,j.category
order by c.company_name,total_jobs DESC;

--percentage of stripe jobs are engineering--
with company_categories as (
select
c.company_name,
j.category,
count(j.job_pk) as total_jobs
from jobs as j join 
companies as c 
on j.company_id=c.company_id
group by c.company_name,j.category
)
select 
company_name,
category,
total_jobs,
round(
total_jobs * 100.0/
sum(total_jobs) over (
PARTITION by company_name
),
2
) as percentage_of_company_jobs
from company_categories
order by company_name,
percentage_of_company_jobs desc;

--jobs as per category--
SELECT
    j.category,
    COUNT(DISTINCT j.company_id) AS companies_hiring,
    COUNT(*) AS total_jobs
FROM jobs AS j
GROUP BY j.category
ORDER BY companies_hiring DESC, total_jobs DESC;

--category by percentage--
SELECT
category,
count(*) as job_count,
round(count(*)*100.0/(SELECT count(*) from jobs),
2)
as percentage_of_jobs
from jobs
group by category
order by job_count desc;

--avg skills per job--
SELECT
round(avg(skill_count),2) as average_skills_per_job
from (
SELECT j.job_pk,
count(js.skill_id) as skill_count
FROM jobs AS j
LEFT JOIN job_skills AS js
ON j.job_pk = js.job_pk
GROUP BY j.job_pk);

--jobs with no skill extracted--
SELECT
    COUNT(*) AS jobs_without_skills
FROM jobs AS j
LEFT JOIN job_skills AS js
    ON j.job_pk = js.job_pk
WHERE js.job_pk IS NULL;

--top skills by job level--
with skill_count as (
select 
s.skill_name,
j.level,
count(j.job_pk) as total_jobs
from skills as s join
job_skills as js on 
js.skill_id = s.skill_id
join jobs as j on
j.job_pk = js.job_pk
where j.level != 'Unspecified'
group by j.level,s.skill_name
),
ranked_skills as (
SELECT
level,
skill_name,
total_jobs,
row_number() OVER(
partition by level
order by total_jobs DESC) as skill_rank
FROM skill_count
)
SELECT
level,
skill_name,
total_jobs,
skill_rank
from ranked_skills
where skill_rank <= 5
order by level, skill_rank;

--work mode and category--
SELECT
    j.category,
    j.work_mode,
    COUNT(*) AS total_jobs
FROM jobs AS j
where work_mode != 'Unspecified'
GROUP BY
    j.category,
    j.work_mode
ORDER BY
    j.category,
    total_jobs DESC;
	
--location and category--
SELECT
    j.location,
    j.category,
    COUNT(*) AS total_jobs
FROM jobs AS j
WHERE j.location IS NOT NULL
GROUP BY
    j.location,
    j.category
ORDER BY
    total_jobs DESC
LIMIT 30;

--companies using each skill--
SELECT
    s.skill_name,
    COUNT(DISTINCT j.company_id) AS companies_using_skill,
    COUNT(DISTINCT j.job_pk) AS total_jobs
FROM skills AS s
JOIN job_skills AS js
    ON s.skill_id = js.skill_id
JOIN jobs AS j
    ON js.job_pk = j.job_pk
GROUP BY s.skill_id, s.skill_name
HAVING COUNT(DISTINCT j.company_id) >= 7
AND COUNT(DISTINCT j.job_pk) >= 50
ORDER BY companies_using_skill DESC, total_jobs DESC;
