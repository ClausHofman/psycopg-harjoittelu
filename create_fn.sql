-- function to get a member from jasen table by jasen id
CREATE FUNCTION public.get_member(
	id integer)

-- define type of result set -> jasen table's structure
RETURNS SETOF public.jasen

-- set language to standard sql
LANGUAGE SQL
AS $$ -- $$ is start of code block (BEGIN)
SELECT * FROM public.jasen WHERE jasen_id = id;
$$; -- $$ is end of the block (END)