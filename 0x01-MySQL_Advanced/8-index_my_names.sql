-- Create index on first letter of name in names table
CREATE INDEX idx_name_first
ON names (name(1));
