USE InfraMusicStore;

-- ------------------------------
-- Table Artist (20 entrées)
-- ------------------------------
INSERT INTO Artist (Name) VALUES
('The Beatles'),
('Adele'),
('Daft Punk'),
('Coldplay'),
('Imagine Dragons'),
('Ed Sheeran'),
('Taylor Swift'),
('Queen'),
('Linkin Park'),
('Bruno Mars'),
('Maroon 5'),
('Kanye West'),
('Beyonce'),
('The Weeknd'),
('Rihanna'),
('Drake'),
('Billie Eilish'),
('Post Malone'),
('Ariana Grande'),
('Shawn Mendes');

-- ------------------------------
-- Table Album (20 entrées)
-- ------------------------------
INSERT INTO Album (Title, ArtistId) VALUES
('Abbey Road', 1),
('25', 2),
('Discovery', 3),
('Parachutes', 4),
('Night Visions', 5),
('Divide', 6),
('1989', 7),
('A Night at the Opera', 8),
('Hybrid Theory', 9),
('Doo-Wops & Hooligans', 10),
('V', 11),
('Graduation', 12),
('Lemonade', 13),
('After Hours', 14),
('ANTI', 15),
('Scorpion', 16),
('When We All Fall Asleep', 17),
('Hollywoods Bleeding', 18),
('Positions', 19),
('Illuminate', 20);

-- ------------------------------
-- Table MediaType (20 entrées)
-- ------------------------------
INSERT INTO MediaType (Name) VALUES
('MP3'),
('WAV'),
('FLAC'),
('AAC'),
('OGG'),
('AIFF'),
('ALAC'),
('WMA'),
('DSD'),
('M4A'),
('PCM'),
('Opus'),
('AMR'),
('AC3'),
('MP2'),
('MP1'),
('APE'),
('MID'),
('RMI'),
('CAF');

-- ------------------------------
-- Table Track (20 entrées)
-- ------------------------------
INSERT INTO Track (Name, AlbumId, MediaTypeId, Genre, Composer, Milliseconds, Bytes, UnitPrice) VALUES
('Come Together', 1, 1, 'Rock', 'Lennon/McCartney', 259000, 4200000, 0.99),
('Something', 1, 2, 'Rock', 'Harrison', 182000, 3000000, 0.99),
('Hello', 2, 3, 'Pop', 'Adele Adkins', 295000, 5000000, 1.29),
('Send My Love', 2, 1, 'Pop', 'Adele Adkins', 210000, 3500000, 0.99),
('One More Time', 3, 1, 'Electronic', 'Daft Punk', 320000, 4500000, 0.99),
('Aerodynamic', 3, 4, 'Electronic', 'Daft Punk', 220000, 3000000, 0.99),
('Yellow', 4, 5, 'Alternative', 'Coldplay', 260000, 4300000, 0.99),
('Fix You', 4, 2, 'Alternative', 'Coldplay', 295000, 4800000, 1.29),
('Radioactive', 5, 1, 'Rock', 'Imagine Dragons', 210000, 4000000, 0.99),
('Demons', 5, 3, 'Rock', 'Imagine Dragons', 200000, 3900000, 0.99),
('Shape of You', 6, 4, 'Pop', 'Ed Sheeran', 240000, 4100000, 1.29),
('Perfect', 6, 1, 'Pop', 'Ed Sheeran', 265000, 4300000, 1.29),
('Blank Space', 7, 5, 'Pop', 'Taylor Swift', 230000, 4000000, 0.99),
('Shake It Off', 7, 2, 'Pop', 'Taylor Swift', 210000, 3800000, 0.99),
('Bohemian Rhapsody', 8, 1, 'Rock', 'Freddie Mercury', 355000, 5000000, 1.29),
('In The End', 9, 3, 'Rock', 'Linkin Park', 216000, 4000000, 0.99),
('Grenade', 10, 2, 'Pop', 'Bruno Mars', 220000, 4100000, 0.99),
('Sugar', 11, 1, 'Pop', 'Maroon 5', 235000, 4300000, 0.99),
('Stronger', 12, 4, 'Hip-Hop', 'Kanye West', 312000, 4800000, 1.29),
('Crazy in Love', 13, 3, 'R&B', 'Beyonce', 235000, 4200000, 0.99);
