
use db_nexquality;
INSERT INTO `Nexquality_metriccategory` (`id`,`name`) VALUE (14, 'Complexity');
INSERT INTO `Nexquality_metriccategory` (`id`,`name`) VALUE (13, 'Coverage');
INSERT INTO `Nexquality_metriccategory` (`id`,`name`) VALUE (15, 'Duplication');
INSERT INTO `Nexquality_metricfield` (`id`,`name`,`unit`,`category_id`,`show_color`,`show_plus_sign`,`tolerance`,`reverse_tolerance`,`show_average`,`show_sum`) VALUES (1,'Line Of Code','lines',13,0,1,0,0,1,1);
INSERT INTO `Nexquality_metricfield` (`id`,`name`,`unit`,`category_id`,`show_color`,`show_plus_sign`,`tolerance`,`reverse_tolerance`,`show_average`,`show_sum`) VALUES (2,'Number Of Tests','tests',13,1,1,1,0,1,1);
INSERT INTO `Nexquality_metricfield` (`id`,`name`,`unit`,`category_id`,`show_color`,`show_plus_sign`,`tolerance`,`reverse_tolerance`,`show_average`,`show_sum`) VALUES (3,'Number Of Failing Tests','tests',13,1,1,0,1,1,1);
INSERT INTO `Nexquality_metricfield` (`id`,`name`,`unit`,`category_id`,`show_color`,`show_plus_sign`,`tolerance`,`reverse_tolerance`,`show_average`,`show_sum`) VALUES (4,'Number Of Ignored Tests','tests',13,1,1,0,1,1,1);
INSERT INTO `Nexquality_metricfield` (`id`,`name`,`unit`,`category_id`,`show_color`,`show_plus_sign`,`tolerance`,`reverse_tolerance`,`show_average`,`show_sum`) VALUES (5,'Code Coverage','%',13,1,0,50,0,1,0);
INSERT INTO `Nexquality_metricfield` (`id`,`name`,`unit`,`category_id`,`show_color`,`show_plus_sign`,`tolerance`,`reverse_tolerance`,`show_average`,`show_sum`) VALUES (6,'Complexity','cycles',14,1,0,3,1,1,0);
INSERT INTO `Nexquality_metricfield` (`id`,`name`,`unit`,`category_id`,`show_color`,`show_plus_sign`,`tolerance`,`reverse_tolerance`,`show_average`,`show_sum`) VALUES (7,'Average By Class','cycles/class',14,1,1,0,1,1,0);
INSERT INTO `Nexquality_metricfield` (`id`,`name`,`unit`,`category_id`,`show_color`,`show_plus_sign`,`tolerance`,`reverse_tolerance`,`show_average`,`show_sum`) VALUES (8,'Average By Method','cycles/method',14,1,0,3,1,1,0);
INSERT INTO `Nexquality_metricfield` (`id`,`name`,`unit`,`category_id`,`show_color`,`show_plus_sign`,`tolerance`,`reverse_tolerance`,`show_average`,`show_sum`) VALUES (9,'Duplicated Blocks','blocks',15,1,1,0,1,1,1);
INSERT INTO `Nexquality_metricfield` (`id`,`name`,`unit`,`category_id`,`show_color`,`show_plus_sign`,`tolerance`,`reverse_tolerance`,`show_average`,`show_sum`) VALUES (10,'Duplicated Lines','lines',15,1,1,0,1,1,1);
INSERT INTO `Nexquality_metricfield` (`id`,`name`,`unit`,`category_id`,`show_color`,`show_plus_sign`,`tolerance`,`reverse_tolerance`,`show_average`,`show_sum`) VALUES (11,'Duplicated Lines Density','',15,1,0,3.5,1,1,0);
INSERT INTO `Nexquality_profiletype` (`id`,`name`) VALUES (1,'Employee');
INSERT INTO `Nexquality_profiletype` (`id`,`name`) VALUES (2,'Admin');
INSERT INTO `Nexquality_profiletype` (`id`,`name`) VALUES (3,'Senior developer');
INSERT INTO `Nexquality_profiletype` (`id`,`name`) VALUES (4,'Software engineer');
INSERT INTO `Nexquality_projectuserrole` (`id`, `name`) VALUES (1, 'Developer');
INSERT INTO `auth_user` (`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) VALUES (1,'pbkdf2_sha256$15000$SHXDkL1d2KCe$GLIBqxgAGq40TdZ+1zIQO5QTfCC8L0I3ec09shE8I8Q=','2015-04-18 12:22:48',1,'admin','','','123@123.com',1,1,'2015-04-18 12:22:28');
INSERT INTO `db_nexquality`.`Nexquality_profile` (`rank`, `profiletype_id`, `user_id`) VALUES ('1', '1', '1');
INSERT INTO `db_nexquality`.`Nexquality_badgecategory` (`name`) VALUES ('General');
INSERT INTO `db_nexquality`.`Nexquality_badgecategory` (`name`) VALUES ('Metrics');
INSERT INTO `Nexquality_badge` (`id`,`name`,`description`,`conditions`,`image`,`score`,`category_id`, `given_once`) VALUES (1,'Labatt 50','Over 50% code coverage','{\"all\": [\"AVG_METRIC Code_Coverage > 40\"]}','images/badges/badge3_8JwDknM.png',25,2, 1);
INSERT INTO `Nexquality_badge` (`id`,`name`,`description`,`conditions`,`image`,`score`,`category_id`, `given_once`) VALUES (2,'Employee of the month','You were elected employee of the month','{\"all\": [\"UNCONDITIONAL\"]}','images/badges/badge3_N0JJEAb.png',50,1);
INSERT INTO `Nexquality_badge` (`id`,`name`,`description`,`conditions`,`image`,`score`,`category_id`, `given_once`) VALUES (3,'Hard coder','Over 1000 lines of code','{\"all\": [\"SUM_METRIC Line_Of_Code > 1000\"]}','images/badges/badge1_iBLyKNU.png',10,2, 1);

