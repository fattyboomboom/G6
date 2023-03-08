-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: database
-- Generation Time: Mar 08, 2023 at 01:07 AM
-- Server version: 8.0.32
-- PHP Version: 8.1.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wolfcampus_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `acc_id` int NOT NULL,
  `user_id` int NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `creation_date` date NOT NULL,
  `last_login` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`acc_id`, `user_id`, `email`, `password`, `creation_date`, `last_login`) VALUES
(1, 2, 'mbazgan@nevada.unr.edu', '1234', '2023-03-05', '2023-03-05'),
(2, 3, 'johasdn@email.com', '12345', '2023-03-06', '2023-03-06'),
(6, 12, 'javi@noholidays.com', '1234', '2023-03-07', '2023-03-07'),
(7, 13, 'last@unr.edu', '1234', '2023-03-07', '2023-03-07'),
(8, 14, 'melaniebazgan@gmail.com', '1234', '2023-03-07', '2023-03-07'),
(9, 15, 'john@emsdfadsfsafasfail.com', '12345', '2023-03-07', '2023-03-07'),
(10, 16, 'john@asadad.com', '12345', '2023-03-07', '2023-03-07'),
(11, 17, 'john@asdasdasdasdas.com', '12345', '2023-03-07', '2023-03-07'),
(12, 18, 'john@asdasdasdasdasdasdas.com', '12345', '2023-03-07', '2023-03-07'),
(13, 19, 'sandra@sandercock.com', '1234', '2023-03-07', '2023-03-07'),
(456456, 8, 'admin@unr.edu', '1234', '2023-02-21', '2023-02-21'),
(456457, 20, 'moderator@unr.edu', '1234', '2023-03-08', '2023-03-08');

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE `answers` (
  `answer_id` int NOT NULL,
  `answer_value` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `blocked_list`
--

CREATE TABLE `blocked_list` (
  `user_id` int NOT NULL,
  `blocked_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `book_id` int NOT NULL,
  `book_isbn` varchar(50) NOT NULL,
  `book_status` int NOT NULL,
  `book_name` varchar(50) NOT NULL,
  `book_author` varchar(50) NOT NULL,
  `book_price` double NOT NULL,
  `book_class` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `book_publication`
--

CREATE TABLE `book_publication` (
  `publication_id` int NOT NULL,
  `publication_text` text NOT NULL,
  `publication_date` date NOT NULL,
  `publication_photo` blob,
  `book_id` int NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `buildings`
--

CREATE TABLE `buildings` (
  `build_id` int NOT NULL,
  `build_name` varchar(50) NOT NULL,
  `build_code` varchar(10) NOT NULL,
  `build_location` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `build_photo` blob
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `buildings`
--

INSERT INTO `buildings` (`build_id`, `build_name`, `build_code`, `build_location`, `build_photo`) VALUES
(63, 'Ansari Business Building', 'AB', 'https://www.google.com/maps?z=12&q=loc:39.5400539,-119.8147023', NULL),
(128, 'Anderson Health Science', 'AHS', 'https://www.google.com/maps?z=12&q=loc:39.549256,-119.816918', NULL),
(173, 'Agricultural Education', 'AE', 'https://www.google.com/maps/place/39%C2%B032\'16.4%22N+119%C2%B048\'25.7%22W/@39.537888,-119.8093377,17z/data=!3m1!4b1!4m4!3m3!8m2!3d39.537888!4d-119.807149', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `classes`
--

CREATE TABLE `classes` (
  `class_id` int NOT NULL,
  `class_name` varchar(50) NOT NULL,
  `begin_end_class` varchar(50) NOT NULL COMMENT 'This is gonna be the begining and end of the class',
  `class_sched` varchar(50) NOT NULL,
  `professor` varchar(50) NOT NULL,
  `requirements` varchar(50) NOT NULL,
  `section` varchar(50) NOT NULL,
  `moderator` int NOT NULL COMMENT 'this is the moderator of the class',
  `building_id` int NOT NULL,
  `room` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `classes`
--

INSERT INTO `classes` (`class_id`, `class_name`, `begin_end_class`, `class_sched`, `professor`, `requirements`, `section`, `moderator`, `building_id`, `room`) VALUES
(1, 'CH201', 'march 20 / may 20', 'MonWed 1.30-2.45', 'Angie', 'CS301, CH201', '1001', 3, 173, '207');

-- --------------------------------------------------------

--
-- Table structure for table `class_note`
--

CREATE TABLE `class_note` (
  `classnote_id` int NOT NULL,
  `classnote_text` text NOT NULL,
  `classnote_photo` blob,
  `classnote_status` tinyint NOT NULL,
  `class_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `class_note`
--

INSERT INTO `class_note` (`classnote_id`, `classnote_text`, `classnote_photo`, `classnote_status`, `class_id`) VALUES
(1, 'holaquetal', NULL, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `friend_list`
--

CREATE TABLE `friend_list` (
  `user_id` int NOT NULL,
  `friend_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `post_id` int NOT NULL,
  `post_date` date NOT NULL,
  `post_text` text NOT NULL,
  `post_photo` blob,
  `post_status` tinyint NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`post_id`, `post_date`, `post_text`, `post_photo`, `post_status`, `user_id`) VALUES
(1, '2023-03-16', 'tuvieja', NULL, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `profiles`
--

CREATE TABLE `profiles` (
  `profile_id` int NOT NULL,
  `user_id` int NOT NULL,
  `post_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `profiles`
--

INSERT INTO `profiles` (`profile_id`, `user_id`, `post_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `reports`
--

CREATE TABLE `reports` (
  `report_id` int NOT NULL,
  `report_status` tinyint NOT NULL,
  `post_id` int NOT NULL,
  `classnote_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `students_class_list`
--

CREATE TABLE `students_class_list` (
  `class_id` int NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `study_sessions`
--

CREATE TABLE `study_sessions` (
  `ss_id` int NOT NULL,
  `ss_place` varchar(50) NOT NULL,
  `ss_date` date NOT NULL,
  `ss_time` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ss_notes` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci COMMENT 'extra info about the study session',
  `build_id` int NOT NULL,
  `ss_class` int NOT NULL,
  `ss_student_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `study_sessions`
--

INSERT INTO `study_sessions` (`ss_id`, `ss_place`, `ss_date`, `ss_time`, `ss_notes`, `build_id`, `ss_class`, `ss_student_id`) VALUES
(1, 'Bob\'s burgers', '2023-03-22', '15.00', 'we are meeting in the bla bla bla', 173, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `surveys`
--

CREATE TABLE `surveys` (
  `survey_id` int NOT NULL,
  `class_id` int NOT NULL,
  `answer_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `profile_picture` blob,
  `type_id` int NOT NULL,
  `major` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `last_name`, `email`, `password`, `profile_picture`, `type_id`, `major`) VALUES
(1, 'John', 'James', 'john@email.com', '12345', NULL, 3, NULL),
(2, 'Bazgan', 'Melanie', '', '1234', NULL, 3, NULL),
(3, 'John', 'James', 'johasdn@email.com', '12345', NULL, 3, NULL),
(8, 'admin', 'admin', 'admin@unr.edu', '1234', NULL, 1, NULL),
(10, 'John', 'Jammmmmmmmmmes', 'john@i.com', '12345', NULL, 3, NULL),
(11, 'javier mariano', 'macchiavello', 'j.macchiavello@hotmail.com', '1234', NULL, 3, NULL),
(12, 'javi', '', 'javi@noholidays.com', '1234', NULL, 3, NULL),
(13, 'lastlast', 'last', 'last@unr.edu', '1234', NULL, 3, NULL),
(14, 'Melanie', 'Bazgan', 'melaniebazgan@gmail.com', '1234', NULL, 3, NULL),
(15, 'John', 'James', 'john@emsdfadsfsafasfail.com', '12345', NULL, 3, NULL),
(16, 'John', 'James', 'john@asadad.com', '12345', NULL, 3, NULL),
(17, 'Johasdasdsan', 'Jamasdsades', 'john@asdasdasdasdas.com', '12345', NULL, 3, NULL),
(18, 'Johasdasdsan', 'Jamasdsades', 'john@asdasdasdasdasdasdas.com', '12345', NULL, 3, NULL),
(19, 'Sandra nilda', 'Bazgan Sandercock', 'sandra@sandercock.com', '1234', NULL, 3, NULL),
(20, '1234', '1234', 'moderator@unr.edu', '1234', NULL, 3, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user_token`
--

CREATE TABLE `user_token` (
  `user_id` int NOT NULL,
  `token` text NOT NULL,
  `date` timestamp NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_type`
--

CREATE TABLE `user_type` (
  `type_id` int NOT NULL,
  `type` varchar(50) NOT NULL COMMENT 'type of user description'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user_type`
--

INSERT INTO `user_type` (`type_id`, `type`) VALUES
(1, 'admin'),
(2, 'mod'),
(3, 'user');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`acc_id`),
  ADD KEY `FK_account_users_user_id` (`user_id`);

--
-- Indexes for table `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`answer_id`);

--
-- Indexes for table `blocked_list`
--
ALTER TABLE `blocked_list`
  ADD PRIMARY KEY (`user_id`,`blocked_id`),
  ADD KEY `FK_blocked_list_users_blocked_id` (`blocked_id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`book_id`),
  ADD KEY `FK_book_class_class_id` (`book_class`);

--
-- Indexes for table `book_publication`
--
ALTER TABLE `book_publication`
  ADD PRIMARY KEY (`publication_id`),
  ADD KEY `FK_bookpublication_book_book_id` (`book_id`),
  ADD KEY `FK_bookpublication_user_user_id` (`user_id`);

--
-- Indexes for table `buildings`
--
ALTER TABLE `buildings`
  ADD PRIMARY KEY (`build_id`);

--
-- Indexes for table `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`class_id`),
  ADD KEY `FK_class_building_id_build_id` (`building_id`),
  ADD KEY `FK_class_user_user_id` (`moderator`);

--
-- Indexes for table `class_note`
--
ALTER TABLE `class_note`
  ADD PRIMARY KEY (`classnote_id`),
  ADD KEY `FK_class_note_class_class_id` (`class_id`);

--
-- Indexes for table `friend_list`
--
ALTER TABLE `friend_list`
  ADD PRIMARY KEY (`friend_id`,`user_id`),
  ADD KEY `FK_friend_list_users_friend_id` (`user_id`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`post_id`),
  ADD KEY `FK_posts_user_user_id` (`user_id`);

--
-- Indexes for table `profiles`
--
ALTER TABLE `profiles`
  ADD PRIMARY KEY (`profile_id`),
  ADD KEY `FK_profiles_posts_post_id` (`post_id`),
  ADD KEY `FK_profiles_users_user_id` (`user_id`);

--
-- Indexes for table `reports`
--
ALTER TABLE `reports`
  ADD PRIMARY KEY (`report_id`),
  ADD KEY `FK_reports_posts_post_id` (`post_id`),
  ADD KEY `FK_reports_class_note_class_note_id` (`classnote_id`);

--
-- Indexes for table `students_class_list`
--
ALTER TABLE `students_class_list`
  ADD PRIMARY KEY (`class_id`,`user_id`),
  ADD KEY `FK_students_class_list_user_user_id` (`user_id`);

--
-- Indexes for table `study_sessions`
--
ALTER TABLE `study_sessions`
  ADD PRIMARY KEY (`ss_id`),
  ADD KEY `FK_study_sessions_buildings_build_id` (`build_id`),
  ADD KEY `FK_study_sessions_classes_class_id` (`ss_class`),
  ADD KEY `FK_study_sessions_users_user_id` (`ss_student_id`);

--
-- Indexes for table `surveys`
--
ALTER TABLE `surveys`
  ADD PRIMARY KEY (`survey_id`),
  ADD KEY `FK_surverys_answers_answer_id` (`answer_id`),
  ADD KEY `FK_surveys_class_class_id` (`class_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `FK_users_user_type_type_id` (`type_id`);

--
-- Indexes for table `user_token`
--
ALTER TABLE `user_token`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `user_type`
--
ALTER TABLE `user_type`
  ADD PRIMARY KEY (`type_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `acc_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=456458;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `post_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `FK_account_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `FK_users_user_type_type_id` FOREIGN KEY (`type_id`) REFERENCES `user_type` (`type_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Constraints for table `user_token`
--
ALTER TABLE `user_token`
  ADD CONSTRAINT `FK_user_token_user_id_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
