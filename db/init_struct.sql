-- Création de la base
CREATE DATABASE IF NOT EXISTS InfraMusicStore;
USE InfraMusicStore;

-- Création des tables  

-- Table Artist
CREATE TABLE Artist (
    ArtistId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(120) NOT NULL
);

-- Table Album
CREATE TABLE Album (
    AlbumId INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(160) NOT NULL,
    ArtistId INT NOT NULL,
    FOREIGN KEY (ArtistId) REFERENCES Artist(ArtistId)
);

-- Table MediaType
CREATE TABLE MediaType (
    MediaTypeId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(120)
);

-- Table Track
CREATE TABLE Track (
    TrackId INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(200) NOT NULL,
    AlbumId INT,
    MediaTypeId INT,
    Genre VARCHAR(120),
    Composer VARCHAR(220),
    Milliseconds INT,
    Bytes INT,
    UnitPrice DECIMAL(10,2),
    FOREIGN KEY (AlbumId) REFERENCES Album(AlbumId),
    FOREIGN KEY (MediaTypeId) REFERENCES MediaType(MediaTypeId)
);
