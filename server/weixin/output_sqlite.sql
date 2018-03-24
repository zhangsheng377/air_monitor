
-- Table: sensor_names
CREATE TABLE sensor_names ( 
    name TEXT PRIMARY KEY
              NOT NULL 
);

INSERT INTO [sensor_names] ([name]) VALUES ('PM2_5');
INSERT INTO [sensor_names] ([name]) VALUES ('CO');
INSERT INTO [sensor_names] ([name]) VALUES ('SO2');
INSERT INTO [sensor_names] ([name]) VALUES ('O3');
INSERT INTO [sensor_names] ([name]) VALUES ('HCHO');
INSERT INTO [sensor_names] ([name]) VALUES ('MQ2');

-- Table: users
CREATE TABLE users ( 
    openid           TEXT    PRIMARY KEY
                             NOT NULL,
    device_id        TEXT    NOT NULL
                             DEFAULT '354298',
    PM2_5_limit      DOUBLE  NOT NULL
                             DEFAULT '200.0',
    CO_limit         DOUBLE  NOT NULL
                             DEFAULT '200.0',
    SO2_limit        DOUBLE  NOT NULL
                             DEFAULT '40.0',
    O3_limit         DOUBLE  NOT NULL
                             DEFAULT '99999.0',
    HCHO_limit       DOUBLE  NOT NULL
                             DEFAULT '99999.0',
    MQ2_limit        DOUBLE  NOT NULL
                             DEFAULT '99999.0',
    PM2_5_alertvalue DOUBLE  NOT NULL
                             DEFAULT '0.0',
    CO_alertvalue    DOUBLE  NOT NULL
                             DEFAULT '0.0',
    SO2_alertvalue   DOUBLE  NOT NULL
                             DEFAULT '0.0',
    O3_alertvalue    DOUBLE  NOT NULL
                             DEFAULT '0.0',
    HCHO_alertvalue  DOUBLE  NOT NULL
                             DEFAULT '0.0',
    MQ2_alertvalue   DOUBLE  NOT NULL
                             DEFAULT '0.0',
    PM2_5_alerttime  INTEGER NOT NULL
                             DEFAULT '0',
    CO_alerttime     INTEGER NOT NULL
                             DEFAULT '0',
    SO2_alerttime    INTEGER NOT NULL
                             DEFAULT '0',
    O3_alerttime     INTEGER NOT NULL
                             DEFAULT '0',
    HCHO_alerttime   INTEGER NOT NULL
                             DEFAULT '0',
    MQ2_alerttime    INTEGER NOT NULL
                             DEFAULT '0' 
);

INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwaD036go9d6b3ELlyFMjjD0', 353097, 0, 200.0, 40.0, 999, 99999.0, 99999.0, 112, 917.96875, 50, 61, 0.0, 0.0, 1502896144, 1491457943, 1502896145, 1492609558, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwfBY0hM3y_UM9dg9RyYntoU', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 1019.53125, 917.96875, 50, 0.0, 0.0, 0.0, 1488882914, 1491457944, 1491465766, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwYDA_hUSYTveYUR1jO0WaPQ', 353097, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 218, 917.96875, 46, 0.0, 0.0, 0.0, 1491459968, 1491457945, 1491464147, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwd6NXwAbjtI6Fj3xqDh2Bss', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 1019.53125, 917.96875, 50, 0.0, 0.0, 0.0, 1488882914, 1491457945, 1491465766, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwU3sG2pdljoq6ZWtBYFI9-Q', 354298, 500, 1000, 500, 99999.0, 99999.0, 99999.0, 1019.53125, 0.0, 0.0, 0.0, 0.0, 0.0, 1488882914, 0, 0, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwXf7rrHsQtknyd0honVkL_Y', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 1019.53125, 917.96875, 50, 0.0, 0.0, 0.0, 1488882915, 1491457946, 1491465767, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwde8zDF3cATEzimiT7qjVjA', 354298, 50, 70, 78, 60, 999, 60, 106, 126, 100, 140, 0.0, 141, 1502896146, 1502896146, 1502896147, 1502896148, 0, 1502896148);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwbntTx3kLsw4s-vNm6ZDwOQ', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 1019.53125, 917.96875, 50, 0.0, 0.0, 0.0, 1488882915, 1491457947, 1491465767, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwdFJ0u6cwSm_2ZitTRChWdo', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 1019.53125, 917.96875, 50, 0.0, 0.0, 0.0, 1488882916, 1491457947, 1491465768, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwbfg7LuLFvJvYcOcwTbIkvY', 353097, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 1019.53125, 917.96875, 100, 0.0, 0.0, 0.0, 1488882916, 1491457948, 1502896148, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwdY9VkNsFK2zBPsHWvkibWg', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwar-kNsK7_UtVWY90XoeIY0', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwVYLt2M2Mk9Ni3k30zdGGDk', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 1019.53125, 917.96875, 50, 0.0, 0.0, 0.0, 1488882917, 1491457950, 1491465769, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwcp_laN8-MlVlFoa_NosXF0', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwdghSqGttW7yHWtGe1WWxKY', 354298, 100, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 112, 917.96875, 50, 0.0, 0.0, 0.0, 1491462949, 1491457951, 1494604418, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwXLddpT7D9b9oYlLRiY_BeM', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwXjTtYix9_eLDBA5fjPvgw8', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 1019.53125, 917.96875, 304.6875, 0.0, 0.0, 0.0, 1488882918, 1491457951, 1491457952, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwUtTmtu8ZAdh-vBMluF_Mbg', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwcJw5xbADvtlV_Zh60s5ta8', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 0.0, 917.96875, 50, 0.0, 0.0, 0.0, 0, 1491457952, 1491465771, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwbz3kd6PFEwSQrcpZYaSrCw', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, 99999.0, 0.0, 917.96875, 50, 0.0, 0.0, 0.0, 0, 1491457953, 1491465771, 0, 0, 0);
INSERT INTO [users] ([openid], [device_id], [PM2_5_limit], [CO_limit], [SO2_limit], [O3_limit], [HCHO_limit], [MQ2_limit], [PM2_5_alertvalue], [CO_alertvalue], [SO2_alertvalue], [O3_alertvalue], [HCHO_alertvalue], [MQ2_alertvalue], [PM2_5_alerttime], [CO_alerttime], [SO2_alerttime], [O3_alerttime], [HCHO_alerttime], [MQ2_alerttime]) VALUES ('owYXAwboTUJd0D1cIyuKGFpoZe28', 354298, 200.0, 200.0, 40.0, 99999.0, 99999.0, -0.7, 0.0, 917.96875, 50, 0.0, 0.0, 34, 0, 1491457954, 1491465772, 0, 0, 1494604419);

-- Table: devices
CREATE TABLE devices ( 
    device_id    TEXT   PRIMARY KEY
                        NOT NULL,
    location_x   DOUBLE NOT NULL,
    location_y   DOUBLE NOT NULL,
    sensor_PM2_5 TEXT   NOT NULL,
    sensor_CO    TEXT   NOT NULL,
    sensor_SO2   TEXT   NOT NULL,
    sensor_O3    TEXT   NOT NULL,
    sensor_HCHO  TEXT   NOT NULL,
    sensor_MQ2   TEXT   NOT NULL 
);

INSERT INTO [devices] ([device_id], [location_x], [location_y], [sensor_PM2_5], [sensor_CO], [sensor_SO2], [sensor_O3], [sensor_HCHO], [sensor_MQ2]) VALUES (353097, 23.101552966333493, 114.419150573398, 397985, 398391, 400110, 400118, 403705, 403706);
INSERT INTO [devices] ([device_id], [location_x], [location_y], [sensor_PM2_5], [sensor_CO], [sensor_SO2], [sensor_O3], [sensor_HCHO], [sensor_MQ2]) VALUES (354298, 32.00441054522347, 118.7206203869564, 400108, 400109, 400111, 400119, 403707, 403708);

-- Index: 
;


-- Index: 
;


-- Index: 
;

