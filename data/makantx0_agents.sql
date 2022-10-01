-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Сен 19 2022 г., 10:52
-- Версия сервера: 5.7.21-20-beget-5.7.21-20-1-log
-- Версия PHP: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `makantx0_agents`
--

-- --------------------------------------------------------

--
-- Структура таблицы `agents`
--
-- Создание: Июн 23 2022 г., 13:33
--

DROP TABLE IF EXISTS `agents`;
CREATE TABLE `agents` (
  `id` int(11) NOT NULL,
  `email` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `fio` varchar(255) DEFAULT NULL,
  `obrazovanie` text,
  `samozan` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `opit` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `resume` varchar(255) DEFAULT NULL,
  `photo` BLOB NOT NULL,
  `telegramid` int(11) DEFAULT NULL,
  `activation` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `clients`
--
-- Создание: Июн 23 2022 г., 13:40
--

DROP TABLE IF EXISTS `clients`;
CREATE TABLE `clients` (
  `id` int(11) NOT NULL,
  `inn` varchar(222) NOT NULL,
  `contacts` text NOT NULL,
  `comments` text NOT NULL,
  `contact_name` text NOT NULL,
  `agent_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `deals`
--
-- Создание: Июн 23 2022 г., 14:07
--

DROP TABLE IF EXISTS `deals`;
CREATE TABLE `deals` (
  `id` int(11) NOT NULL,
  `deals_id` int(11) NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `etap` varchar(255) NOT NULL,
  `budget` varchar(255) NOT NULL,
  `agent_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `deals_history`
--
-- Создание: Июн 23 2022 г., 14:09
--

DROP TABLE IF EXISTS `deals_history`;
CREATE TABLE `deals_history` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `agents`
--
ALTER TABLE `agents`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `deals`
--
ALTER TABLE `deals`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `deals_history`
--
ALTER TABLE `deals_history`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `agents`
--
ALTER TABLE `agents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `clients`
--
ALTER TABLE `clients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `deals`
--
ALTER TABLE `deals`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `deals_history`
--
ALTER TABLE `deals_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
