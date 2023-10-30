/*
 Navicat Premium Data Transfer

 Source Server         : eve
 Source Server Type    : MySQL
 Source Server Version : 80034 (8.0.34)
 Source Host           : localhost:3306
 Source Schema         : eve

 Target Server Type    : MySQL
 Target Server Version : 80034 (8.0.34)
 File Encoding         : 65001

 Date: 30/10/2023 09:47:58
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for me_groups
-- ----------------------------
DROP TABLE IF EXISTS `me_groups`;
CREATE TABLE `me_groups`  (
  `groupID` int NOT NULL,
  `description` varchar(1000) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`groupID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of me_groups
-- ----------------------------
INSERT INTO `me_groups` VALUES (0, 'Unknown');
INSERT INTO `me_groups` VALUES (1, 'Ship Modules, Ship Rigs, Personal Deployables, Implants, Cargo Containers');
INSERT INTO `me_groups` VALUES (2, 'Ammunition, Charges, Scripts');
INSERT INTO `me_groups` VALUES (3, 'Drones, Fighters');
INSERT INTO `me_groups` VALUES (4, 'T1 Frigates, T1 Destroyers, Shuttles');
INSERT INTO `me_groups` VALUES (5, 'T1 Cruisers, T1 Battlecruisers, Industrial Ships, Mining Barges');
INSERT INTO `me_groups` VALUES (6, 'T1 Battleships, T1 Freighters, Industrial Command Ships');
INSERT INTO `me_groups` VALUES (7, 'T2 Frigates, T2 Destroyers, T3 Destroyers');
INSERT INTO `me_groups` VALUES (8, 'T2 Cruisers, T2 Battlecruisers, T2 Haulers, Exhumers, T3 Cruisers,T3 Subsystems');
INSERT INTO `me_groups` VALUES (9, 'T2 Battleships, Jump Freighters');
INSERT INTO `me_groups` VALUES (10, 'T2 Components, Tools, Data Interfaces, T3 Components');
INSERT INTO `me_groups` VALUES (11, 'Capital Construction Components');
INSERT INTO `me_groups` VALUES (12, 'Structure Components, Structure Modules, Upwell Structures, Starbase Structures, Fuel Blocks');
INSERT INTO `me_groups` VALUES (13, 'T2 Capital Construction Components');
INSERT INTO `me_groups` VALUES (14, 'Reactions');
INSERT INTO `me_groups` VALUES (15, 'Capital Ships');

SET FOREIGN_KEY_CHECKS = 1;
