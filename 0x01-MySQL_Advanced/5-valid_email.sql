-- Create trigger that changes valid_email to 0 when email changed
-- Need to include multiple ; so change final delimiter to $$
DELIMITER $$

CREATE TRIGGER email_update
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END $$

DELIMITER ;
