-- 3. Create Recruiter Users and Profiles for each company
-- Company 1 - TechCorp Industries (2 recruiters)
INSERT INTO main_app_user (username, password, last_login, is_active, is_staff, is_superuser, first_name, last_name, email, date_joined, role) VALUES
('recruiter_john_tech', 'pbkdf2_sha256$1000000$wo2eTmXVOlW8srd7lBmFoW$gLIWElodmWZqV21T/bfXdtUqCYkpIs6zQp7I5rTCSpc=', NULL, true, false, false, 'John', 'Smith', 'john@techcorp.com', CURRENT_TIMESTAMP, 'REC'),
('recruiter_sarah_tech', 'pbkdf2_sha256$1000000$wo2eTmXVOlW8srd7lBmFoW$gLIWElodmWZqV21T/bfXdtUqCYkpIs6zQp7I5rTCSpc=', NULL, true, false, false, 'Sarah', 'Johnson', 'sarah@techcorp.com', CURRENT_TIMESTAMP, 'REC');

INSERT INTO main_app_recruiterprofile (user_id, company_id, experience) VALUES
((SELECT id FROM main_app_user WHERE username = 'recruiter_john_tech'), (SELECT id FROM main_app_company WHERE name = 'TechCorp Industries'), 8.5),
((SELECT id FROM main_app_user WHERE username = 'recruiter_sarah_tech'), (SELECT id FROM main_app_company WHERE name = 'TechCorp Industries'), 6.0);

-- Company 2 - CloudNine Solutions (3 recruiters)
INSERT INTO main_app_user (username, password, last_login, is_active, is_staff, is_superuser, first_name, last_name, email, date_joined, role) VALUES
('recruiter_mike_cloud', 'pbkdf2_sha256$1000000$wo2eTmXVOlW8srd7lBmFoW$gLIWElodmWZqV21T/bfXdtUqCYkpIs6zQp7I5rTCSpc=', NULL, true, false, false, 'Mike', 'Wilson', 'mike@cloudnine.io', CURRENT_TIMESTAMP, 'REC'),
('recruiter_emma_cloud', 'pbkdf2_sha256$1000000$wo2eTmXVOlW8srd7lBmFoW$gLIWElodmWZqV21T/bfXdtUqCYkpIs6zQp7I5rTCSpc=', NULL, true, false, false, 'Emma', 'Davis', 'emma@cloudnine.io', CURRENT_TIMESTAMP, 'REC'),
('recruiter_alex_cloud', 'pbkdf2_sha256$1000000$wo2eTmXVOlW8srd7lBmFoW$gLIWElodmWZqV21T/bfXdtUqCYkpIs6zQp7I5rTCSpc=', NULL, true, false, false, 'Alex', 'Brown', 'alex@cloudnine.io', CURRENT_TIMESTAMP, 'REC');

INSERT INTO main_app_recruiterprofile (user_id, company_id, experience) VALUES
((SELECT id FROM main_app_user WHERE username = 'recruiter_mike_cloud'), (SELECT id FROM main_app_company WHERE name = 'CloudNine Solutions'), 7.0),
((SELECT id FROM main_app_user WHERE username = 'recruiter_emma_cloud'), (SELECT id FROM main_app_company WHERE name = 'CloudNine Solutions'), 5.5),
((SELECT id FROM main_app_user WHERE username = 'recruiter_alex_cloud'), (SELECT id FROM main_app_company WHERE name = 'CloudNine Solutions'), 9.0);

-- Company 3 - DataStream Analytics (2 recruiters)
INSERT INTO main_app_user (username, password, last_login, is_active, is_staff, is_superuser, first_name, last_name, email, date_joined, role) VALUES
('recruiter_david_data', 'pbkdf2_sha256$1000000$wo2eTmXVOlW8srd7lBmFoW$gLIWElodmWZqV21T/bfXdtUqCYkpIs6zQp7I5rTCSpc=', NULL, true, false, false, 'David', 'Martinez', 'david@datastream.io', CURRENT_TIMESTAMP, 'REC'),
('recruiter_lisa_data', 'pbkdf2_sha256$1000000$wo2eTmXVOlW8srd7lBmFoW$gLIWElodmWZqV21T/bfXdtUqCYkpIs6zQp7I5rTCSpc=', NULL, true, false, false, 'Lisa', 'Anderson', 'lisa@datastream.io', CURRENT_TIMESTAMP, 'REC');

