-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 09-Fev-2018 às 11:43
-- Versão do servidor: 10.1.21-MariaDB
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `leagueoflegends`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `champs`
--

CREATE TABLE `champs` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `url` varchar(50) NOT NULL,
  `uid` int(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `champs`
--

INSERT INTO `champs` (`id`, `name`, `url`, `uid`) VALUES
(1, 'MonkeyKing', 'MonkeyKing_vxuea2', 62),
(2, 'Jax', 'Jax_uvpgkq', 24),
(3, 'Fiddlesticks', 'Fiddlesticks_jb8isc', 9),
(4, 'Shaco', 'Shaco_cmw8bi', 35),
(5, 'Warwick', 'Warwick_pmrx0x', 19),
(6, 'Xayah', 'Xayah_wjn3ve', 498),
(7, 'Nidalee', 'Nidalee_onjloi', 76),
(8, 'Zyra', 'Zyra_rhatdv', 143),
(9, 'Kled', 'Kled_iwalhi', 240),
(10, 'Brand', 'Brand_ladogh', 63),
(11, 'Rammus', 'Rammus_iahegv', 33),
(12, 'Illaoi', 'Illaoi_bhvo0a', 420),
(13, 'Corki', 'Corki_a8gjdm', 42),
(14, 'Braum', 'Braum_fn5u2s', 201),
(15, 'Darius', 'Darius_sgadhh', 122),
(16, 'Tryndamere', 'Tryndamere_f163dt', 23),
(17, 'MissFortune', 'MissFortune_o7n6az', 21),
(18, 'Yorick', 'Yorick_cyfuan', 83),
(19, 'Xerath', 'Xerath_iky0dg', 101),
(20, 'Sivir', 'Sivir_fib6pk', 15),
(21, 'Riven', 'Riven_k5uhr6', 92),
(22, 'Orianna', 'Orianna_wb9fr0', 61),
(23, 'Gangplank', 'Gangplank_mu92at', 41),
(24, 'Malphite', 'Malphite_opbb29', 54),
(25, 'Poppy', 'Poppy_apyzn3', 78),
(26, 'Karthus', 'Karthus_ti1grw', 30),
(27, 'Jayce', 'Jayce_efliq5', 126),
(28, 'Nunu', 'Nunu_iyzaqy', 20),
(29, 'Trundle', 'Trundle_unlfru', 48),
(30, 'Graves', 'Graves_y3nbr6', 104),
(31, 'Zoe', 'Zoe_ebcvnx', 142),
(32, 'Gnar', 'Gnar_x4pchb', 150),
(33, 'Lux', 'Lux_pgtgbi', 99),
(34, 'Shyvana', 'Shyvana_ae38l6', 102),
(35, 'Renekton', 'Renekton_ct3fdv', 58),
(36, 'Fiora', 'Fiora_mm5wzj', 114),
(37, 'Jinx', 'Jinx_gfpoju', 222),
(38, 'Kalista', 'Kalista_vsvon0', 429),
(39, 'Fizz', 'Fizz_y6w3ly', 105),
(40, 'Kassadin', 'Kassadin_z31nwe', 38),
(41, 'Sona', 'Sona_wscawa', 37),
(42, 'Irelia', 'Irelia_g95etq', 39),
(43, 'Viktor', 'Viktor_zcmlct', 112),
(44, 'Rakan', 'Rakan_yggftl', 497),
(45, 'Kindred', 'Kindred_iwfh9p', 203),
(46, 'Cassiopeia', 'Cassiopeia_m03xgf', 69),
(47, 'Maokai', 'Maokai_fgqz2s', 57),
(48, 'Ornn', 'Ornn_jfxv6t', 516),
(49, 'Thresh', 'Thresh_eowzxf', 412),
(50, 'Kayle', 'Kayle_ite8x6', 10),
(51, 'Hecarim', 'Hecarim_nxa7k6', 120),
(52, 'Khazix', 'Khazix_ornb6c', 121),
(53, 'Olaf', 'Olaf_gb1q6m', 2),
(54, 'Ziggs', 'Ziggs_hs36zc', 115),
(55, 'Syndra', 'Syndra_e5x0dw', 134),
(56, 'DrMundo', 'DrMundo_f2i6ws', 36),
(57, 'Karma', 'Karma_vabogg', 43),
(58, 'Annie', 'Annie_vxmi7u', 1),
(59, 'Akali', 'Akali_ctsv58', 84),
(60, 'Volibear', 'Volibear_zrzz2t', 106),
(61, 'Yasuo', 'Yasuo_fwddlb', 157),
(62, 'Kennen', 'Kennen_tjo71v', 85),
(63, 'Rengar', 'Rengar_pvtzrd', 107),
(64, 'Ryze', 'Ryze_u8qvmi', 13),
(65, 'Shen', 'Shen_oz3nur', 98),
(66, 'Zac', 'Zac_sktndb', 154),
(67, 'Talon', 'Talon_jhv1ip', 91),
(68, 'Swain', 'Swain_gsgrf8', 50),
(69, 'Bard', 'Bard_dvkodr', 432),
(70, 'Sion', 'Sion_euybyi', 14),
(71, 'Vayne', 'Vayne_citiq9', 67),
(72, 'Nasus', 'Nasus_d8lu6z', 75),
(73, 'Kayn', 'Kayn_yvi1ng', 141),
(74, 'TwistedFate', 'TwistedFate_cebtep', 4),
(75, 'Chogath', 'Chogath_fpaid6', 31),
(76, 'Udyr', 'Udyr_zvln3g', 77),
(77, 'Lucian', 'Lucian_o8ymah', 236),
(78, 'Ivern', 'Ivern_rmgp3v', 427),
(79, 'Leona', 'Leona_vtnfcf', 89),
(80, 'Caitlyn', 'Caitlyn_enbgus', 51),
(81, 'Sejuani', 'Sejuani_wgkwz4', 113),
(82, 'Nocturne', 'Nocturne_pmvgif', 56),
(83, 'Zilean', 'Zilean_xrvrzh', 26),
(84, 'Azir', 'Azir_irtk6u', 268),
(85, 'Rumble', 'Rumble_qz65ab', 68),
(86, 'Morgana', 'Morgana_i3dlxw', 25),
(87, 'Taliyah', 'Taliyah_tmbggc', 163),
(88, 'Teemo', 'Teemo_r6iodt', 17),
(89, 'Urgot', 'Urgot_bilkav', 6),
(90, 'Amumu', 'Amumu_euqkbi', 32),
(91, 'Galio', 'Galio_zssmmw', 3),
(92, 'Heimerdinger', 'Heimerdinger_pctrrj', 74),
(93, 'Anivia', 'Anivia_zcbjor', 34),
(94, 'Ashe', 'Ashe_ca5ls0', 22),
(95, 'Velkoz', 'Velkoz_cqmp2m', 161),
(96, 'Singed', 'Singed_qmbcjf', 27),
(97, 'Skarner', 'Skarner_x8alx1', 72),
(98, 'Varus', 'Varus_ixtiwy', 110),
(99, 'Twitch', 'Twitch_do2vya', 29),
(100, 'Garen', 'Garen_kgejh8', 86),
(101, 'Blitzcrank', 'Blitzcrank_wtp21f', 53),
(102, 'MasterYi', 'MasterYi_xbwndn', 11),
(103, 'Elise', 'Elise_fwfnw3', 60),
(104, 'Alistar', 'Alistar_ndw3sn', 12),
(105, 'Katarina', 'Katarina_u0kdky', 55),
(106, 'Ekko', 'Ekko_aefzsk', 245),
(107, 'Mordekaiser', 'Mordekaiser_nv0kci', 82),
(108, 'Lulu', 'Lulu_hdqisp', 117),
(109, 'Camille', 'Camille_zeu1xi', 164),
(110, 'Aatrox', 'Aatrox_sjjmj0', 266),
(111, 'Draven', 'Draven_fpcqq3', 119),
(112, 'TahmKench', 'TahmKench_tfuuoe', 223),
(113, 'Pantheon', 'Pantheon_y9ccpv', 80),
(114, 'XinZhao', 'XinZhao_fon5la', 5),
(115, 'AurelionSol', 'AurelionSol_wqi3wt', 136),
(116, 'LeeSin', 'LeeSin_knukr5', 64),
(117, 'Taric', 'Taric_lh7crm', 44),
(118, 'Malzahar', 'Malzahar_baspfj', 90),
(119, 'Lissandra', 'Lissandra_gaeehw', 127),
(120, 'Diana', 'Diana_jhvafx', 131),
(121, 'Tristana', 'Tristana_q3a4p1', 18),
(122, 'RekSai', 'RekSai_fe1wdo', 421),
(123, 'Vladimir', 'Vladimir_jc1kpf', 8),
(124, 'JarvanIV', 'JarvanIV_zt9yjw', 59),
(125, 'Nami', 'Nami_jz2e7c', 267),
(126, 'Jhin', 'Jhin_z7voxd', 202),
(127, 'Soraka', 'Soraka_fofe4o', 16),
(128, 'Veigar', 'Veigar_ttbsrx', 45),
(129, 'Janna', 'Janna_e9qtxt', 40),
(130, 'Nautilus', 'Nautilus_huhugq', 111),
(131, 'Evelynn', 'Evelynn_noivi3', 28),
(132, 'Gragas', 'Gragas_ciptaz', 79),
(133, 'Zed', 'Zed_r2zriz', 238),
(134, 'Vi', 'Vi_km3pjd', 254),
(135, 'KogMaw', 'KogMaw_eayglp', 96),
(136, 'Ahri', 'Ahri_j3avlb', 103),
(137, 'Quinn', 'Quinn_pf6oa5', 133),
(138, 'Leblanc', 'Leblanc_h0ysgr', 7),
(139, 'Ezreal', 'Ezreal_ejzzsi', 81);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `champs`
--
ALTER TABLE `champs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `champs`
--
ALTER TABLE `champs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=140;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
