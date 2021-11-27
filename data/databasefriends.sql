-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema friends
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema friends
-- -----------------------------------------------------
DROP SCHEMA IF exists `friends`;
CREATE SCHEMA IF NOT EXISTS `friends` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `friends` ;

-- -----------------------------------------------------
-- Table `friends`.`Temporadas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friends`.`Temporadas` (
  `idTemporadas` INT NOT NULL,
  PRIMARY KEY (`idTemporadas`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `friends`.`Episodios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friends`.`Episodios` (
  `idEpisodio` INT NOT NULL AUTO_INCREMENT,
  `number` INT NULL,
  `tituloEp` VARCHAR(65) NOT NULL,
  `idTemporadas` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idEpisodio`),
  INDEX `ep_temp_idx` (`idTemporadas` ASC) VISIBLE,
  CONSTRAINT `ep_temp`
    FOREIGN KEY (`idTemporadas`)
    REFERENCES `friends`.`Temporadas` (`idTemporadas`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `friends`.`characters`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friends`.`characters` (
  `idcharacters` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`idcharacters`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `friends`.`quotes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friends`.`quotes` (
  `idquotes` INT NOT NULL AUTO_INCREMENT,
  `texto` TEXT NOT NULL,
  `idEpisodio` INT NULL DEFAULT NULL,
  `idcharacters` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idquotes`),
  INDEX `quoteep_idx` (`idEpisodio` ASC) VISIBLE,
  INDEX `quotechar_idx` (`idcharacters` ASC) VISIBLE,
  CONSTRAINT `quotechar`
    FOREIGN KEY (`idcharacters`)
    REFERENCES `friends`.`characters` (`idcharacters`),
  CONSTRAINT `quoteep`
    FOREIGN KEY (`idEpisodio`)
    REFERENCES `friends`.`Episodios` (`idEpisodio`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

