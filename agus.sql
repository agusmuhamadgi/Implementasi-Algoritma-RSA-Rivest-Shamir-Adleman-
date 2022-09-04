-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Waktu pembuatan: 12 Jun 2022 pada 07.41
-- Versi server: 10.7.3-MariaDB
-- Versi PHP: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `agus`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `dekripsi`
--

CREATE TABLE `dekripsi` (
  `id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `enkripsi_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dekripsi` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `dekripsi`
--

INSERT INTO `dekripsi` (`id`, `enkripsi_id`, `dekripsi`) VALUES
('lzxPjaYmox', 'oELKLMRHXB', 'test');

-- --------------------------------------------------------

--
-- Struktur dari tabel `enkripsi`
--

CREATE TABLE `enkripsi` (
  `id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `kunci_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `enkripsi_img` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `enkripsi_text` text COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `enkripsi`
--

INSERT INTO `enkripsi` (`id`, `kunci_id`, `enkripsi_img`, `enkripsi_text`) VALUES
('oELKLMRHXB', 'LJNXWomCBR', NULL, '77 264 344 77');

-- --------------------------------------------------------

--
-- Struktur dari tabel `kunci`
--

CREATE TABLE `kunci` (
  `id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `text` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `img` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `public_key` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `private_key` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `kunci`
--

INSERT INTO `kunci` (`id`, `text`, `img`, `public_key`, `private_key`) VALUES
('LJNXWomCBR', 'test', 'test', '8063', '287');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `dekripsi`
--
ALTER TABLE `dekripsi`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `enkripsi`
--
ALTER TABLE `enkripsi`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `kunci`
--
ALTER TABLE `kunci`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
