-- Create view that lists students who have score under 80%
-- Student must have no last_meeting or more than a month since last meeting
CREATE VIEW need_meeting AS
SELECT students.name
FROM students
WHERE
	students.score < 80 AND
	last_meeting IS NULL OR
	DATEDIFF(NOW(), last_meeting) > 30
