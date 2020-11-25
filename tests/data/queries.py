MIN_TIME_QUERY = '''SELECT project.name AS PROJECT, test.name AS TEST, (end_time-start_time) as MIN_WORKING_TIME
FROM test
LEFT JOIN project
ON project.id = test.project_id
GROUP BY test.name
HAVING MIN(end_time - start_time)
ORDER BY project.name, test.name
'''

PROJECT_TEST_COUNT_QUERY = '''SELECT project.name AS PROJECT, COUNT(DISTINCT test.id) AS TESTS_COUNT
FROM test
LEFT JOIN project
ON project.id = test.project_id
GROUP BY project.name
HAVING COUNT(DISTINCT test.id)'''

PROJECTS_BY_DATE_QUERY = '''SELECT project.name AS PROJECT, test.name AS TEST, test.start_time AS DATE
FROM test
JOIN project
ON project.id = test.project_id
WHERE CAST(start_time AS DATE ) > '2015-11-07' 
ORDER BY project.name, test.name'''

BROWSER_TEST_COUNT_QUERY = '''(SELECT COUNT(test.id) AS BROWSERS
FROM test
WHERE browser = 'chrome'
GROUP BY browser
HAVING COUNT(test.id))
UNION 
(SELECT COUNT(test.id) AS BROWSERS
FROM test
WHERE browser = 'firefox'
GROUP BY browser
HAVING COUNT(test.id))'''
