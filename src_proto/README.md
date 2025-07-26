# Modefied protobuf files

This folder contains unmodified protobuf files. For modified protobuf files see [proto](../proto/).
## Command IDs mapping

> [!NOTE]
> Some Command IDs are associated with multiple commands.

| ID (Decimal; to DTU) | ID (Hex; to DTU) | Command (to DTU) | ID (Hex; from DTU)[^1] | Command (from DTU)[^1] | File |
| --- | --- | --- | --- | --- | --- |
|   [^2] | 0x2301 | APPInfoDataResDTO | 0x2201 | APPInfoDataReqDTO | [APPInfomationData](APPInfomationData.proto) |
|   [^2] | 0x2302 | HBResDTO | 0x2202 | HBReqDTO | [APPHeartbeatPB](APPHeartbeatPB.proto) |
|   [^2] | 0x2303 | RealDataResDTO | 0x2203 | RealDataReqDTO | [RealData](RealData.proto) |
|   [^2] | 0x2304 | RealDataResDTO | 0x2204 | RealDataReqDTO | [RealData](RealData.proto) |
|   [^2] | 0x2305 | CommandResDTO | 0x2205 | CommandReqDTO | [CommandPB](CommandPB.proto) |
|   [^2] | 0x2306 | CommandStatusResDTO | 0x2206 | CommandStatusReqDTO | [CommandPB](CommandPB.proto) |
|   [^2] | 0x2307 | DevConfigFetchResDTO | 0x2207 | DevConfigFetchReqDTO | [DevConfig](DevConfig.proto) |
|   [^2] | 0x2308 | DevConfigPutResDTO | 0x2208 | DevConfigPutReqDTO | [DevConfig](DevConfig.proto) |
|   [^2] | 0x230A | WaveResDTO | 0x220A | WaveReqDTO | [WarnData](WarnData.proto) |
|   [^2] | 0x230B | WarnResDTO | 0x220B | WarnReqDTO | [WarnData](WarnData.proto) |
|   [^2] | 0x230C | RealResDTO | 0x220C | RealReqDTO | [RealDataNew](RealDataNew.proto) |
|   [^2] | 0x230D | RealResDTO | 0x220D | RealReqDTO | [RealDataNew](RealDataNew.proto) |
|  12545 | 0x3101 | HbSmlpeResDTO | 0x3001 | HbSmlpeReqDTO | [HeartbeatSMLPE](HeartbeatSMLPE.proto) |
|  12546 | 0x3102 | ReadHRegResDTO | 0x3002 | ReadHRegReqDTO | [DevConfigSMLPE](DevConfigSMLPE.proto) |
|  12547 | 0x3103 | WriteHRegResDTO | 0x3003 | WriteHRegReqDTO | [DevConfigSMLPE](DevConfigSMLPE.proto) |
|  12552 | 0x3108 | CmdSmlpeResDTO | 0x3008 | CmdSmlpeReqDTO | [CmdSMLPE](CmdSMLPE.proto) |
| -31999 | 0x8301 | HBResDTO | 0x8201 | HBReqDTO | [APPHeartbeatPB](APPHeartbeatPB.proto) |
| -31998 | 0x8302 | RegisterResDTO | 0x8202 | StorageRegisterReqDTO | [StorageRegisterPB](StorageRegisterPB.proto) |
| -31997 | 0x8303 | StorageDataRes | 0x8203 | StorageDataReqDTO | [StorageData](StorageData.proto) |
| -31995 | 0x8305 | CommandResDTO | 0x8205 | CommandReqDTO | [CommandPB](CommandPB.proto) |
| -31994 | 0x8306 | CommandStatusResDTO | 0x8206 | CommandStatusReqDTO | [CommandPB](CommandPB.proto) |
| -31993 | 0x8307 | DevConfigFetchResDTO | 0x8207 | DevConfigFetchReqDTO | [DevConfig](DevConfig.proto) |
| -31992 | 0x8308 | DevConfigPutResDTO | 0x8208 | DevConfigPutReqDTO | [DevConfig](DevConfig.proto) |
| -30463 | 0x8901 | AUInfoResDTO | 0x8801 | AUInfoReqDTO | [AUInfo](AUInfo.proto) |
| -30462 | 0x8902 | GWHBResDTO | 0x8802 | GWHBReqDTO | [GWHeartbeat](GWHeartbeat.proto) |
| -30461 | 0x8903 | AuRealResDTO | 0x8803 | AuRealReqDTO | [AURealData](AURealData.proto) |
| -30460 | 0x8904 | AUWarnResDTO | 0x8804 | AUWarnReqDTO | [AUWarnData](AUWarnData.proto) |
| -30459 | 0x8905 | CommCmdResDTO | 0x8805 | CommCmdReqDTO | [CommCmd](CommCmd.proto) |
| -30458 | 0x8906 | CommCmdStatusResDTO | 0x8806 | CommCmdStatusReqDTO | [CommCmd](CommCmd.proto) |
| -30455 | 0x8909 | APPGetConfigRes | 0x8809 | APPGetConfigReq | [APPGetConfig](APPGetConfig.proto) |
| -30454 | 0x890A | APPSetConfigRes | 0x880A | APPSetConfigReq | [APPSetConfig](APPSetConfig.proto) |
| -30453 | 0x890B | APPNetworkInfoRes | 0x880B | APPNetworkInfoReq | [APPNetworkInfo](APPNetworkInfo.proto) |
| -30452 | 0x890C | AUGetHistPowerRes | 0x880C | AUGetHistPowerReq | [AppAUGetHistPower](AppAUGetHistPower.proto) |
| -30451 | 0x890D | AUGetHistEDRes | 0x880D | AUGetHistEDReq | [AppAUGetHistED](AppAUGetHistED.proto) |
| -30450 | 0x890E | FWInfoResDTO | 0x880E | FWInfoReqDTO | [AppFWOTA](AppFWOTA.proto) |
| -30449 | 0x890F | FWOTAResDTO | 0x880F | FWOTAReqDTO | [AppFWOTA](AppFWOTA.proto) |
| -30448 | 0x8910 | AUDspCmdSetResDTO | 0x8810 | AUDspCmdSetReqDTO | [AUDspCmdSet](AUDspCmdSet.proto) |
| -30447 | 0x8911 | AUDspCmdGetResDTO | 0x8811 | AUDspCmdGetReqDTO | [AUDspCmdSet](AUDspCmdSet.proto) |
| -23807 | 0xA301 | APPInfoDataResDTO | 0xA201 | APPInfoDataReqDTO | [APPInfomationData](APPInfomationData.proto) |
| -23806 | 0xA302 | HBResDTO | 0xA202 | HBReqDTO | [APPHeartbeatPB](APPHeartbeatPB.proto) |
| -23805 | 0xA303 | RealDataResDTO | 0xA203 | RealDataReqDTO | [RealData](RealData.proto) |
| -23804 | 0xA304 | WarnResDTO | 0xA204 | WarnReqDTO | [WarnData](WarnData.proto) |
| -23804 | 0xA304 | WInfoResDTO | 0xA204 | WInfoReqDTO | [AlarmData](AlarmData.proto) |
| -23803 | 0xA305 | CommandResDTO | 0xA205 | CommandReqDTO | [CommandPB](CommandPB.proto) |
| -23802 | 0xA306 | CommandStatusResDTO | 0xA206 | CommandStatusReqDTO | [CommandPB](CommandPB.proto) |
| -23801 | 0xA307 | DevConfigFetchResDTO | 0xA207 | DevConfigFetchReqDTO | [DevConfig](DevConfig.proto) |
| -23800 | 0xA308 | DevConfigPutResDTO | 0xA208 | DevConfigPutReqDTO | [DevConfig](DevConfig.proto) |
| -23799 | 0xA309 | GetConfigRes | 0xA209 | GetConfigReq | [GetConfig](GetConfig.proto) |
| -23792 | 0xA310 | SetConfigRes | 0xA210 | SetConfigReq | [SetConfig](SetConfig.proto) |
| -23791 | 0xA311 | RealResDTO | 0xA211 | RealReqDTO | [RealDataNew](RealDataNew.proto) |
| -23791 | 0xA311 | APPInfoDataResDTO | 0xA211 | APPInfoDataReqDTO | [APPInfomationData](APPInfomationData.proto) |
| -23790 | 0xA312 | GPSTResDTO | 0xA212 | GPSTReqDTO | [GPSTData](GPSTData.proto) |
| -23789 | 0xA313 | AutoSearchRes | 0xA213 | AutoSearchReq | [AutoSearch](AutoSearch.proto) |
| -23788 | 0xA314 | NetworkInfoRes | 0xA214 | NetworkInfoReq | [NetworkInfo](NetworkInfo.proto) |
| -23788 | 0xA314 | GetConfigRes | 0xA214 | GetConfigReq | [GetConfig](GetConfig.proto) |
| -23788 | 0xA314 | SetConfigRes | 0xA214 | SetConfigReq | [SetConfig](SetConfig.proto) |
| -23787 | 0xA315 | AppGetHistPowerRes | 0xA215 | AppGetHistPowerReq | [AppGetHistPower](AppGetHistPower.proto) |
| -23786 | 0xA316 | AppGetHistEDRes | 0xA216 | AppGetHistEDReq | [AppGetHistED](AppGetHistED.proto) |
| -15614 | 0xC302 | ESRegResDTO | 0xC202 | ESRegReqDTO | [ESRegPB](ESRegPB.proto) |
| -15613 | 0xC303 | ESDataResDTO | 0xC203 | ESDataReqDTO | [ESDataPB](ESDataPB.proto) |
| -15609 | 0xC307 | ESUserSetPutReqDTO | 0xC207 | ESUserSetPutResDTO | [ESUserSet](ESUserSet.proto) |
| -15608 | 0xC308 | ESUserSetPutResDTO | 0xC208 | ESUserSetPutReqDTO | [ESUserSet](ESUserSet.proto) |
| -15362 | 0xC3FE | CommDevCfgFetchResDTO | 0xC2FE | CommDevCfgFetchReqDTO | [CommDevCfg](CommDevCfg.proto) |
| -15361 | 0xC3FF | CommDevCfgPutResDTO | 0xC2FF | CommDevCfgPutReqDTO | [CommDevCfg](CommDevCfg.proto) |
| -15361 | 0xC3FF | ESCOMMCfgBO | 0xC2FF | ESHMIDCfgMO | [ESCommCfg](ESCommCfg.proto) |
| -14078 | 0xC902 | PVInvInfoResDTO | 0xC802 | PVInvInfoReqDTO | [PV_Inv_Information](PV_Inv_Information.proto) |
| -14077 | 0xC903 | PVInvDataResDTO | 0xC803 | PVInvDataReqDTO | [PV_Inv_RT_Data](PV_Inv_RT_Data.proto) |
| -14073 | 0xC907 | PVInvUserSetGetResDTO | 0xC807 | PVInvUserSetGetReqDTO | [PV_Inv_UserSet](PV_Inv_UserSet.proto) |
| -14072 | 0xC908 | PVInvUserSetGetReqDTO | 0xC808 | PVInvUserSetGetResDTO | [PV_Inv_UserSet](PV_Inv_UserSet.proto) |
| -14071 | 0xC909 | PVInvWarnResDTO | 0xC809 | PVInvWarnReqDTO | [PV_Inv_Warn](PV_Inv_Warn.proto) |
| -14013 | 0xC943 | PVInvUpdateResDTO | 0xC843 | PVInvUpdateReqDTO | [PV_Inv_Update](PV_Inv_Update.proto) |
| -14012 | 0xC944 | PVInvOTAResDTO | 0xC844 | PVInvOTAReqDTO | [PV_Inv_Update](PV_Inv_Update.proto) |
| -13888 | 0xC9C0 | PVInvCurveResDTO | 0xC8C0 | PVInvCurveReqDTO | [PV_Inv_Curve](PV_Inv_Curve.proto) |
| -13887 | 0xC9C1 | PVInvEnergyCurveResDTO | 0xC8C1 | PVInvEnergyCurveReqDTO | [PV_Inv_EnergyCurve](PV_Inv_EnergyCurve.proto) |
| -13872 | 0xC9D0 | PVInvEventLogResDTO | 0xC8D0 | PVInvEventLogReqDTO | [PV_Inv_EventLog](PV_Inv_EventLog.proto) |
| -13054 | 0xCD02 | HPCSInfoResDTO | 0xCC02 | HPCSInfoReqDTO | [HPCS_Information](HPCS_Information.proto) |
| -13053 | 0xCD03 | HPCSDataResDTO | 0xCC03 | HPCSDataReqDTO | [HPCS_RT_Data](HPCS_RT_Data.proto) |
| -13053 | 0xCD03 | HPCSLRDataResDTO | 0xCC03 | HPCSLRDataReqDTO | [HPCSLR_RT_Data](HPCSLR_RT_Data.proto) |
| -13053 | 0xCD03 | HPCSInfoResDTO | 0xCC03 | HPCSInfoReqDTO | [HPCS_Information](HPCS_Information.proto) |
| -13049 | 0xCD07 | HPCSLRUserSetGetResDTO | 0xCC07 | HPCSLRUserSetGetReqDTO | [HPCSLR_UserSet](HPCSLR_UserSet.proto) |
| -13049 | 0xCD07 | HPCSUserSetGetResDTO | 0xCC07 | HPCSUserSetGetReqDTO | [HPCS_UserSet](HPCS_UserSet.proto) |
| -13048 | 0xCD08 | HPCSLRUserSetGetReqDTO | 0xCC08 | HPCSLRUserSetGetResDTO | [HPCSLR_UserSet](HPCSLR_UserSet.proto) |
| -13048 | 0xCD08 | HPCSUserSetGetReqDTO | 0xCC08 | HPCSUserSetGetResDTO | [HPCS_UserSet](HPCS_UserSet.proto) |
| -13047 | 0xCD09 | HPCSWarnResDTO | 0xCC09 | HPCSWarnReqDTO | [HPCS_Warn](HPCS_Warn.proto) |
|  -9471 | 0xDB01 | GWInfoResDTO | 0xDA01 | GWInfoReqDTO | [GWInfo](GWInfo.proto) |
|  -9471 | 0xDB01 | ESRegResDTO | 0xDA01 | ESRegReqDTO | [ESRegPB](ESRegPB.proto) |
|  -9471 | 0xDB01 | GWGetConfigRes | 0xDA01 | GWGetConfigReq | [GWGetConfig](GWGetConfig.proto) |
|  -9471 | 0xDB01 | GWSetConfigRes | 0xDA01 | GWSetConfigReq | [GWSetConfig](GWSetConfig.proto) |
|  -9470 | 0xDB02 | GWHBResDTO | 0xDA02 | GWHBReqDTO | [GWHeartbeat](GWHeartbeat.proto) |
|  -9469 | 0xDB03 | CommCmdResDTO | 0xDA03 | CommCmdReqDTO | [CommCmd](CommCmd.proto) |
|  -9468 | 0xDB04 | CommCmdStatusResDTO | 0xDA04 | CommCmdStatusReqDTO | [CommCmd](CommCmd.proto) |
|  -9466 | 0xDB06 | GWNetInfoRes | 0xDA06 | GWNetInfoReq | [GWNetInfo](GWNetInfo.proto) |
|  -9466 | 0xDB06 | GWGetConfigRes | 0xDA06 | GWGetConfigReq | [GWGetConfig](GWGetConfig.proto) |
|  -9466 | 0xDB06 | GWSetConfigRes | 0xDA06 | GWSetConfigReq | [GWSetConfig](GWSetConfig.proto) |
|  -9465 | 0xDB07 | SetConfigRes | 0xDA07 | SetConfigReq | [SetConfig](SetConfig.proto) |
|  -9464 | 0xDB08 | GetConfigRes | 0xDA08 | GetConfigReq | [GetConfig](GetConfig.proto) |
|  -9221 | 0xDBFB | MemReadResDTO | 0xDAFB | MemReadReqDTO | [GWMemRW](GWMemRW.proto) |
|  -9220 | 0xDBFC | MemWriteResDTO | 0xDAFC | MemWriteReqDTO | [GWMemRW](GWMemRW.proto) |
|  -9218 | 0xDBFE | CommDevCfgFetchResDTO | 0xDAFE | CommDevCfgFetchReqDTO | [CommDevCfg](CommDevCfg.proto) |
|  -9217 | 0xDBFF | CommDevCfgPutResDTO | 0xDAFF | CommDevCfgPutReqDTO | [CommDevCfg](CommDevCfg.proto) |
|  -3838 | 0xF102 | InfoResDTO | 0xF002 | InfoReqDTO | [SMLPEInfo](SMLPEInfo.proto) |
|  -3837 | 0xF103 | DTLResDTO | 0xF003 | DTLReqDTO | [SMLPERTData](SMLPERTData.proto) |
|  -3836 | 0xF104 | DTLStateResDTO | 0xF004 | DTLStateReqDTO | [SMLPEState](SMLPEState.proto) |
|  -3835 | 0xF105 | SMLPENetworkResDTO | 0xF005 | SMLPENetworkReqDTO | [SMLPENetwork](SMLPENetwork.proto) |

