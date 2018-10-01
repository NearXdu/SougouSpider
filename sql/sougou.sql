SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `sougoudb`
--



--
-- Table: `sougou_cate`
--

CREATE TABLE IF NOT EXISTS `sougou_cate`(
  `id` INT(11) NOT NULL COMMENT 'ID',
  `url` VARCHAR(255) NOT NULL COMMENT '爬取URL',
  `page` int(11) NOT NULL COMMENT '页数',
  `category` VARCHAR(512) NOT NULL COMMENT '一级标题',
  `subcategory` VARCHAR(512) NOT NULL COMMENT '二级标题',
  `create_time` DATETIME DEFAULT NULL COMMENT '创建时间',
  `update_time` DATETIME DEFAULT NULL COMMENT '最后修改时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;




--
-- Table: `sougou_detail`
--

CREATE TABLE IF NOT EXISTS `sougou_detail`(
  `id` INT(11) NOT NULL COMMENT 'ID',
  `url` VARCHAR(255) NOT NULL COMMENT '详情页URL',
  `filename` VARCHAR(512) NOT NULL COMMENT '文件名',
  `category` VARCHAR(512) NOT NULL COMMENT '一级标题',
  `subcategory` VARCHAR(512) NOT NULL COMMENT '二级标题',
  `create_time` DATETIME DEFAULT NULL COMMENT '创建时间',
  `update_time` DATETIME DEFAULT NULL COMMENT '最后修改时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;



--
-- Table: `sougou_keyword`
--

CREATE TABLE IF NOT EXISTS `sougou_keyword`(
  `id` INT(11) NOT NULL COMMENT 'ID',
  `keyword` VARCHAR(255) NOT NULL COMMENT '关键字',
  `category` VARCHAR(512) NOT NULL COMMENT '一级标题',
  `subcategory` VARCHAR(512) NOT NULL COMMENT '二级标题',
  `subsubcategory` VARCHAR(512) NOT NULL COMMENT '三级标题',
  `create_time` DATETIME DEFAULT NULL COMMENT '创建时间',
  `update_time` DATETIME DEFAULT NULL COMMENT '最后修改时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 删除Table sougou_cate
--

DROP TABLE sougou_cate;

--
-- 修改Table sougou_detail to t_sougou_list 列表页
--

ALTER TABLE `sougou_detail` RENAME TO `t_sougou_list`;
ALTER TABLE `t_sougou_list` DROP COLUMN `category`;
ALTER TABLE `t_sougou_list` DROP COLUMN `subcategory`;

--
-- Table: t_sougou_detail 详情页
--

CREATE TABLE IF NOT EXISTS `t_sougou_detail`(
  `id` INT(11) NOT NULL COMMENT 'ID',
  `filename` VARCHAR(512) NOT NULL COMMENT '文件名',
  `url` VARCHAR(255) NOT NULL COMMENT '下载URL',
  `create_time` DATETIME DEFAULT NULL COMMENT '创建时间',
  `update_time` DATETIME DEFAULT NULL COMMENT '最后修改时间'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


--
-- Table: sougou_keyword 重命名t_sougou_keyword
--
ALTER TABLE `sougou_keyword` RENAME TO `t_sougou_keyword`
