CREATE OR REPLACE PROCEDURE public.add_jakoryhma(
	IN seurue integer,
	IN ryhman_nimi character varying)
LANGUAGE 'sql'
AS $BODY$
INSERT INTO public.jakoryhma(seurue_id,ryhman_nimi) VALUES (seurue, ryhman_nimi);
$BODY$;
ALTER PROCEDURE public.add_jakoryhma(integer, character varying)
    OWNER TO postgres;