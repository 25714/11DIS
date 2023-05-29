DROP TABLE IF EXISTS albums;

CREATE TABLE albums (
    idAlbum VARCHAR PRIMARY KEY,
    idArtist VARCHAR,
    idLabel VARCHAR,
    strAlbum VARCHAR,
    strAlbumStripped VARCHAR,
    strArtist VARCHAR,
    strArtistStripped VARCHAR,
    intYearReleased VARCHAR,
    strStyle VARCHAR,
    strGenre VARCHAR,
    strLabel VARCHAR,
    strReleaseFormat VARCHAR,
    intSales VARCHAR,
    strAlbumThumb VARCHAR,
    strAlbumThumbHQ VARCHAR,
    strAlbumThumbBack VARCHAR,
    strAlbumCDart VARCHAR,
    strAlbumSpine VARCHAR,
    strAlbum3DCase VARCHAR,
    strAlbum3DFlat VARCHAR,
    strAlbum3DFace VARCHAR,
    strAlbum3DThumb VARCHAR,
    strDescription TEXT,
    strDescriptionDE TEXT,
    strDescriptionFR TEXT,
    strDescriptionCN TEXT,
    strDescriptionIT TEXT,
    strDescriptionJP TEXT,
    strDescriptionRU TEXT,
    strDescriptionES TEXT,
    strDescriptionPT TEXT,
    strDescriptionSE TEXT,
    strDescriptionNL TEXT,
    strDescriptionHU TEXT,
    strDescriptionNO TEXT,
    strDescriptionIL TEXT,
    strDescriptionPL TEXT,
    intLoved VARCHAR,
    intScore VARCHAR,
    intScoreVotes VARCHAR,
    strReview TEXT,
    strMood VARCHAR,
    strTheme VARCHAR,
    strSpeed VARCHAR,
    strLocation VARCHAR,
    strMusicBrainzID VARCHAR,
    strMusicBrainzArtistID VARCHAR,
    strAllMusicID VARCHAR,
    strBBCReviewID VARCHAR,
    strRateYourMusicID VARCHAR,
    strDiscogsID VARCHAR,
    strWikidataID VARCHAR,
    strWikipediaID VARCHAR,
    strGeniusID VARCHAR,
    strLyricWikiID VARCHAR,
    strMusicMozID VARCHAR,
    strItunesID VARCHAR,
    strAmazonID VARCHAR,
    strLocked VARCHAR
);
