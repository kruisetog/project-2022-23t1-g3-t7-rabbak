CREATE DATABASE cs301_scis_bank;
USE cs301_scis_bank;

CREATE TABLE `decorator` (
	`Decorator_ID` int,
    `Is_Foreign` bool,
    `Is_Online` bool,
    CONSTRAINT `decorator_pk` PRIMARY KEY (`Decorator_ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `user` (
	`User_ID` varchar(50),
    `Points_Total` double,
	`Miles_Total` double,
    `Cashback_Total` double,
	CONSTRAINT `user_pk` PRIMARY KEY (`User_ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `merchant` (
	`Merchant_ID` int,
    `Name` varchar(100),
	`MCC` int,
	CONSTRAINT `merchant_pk` PRIMARY KEY (`Merchant_ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `card` (
	`Card_ID` varchar(50),
    `Name` varchar(100),
	CONSTRAINT `card_pk` PRIMARY KEY (`Card_ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `user_to_card` (
	`Card_ID` varchar(50),
    `User_ID` varchar(50),
    `Card_Pan` varchar(50),
	CONSTRAINT `user_to_card_pk` PRIMARY KEY (`Card_ID`, `User_ID`),
	CONSTRAINT `user_to_card_fk1` FOREIGN KEY (`Card_ID`) REFERENCES card(`Card_ID`),
    CONSTRAINT `user_to_card_fk2` FOREIGN KEY (`User_ID`) REFERENCES user(`User_ID`) ON DELETE CASCADE  
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `transaction` (
	`Transaction_ID` varchar(40),
    `Card_ID` varchar(50),
    `User_ID` varchar(50),
    `Merchant_ID` int,
	`Amount` double,
    `Currency` varchar(10),
    `Transaction_Date` datetime,
	`Is_Online_Spend` bool,
	CONSTRAINT `transaction_pk` PRIMARY KEY (`Transaction_ID`),
	CONSTRAINT `transaction_fk1` FOREIGN KEY (`Card_ID`, `User_ID`) REFERENCES user_to_card(`Card_ID`, `User_ID`) ON DELETE CASCADE,
    CONSTRAINT `transaction_fk2` FOREIGN KEY (`Merchant_ID`) REFERENCES merchant(`Merchant_ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `rewards_program` (
	`Rewards_Program_ID` int,
    `Card_ID` varchar(50),
    `Decorator_Id` int,
	`Reward_Type` enum('Miles', 'Cashback', 'Points'),
    `Amount` double,
	`Min_Spend` double,
    `Is_Stackable` bool,
    `MCC` int,
	`Merchant_ID` int,
	CONSTRAINT `rewards_program_pk` PRIMARY KEY (`Rewards_Program_ID`),
	CONSTRAINT `rewards_program_fk1` FOREIGN KEY (`Card_ID`) REFERENCES card(`Card_ID`),
	CONSTRAINT `rewards_program_fk2` FOREIGN KEY (`Decorator_Id`) REFERENCES decorator(`Decorator_Id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `campaign` (
	`Campaign_ID` int,
	`Rewards_Program_ID` int,
    `Merchant_ID` int,
    `Start_Date` datetime,
	`End_Date` datetime,
    `Description` varchar(300),
	CONSTRAINT `campaign_pk` PRIMARY KEY (`Campaign_ID`),
	CONSTRAINT `campaign_fk1` FOREIGN KEY (`Rewards_Program_ID`) REFERENCES rewards_program(`Rewards_Program_ID`),
	CONSTRAINT `campaign_fk2` FOREIGN KEY (`Merchant_ID`) REFERENCES merchant(`Merchant_ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `exclusion` (
	`Merchant_ID` int,
	`Rewards_Program_ID` int,
	CONSTRAINT `exclusion_pk` PRIMARY KEY (`Merchant_ID`, `Rewards_Program_ID`),
	CONSTRAINT `exclusion_fk1` FOREIGN KEY (`Rewards_Program_ID`) REFERENCES rewards_program(`Rewards_Program_ID`),
	CONSTRAINT `exclusion_fk2` FOREIGN KEY (`Merchant_ID`) REFERENCES merchant(`Merchant_ID`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;




