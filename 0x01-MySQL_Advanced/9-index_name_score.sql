-- Create index on first letter of name and score in names table
CREATE INDEX idx_name_first_score
ON names (name(1), score);
