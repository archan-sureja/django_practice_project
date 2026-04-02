-- 7. Create Applications (randomly distribute applicants to jobs)
-- Each applicant applies to 2-3 jobs with different statuses

INSERT INTO main_app_application (job_id, applicant_id, cover_letter, status, applied_at) VALUES
-- James (applicant_james_1)
((SELECT id FROM main_app_job WHERE title = 'Senior Python Developer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_james_1'), 'resumes/james_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Django Backend Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_james_1'), 'resumes/james_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '5 days'),
-- Mary (applicant_mary_2)
((SELECT id FROM main_app_job WHERE title = 'Senior Cloud Architect' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_mary_2'), 'resumes/mary_1_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '3 days'),
((SELECT id FROM main_app_job WHERE title = 'Full Stack Python Developer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_mary_2'), 'resumes/mary_2_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Cloud Solutions Architect' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_mary_2'), 'resumes/mary_3_cover.pdf', 'REJECTED', CURRENT_DATE - INTERVAL '10 days'),
-- Robert (applicant_robert_3)
((SELECT id FROM main_app_job WHERE title = 'Python REST API Developer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_robert_3'), 'resumes/robert_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'DevOps Engineer (Python)' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_robert_3'), 'resumes/robert_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '7 days'),
-- Jessica (applicant_jessica_4)
((SELECT id FROM main_app_job WHERE title = 'DevOps Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_jessica_4'), 'resumes/jessica_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Cloud Infrastructure Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_jessica_4'), 'resumes/jessica_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '6 days'),
((SELECT id FROM main_app_job WHERE title = 'Site Reliability Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_jessica_4'), 'resumes/jessica_3_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '4 days'),
-- Michael (applicant_michael_5)
((SELECT id FROM main_app_job WHERE title = 'Django Developer (Junior)' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_michael_5'), 'resumes/michael_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Python Data Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_michael_5'), 'resumes/michael_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '8 days'),
-- Jennifer (applicant_jennifer_6)
((SELECT id FROM main_app_job WHERE title = 'Database Administrator (PostgreSQL)' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_jennifer_6'), 'resumes/jennifer_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Python Automation Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_jennifer_6'), 'resumes/jennifer_2_cover.pdf', 'REJECTED', CURRENT_DATE - INTERVAL '12 days'),
-- Daniel (applicant_daniel_7)
((SELECT id FROM main_app_job WHERE title = 'Senior Software Architect' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_daniel_7'), 'resumes/daniel_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Technical Lead' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_daniel_7'), 'resumes/daniel_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '9 days'),
((SELECT id FROM main_app_job WHERE title = 'Solutions Architect' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_daniel_7'), 'resumes/daniel_3_cover.pdf', 'PENDING', CURRENT_DATE),
-- Elizabeth (applicant_elizabeth_8)
((SELECT id FROM main_app_job WHERE title = 'Python Software Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_elizabeth_8'), 'resumes/elizabeth_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Senior Backend Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_elizabeth_8'), 'resumes/elizabeth_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '2 days'),
-- William (applicant_william_9)
((SELECT id FROM main_app_job WHERE title = 'Staff Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_william_9'), 'resumes/william_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Engineering Manager' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_william_9'), 'resumes/william_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '11 days'),
((SELECT id FROM main_app_job WHERE title = 'Research Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_william_9'), 'resumes/william_3_cover.pdf', 'REJECTED', CURRENT_DATE - INTERVAL '15 days'),
-- Susan (applicant_susan_10)
((SELECT id FROM main_app_job WHERE title = 'AWS Solutions Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_susan_10'), 'resumes/susan_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Cloud Security Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_susan_10'), 'resumes/susan_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '5 days'),
-- Richard (applicant_richard_11)
((SELECT id FROM main_app_job WHERE title = 'Platform Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_richard_11'), 'resumes/richard_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Systems Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_richard_11'), 'resumes/richard_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '7 days'),
((SELECT id FROM main_app_job WHERE title = 'Security Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_richard_11'), 'resumes/richard_3_cover.pdf', 'PENDING', CURRENT_DATE),
-- Patricia (applicant_patricia_12)
((SELECT id FROM main_app_job WHERE title = 'Kubernetes Specialist' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_patricia_12'), 'resumes/patricia_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Infrastructure as Code Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_patricia_12'), 'resumes/patricia_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '6 days'),
-- Charles (applicant_charles_13)
((SELECT id FROM main_app_job WHERE title = 'Cloud Network Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_charles_13'), 'resumes/charles_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Cloud Operations Manager' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_charles_13'), 'resumes/charles_2_cover.pdf', 'REJECTED', CURRENT_DATE - INTERVAL '8 days'),
-- Barbara (applicant_barbara_14)
((SELECT id FROM main_app_job WHERE title = 'Senior Cloud Architect' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_barbara_14'), 'resumes/barbara_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Cloud Migration Specialist' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_barbara_14'), 'resumes/barbara_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '9 days'),
-- Joseph (applicant_joseph_15)
((SELECT id FROM main_app_job WHERE title = 'Hybrid Cloud Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_joseph_15'), 'resumes/joseph_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Container Orchestration Specialist' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_joseph_15'), 'resumes/joseph_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '3 days'),
((SELECT id FROM main_app_job WHERE title = 'Cloud Performance Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_joseph_15'), 'resumes/joseph_3_cover.pdf', 'PENDING', CURRENT_DATE),
-- Carol (applicant_carol_16)
((SELECT id FROM main_app_job WHERE title = 'Database Architect' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_carol_16'), 'resumes/carol_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Cloud Cost Optimizer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_carol_16'), 'resumes/carol_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '10 days'),
-- Thomas (applicant_thomas_17)
((SELECT id FROM main_app_job WHERE title = 'Disaster Recovery Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_thomas_17'), 'resumes/thomas_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Cloud API Developer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_thomas_17'), 'resumes/thomas_2_cover.pdf', 'REJECTED', CURRENT_DATE - INTERVAL '13 days'),
((SELECT id FROM main_app_job WHERE title = 'Cloud Integration Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_thomas_17'), 'resumes/thomas_3_cover.pdf', 'PENDING', CURRENT_DATE),
-- Sandra (applicant_sandra_18)
((SELECT id FROM main_app_job WHERE title = 'Enterprise Cloud Architect' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_sandra_18'), 'resumes/sandra_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Principal Cloud Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_sandra_18'), 'resumes/sandra_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '4 days'),
-- Matthew (applicant_matthew_19)
((SELECT id FROM main_app_job WHERE title = 'Multi-Cloud Architect' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_matthew_19'), 'resumes/matthew_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Cloud Platform Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_matthew_19'), 'resumes/matthew_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '6 days'),
-- Margaret (applicant_margaret_20)
((SELECT id FROM main_app_job WHERE title = 'Senior Data Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_margaret_20'), 'resumes/margaret_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Data Analyst' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_margaret_20'), 'resumes/margaret_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '8 days'),
-- Andrew (applicant_andrew_21)
((SELECT id FROM main_app_job WHERE title = 'Data Scientist' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_andrew_21'), 'resumes/andrew_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'ETL Developer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_andrew_21'), 'resumes/andrew_2_cover.pdf', 'REJECTED', CURRENT_DATE - INTERVAL '11 days'),
-- Ashley (applicant_ashley_22)
((SELECT id FROM main_app_job WHERE title = 'Analytics Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_ashley_22'), 'resumes/ashley_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Big Data Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_ashley_22'), 'resumes/ashley_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '5 days'),
((SELECT id FROM main_app_job WHERE title = 'Data Warehouse Architect' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_ashley_22'), 'resumes/ashley_3_cover.pdf', 'PENDING', CURRENT_DATE),
-- Joshua (applicant_joshua_23)
((SELECT id FROM main_app_job WHERE title = 'Machine Learning Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_joshua_23'), 'resumes/joshua_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Data Quality Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_joshua_23'), 'resumes/joshua_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '7 days'),
-- Cynthia (applicant_cynthia_24)
((SELECT id FROM main_app_job WHERE title = 'Real-time Data Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_cynthia_24'), 'resumes/cynthia_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Principal Data Scientist' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_cynthia_24'), 'resumes/cynthia_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '9 days'),
-- Kenneth (applicant_kenneth_25)
((SELECT id FROM main_app_job WHERE title = 'Data Platform Engineer' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_kenneth_25'), 'resumes/kenneth_1_cover.pdf', 'PENDING', CURRENT_DATE),
((SELECT id FROM main_app_job WHERE title = 'Business Analyst' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_kenneth_25'), 'resumes/kenneth_2_cover.pdf', 'REVIEWED', CURRENT_DATE - INTERVAL '6 days'),
((SELECT id FROM main_app_job WHERE title = 'Data Visualization Specialist' LIMIT 1), (SELECT id FROM main_app_user WHERE username = 'applicant_kenneth_25'), 'resumes/kenneth_3_cover.pdf', 'REJECTED', CURRENT_DATE - INTERVAL '14 days');