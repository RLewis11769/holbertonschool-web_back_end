-- Create trigger that decreases quantity of item after adding new order
-- Meaning after adding to orders table, decrease from items table
CREATE TRIGGER trigger_name
AFTER INSERT
ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
