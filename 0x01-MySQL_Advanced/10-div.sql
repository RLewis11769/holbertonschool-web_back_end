-- Create function that divides and returns first number by second number
-- Returns 0 if second number is 0
DELIMITER $$

CREATE FUNCTION SafeDiv(
	a INT,
	b INT)
RETURNS FLOAT
BEGIN
	IF b = 0 THEN
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END $$
