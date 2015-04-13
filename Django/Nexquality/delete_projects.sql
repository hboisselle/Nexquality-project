use db_nexquality;
DELETE FROM Nexquality_metric;
DELETE FROM nexquality_commit_issues;
DELETE FROM Nexquality_issue;
DELETE FROM Nexquality_metric;
DELETE FROM Nexquality_issuelevel;
DELETE FROM Nexquality_violation;
DELETE FROM nexquality_projectuser;
DELETE FROM Nexquality_commit;
DELETE FROM nexquality_project;


##DO NOT EXEXECUTE BLINDLY
DELETE FROM Nexquality_metricfield;
DELETE FROM Nexquality_metriccategory;