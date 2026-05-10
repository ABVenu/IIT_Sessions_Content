| Topic / Sub-topic | Status | Remarks |
| --- | --- | --- |
| Aggregation – GROUP BY with aggregate functions (COUNT, SUM, AVG) | Covered | Instructor reviewed COUNT, SUM, AVG with demos; extended to MIN/MAX; explained COUNT(*) vs COUNT(column) for NULL handling and COUNT(1); collapsing rows into summaries; multiple aggregates and aliases in SELECT. |
| Group filtering – HAVING with grouped results | Covered | HAVING as filter after GROUP BY; contrast with WHERE on aggregates; examples filtering grouped averages (e.g., average amount thresholds); recap tied to quiz on WHERE vs HAVING with averages. |
| Joining tables – INNER JOIN and LEFT JOIN concepts | Covered | INNER JOIN and LEFT JOIN syntax, ON conditions, table aliases; matching vs non-matching rows; example where inner drops a customer with no orders vs left join retains; brief mention of right join in quiz discussion. |
| Multi-table queries – combining information across tables | Covered | Chaining joins across several tables; student/scores/modules-style walkthrough; integrated case studies combining join with GROUP BY/HAVING/ORDER BY. |
| Pandas vs SQL – mapping groupby and merge to SQL operations | Covered | Parallels drawn between SQL GROUP BY aggregations and pandas groupby; merge linked to SQL JOIN; left-join parallel noted toward end of session. |
| *(Extra)* Primary key and foreign key relationships | Covered | Substantial setup before first join: how tables relate via keys for multi-table queries. |
| *(Extra)* Logical order of SQL clauses (FROM/JOIN, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT) | Covered | Explicit teaching that JOIN builds the working table before filtering and grouping; reinforced in complex case-study queries. |
