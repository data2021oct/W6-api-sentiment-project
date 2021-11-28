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
DROP SCHEMA IF EXISTS `friends`;
CREATE SCHEMA IF NOT EXISTS `friends` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `friends` ;

-- -----------------------------------------------------
-- Table `friends`.`characters`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friends`.`characters` (
  `idcharacters` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`idcharacters`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `friends`.`temporadas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friends`.`temporadas` (
  `idTemporadas` INT NOT NULL,
  PRIMARY KEY (`idTemporadas`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `friends`.`episodios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friends`.`episodios` (
  `idEpisodio` INT NOT NULL AUTO_INCREMENT,
  `numero` INT NULL DEFAULT NULL,
  `tituloEp` VARCHAR(65) NOT NULL,
  `idTemporadas` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idEpisodio`),
  INDEX `ep_temp_idx` (`idTemporadas` ASC) VISIBLE,
  CONSTRAINT `ep_temp`
    FOREIGN KEY (`idTemporadas`)
    REFERENCES `friends`.`temporadas` (`idTemporadas`))
ENGINE = InnoDB
AUTO_INCREMENT = 136
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
    REFERENCES `friends`.`episodios` (`idEpisodio`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `friends`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friends`.`usuario` (
  `idusuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idusuario`),
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