[^1]: automatically derived from found commands, generated files and previous observations
[^2]: gathered from other sources (not found in the files)

## Protos file tree

The following file tree represents the file structure of the proto files extracted from the Android app.

```
📂 
 ┗━📁 com
    ┣━📁 balcony
    ┃  ┗━📁 proto
    ┃     ┗━📁 bean
    ┃        ┗━📁 jg
    ┃           ┣━📄 AppAUGetHistED.proto
    ┃           ┣━📄 AppAUGetHistPower.proto
    ┃           ┣━📄 AppFWOTA.proto
    ┃           ┣━📄 APPGetConfig.proto
    ┃           ┣━📄 APPNetworkInfo.proto
    ┃           ┣━📄 APPSetConfig.proto
    ┃           ┣━📄 AUDspCmdSet.proto
    ┃           ┣━📄 AUInfo.proto
    ┃           ┣━📄 AURealData.proto
    ┃           ┗━📄 AUWarnData.proto
    ┗━📁 hoymiles
       ┗━📁 proto
          ┗━📁 bean
             ┣━📁 deprecated
             ┃  ┗━📁 logger
             ┃     ┣━📄 CmdSMLPE.proto
             ┃     ┣━📄 DevConfigSMLPE.proto
             ┃     ┣━📄 FileDataSMLPE.proto
             ┃     ┗━📄 HeartbeatSMLPE.proto
             ┣━📁 ld
             ┃  ┣━📁 es
             ┃  ┃  ┣━📄 ESCheckPB.proto
             ┃  ┃  ┣━📄 ESCommCfg.proto
             ┃  ┃  ┣━📄 ESCPCfg.proto
             ┃  ┃  ┣━📄 ESDataPB.proto
             ┃  ┃  ┣━📄 ESDebugLog.proto
             ┃  ┃  ┣━📄 ESParaSet.proto
             ┃  ┃  ┣━📄 ESRegPB.proto
             ┃  ┃  ┣━📄 ESUserSet.proto
             ┃  ┃  ┣━📄 ESWarnPB.proto
             ┃  ┃  ┣━📄 StorageData.proto
             ┃  ┃  ┗━📄 StorageRegisterPB.proto
             ┃  ┣━📁 gw
             ┃  ┃  ┣━📄 CommCmd.proto
             ┃  ┃  ┣━📄 CommDevCfg.proto
             ┃  ┃  ┣━📄 GWGetConfig.proto
             ┃  ┃  ┣━📄 GWHeartbeat.proto
             ┃  ┃  ┣━📄 GWInfo.proto
             ┃  ┃  ┣━📄 GWMemRW.proto
             ┃  ┃  ┣━📄 GWNetInfo.proto
             ┃  ┃  ┣━📄 GWSetConfig.proto
             ┃  ┃  ┗━📄 GWWarn.proto
             ┃  ┣━📁 lj
             ┃  ┃  ┣━📄 PV_Inv_Curve.proto
             ┃  ┃  ┣━📄 PV_Inv_EnergyCurve.proto
             ┃  ┃  ┣━📄 PV_Inv_EventLog.proto
             ┃  ┃  ┣━📄 PV_Inv_Information.proto
             ┃  ┃  ┣━📄 PV_Inv_RT_Data.proto
             ┃  ┃  ┣━📄 PV_Inv_Update.proto
             ┃  ┃  ┣━📄 PV_Inv_UserSet.proto
             ┃  ┃  ┗━📄 PV_Inv_Warn.proto
             ┃  ┣━📁 lr
             ┃  ┃  ┣━📄 HPCSLR_Information.proto
             ┃  ┃  ┣━📄 HPCSLR_RT_Data.proto
             ┃  ┃  ┣━📄 HPCSLR_UserSet.proto
             ┃  ┃  ┗━📄 HPCSLR_Warn.proto
             ┃  ┣━📁 power
             ┃  ┃  ┣━📄 AlarmData.proto
             ┃  ┃  ┣━📄 AppGetHistED.proto
             ┃  ┃  ┣━📄 AppGetHistPower.proto
             ┃  ┃  ┣━📄 APPHeartbeatPB.proto
             ┃  ┃  ┣━📄 APPInfomationData.proto
             ┃  ┃  ┣━📄 AutoSearch.proto
             ┃  ┃  ┣━📄 CommandPB.proto
             ┃  ┃  ┣━📄 DevConfig.proto
             ┃  ┃  ┣━📄 EventData.proto
             ┃  ┃  ┣━📄 GetConfig.proto
             ┃  ┃  ┣━📄 GPSTData.proto
             ┃  ┃  ┣━📄 NetworkInfo.proto
             ┃  ┃  ┣━📄 RealData.proto
             ┃  ┃  ┣━📄 RealDataNew.proto
             ┃  ┃  ┣━📄 SetConfig.proto
             ┃  ┃  ┗━📄 WarnData.proto
             ┃  ┣━📁 ql
             ┃  ┃  ┣━📄 HPCS_Information.proto
             ┃  ┃  ┣━📄 HPCS_RT_Data.proto
             ┃  ┃  ┣━📄 HPCS_UserSet.proto
             ┃  ┃  ┗━📄 HPCS_Warn.proto
             ┃  ┗━📁 rsd
             ┃     ┣━📄 SMLPEInfo.proto
             ┃     ┣━📄 SMLPENetwork.proto
             ┃     ┣━📄 SMLPERTData.proto
             ┃     ┗━📄 SMLPEState.proto
             ┗━📁 net
                ┣━📄 CfgRuleConfigPB.proto
                ┣━📄 ChartPB.proto
                ┗━📄 PlaybackDataPB.proto
```