INSERT INTO main_app_recruiterprofile (user_id, company_id, experience) VALUES
((SELECT id FROM main_app_user WHERE username = 'recruiter_david_data'), (SELECT id FROM main_app_company WHERE name = 'DataStream Analytics'), 10.0),
((SELECT id FROM main_app_user WHERE username = 'recruiter_lisa_data'), (SELECT id FROM main_app_company WHERE name = 'DataStream Analytics'), 4.5);

-- Company 4 - WebFlow Digital (2 recruiters)
INSERT INTO main_app_user (username, password, last_login, is_active, is_staff, is_superuser, first_name, last_name, email, date_joined, role) VALUES
('recruiter_tom_web', 'pbkdf2_sha256$1000000$wo2eTmXVOlW8srd7lBmFoW$gLIWElodmWZqV21T/bfXdtUqCYkpIs6zQp7I5rTCSpc=', NULL, true, false, false, 'Tom', 'Taylor', 'tom@webflow.com', CURRENT_TIMESTAMP, 'REC'),
('recruiter_rachel_web', 'pbkdf2_sha256$1000000$wo2eTmXVOlW8srd7lBmFoW$gLIWElodmWZqV21T/bfXdtUqCYkpIs6zQp7I5rTCSpc=', NULL, true, false, false, 'Rachel', 'Thomas', 'rachel@webflow.com', CURRENT_TIMESTAMP, 'REC');

INSERT INTO main_app_recruiterprofile (user_id, company_id, experience) VALUES
((SELECT id FROM main_app_user WHERE username = 'recruiter_tom_web'), (SELECT id FROM main_app_company WHERE name = 'WebFlow Digital'), 6.5),
((SELECT id FROM main_app_user WHERE username = 'recruiter_rachel_web'), (SELECT id FROM main_app_company WHERE name = 'WebFlow Digital'), 5.0);

-- Company 5 - AI Innovations Inc (3 recruiters)
INSERT INTO main_app_user (username, password, last_login, is_active, is_staff, is_superuser, first_name, last_name, email, date_joined, role) VALUES
('recruiter_chris_ai', 'pbkdf2_sha256$1000000$wo2eTmXVOlW8srd7lBmFoW$gLIWElodmWZqV21T/bfXdtUqCYkpIs6zQp7I5rTCSpc=', NULL, true, false, false, 'Chris', 'Garcia', 'chris@aiinnovations.com', CURRENT_TIMESTAMP, 'REC'),
('recruiter_laura_ai', 'pbkdf2_sha256$1000000$wo2eTmXVOlW8srd7lBmFoW$gLIWElodmWZqV21T/bfXdtUqCYkpIs6zQp7I5rTCSpc=', NULL, true, false, false, 'Laura', 'Rodriguez', 'laura@aiinnovations.com', CURRENT_TIMESTAMP, 'REC'),
('recruiter_kevin_ai', 'pbkdf2_sha256$1000000$wo2eTmXVOlW8srd7lBmFoW$gLIWElodmWZqV21T/bfXdtUqCYkpIs6zQp7I5rTCSpc=', NULL, true, false, false, 'Kevin', 'Lee', 'kevin@aiinnovations.com', CURRENT_TIMESTAMP, 'REC');

INSERT INTO main_app_recruiterprofile (user_id, company_id, experience) VALUES
((SELECT id FROM main_app_user WHERE username = 'recruiter_chris_ai'), (SELECT id FROM main_app_company WHERE name = 'AI Innovations Inc'), 11.0),
((SELECT id FROM main_app_user WHERE username = 'recruiter_laura_ai'), (SELECT id FROM main_app_company WHERE name = 'AI Innovations Inc'), 7.5),
((SELECT id FROM main_app_user WHERE username = 'recruiter_kevin_ai'), (SELECT id FROM main_app_company WHERE name = 'AI Innovations Inc'), 6.0);
