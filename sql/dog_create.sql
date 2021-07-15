DROP TABLE IF EXISTS "dogs";

CREATE TABLE "dogs"
(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "description" TEXT,
    "character" TEXT,
    "color" TEXT,
    "male_weight" INTEGER,
    "female_weight" INTEGER,
    "male_height" INTEGER,
    "female_height" INTEGER,
    "health" TEXT
);
