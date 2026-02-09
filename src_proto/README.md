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
| -31998 | 0x8302 | APPInfoDataResDTO | 0x8202 | APPInfoDataReqDTO | [APPInfomationData](APPInfomationData.proto) |
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
| -23803 | 0xA305 | CommandResDTO | 0xA205 | CommandReqDTO | [CommandPB](CommandPB.proto) |
| -23803 | 0xA305 | CommCmdResDTO | 0xA205 | CommCmdReqDTO | [CommCmd](CommCmd.proto) |
| -23802 | 0xA306 | CommandStatusResDTO | 0xA206 | CommandStatusReqDTO | [CommandPB](CommandPB.proto) |
| -23799 | 0xA309 | GetConfigRes | 0xA209 | GetConfigReq | [GetConfig](GetConfig.proto) |
| -23792 | 0xA310 | SetConfigRes | 0xA210 | SetConfigReq | [SetConfig](SetConfig.proto) |
| -23791 | 0xA311 | RealResDTO | 0xA211 | RealReqDTO | [RealDataNew](RealDataNew.proto) |
| -23790 | 0xA312 | GPSTResDTO | 0xA212 | GPSTReqDTO | [GPSTData](GPSTData.proto) |
| -23789 | 0xA313 | AutoSearchRes | 0xA213 | AutoSearchReq | [AutoSearch](AutoSearch.proto) |
| -23788 | 0xA314 | NetworkInfoRes | 0xA214 | NetworkInfoReq | [NetworkInfo](NetworkInfo.proto) |
| -23787 | 0xA315 | AppGetHistPowerRes | 0xA215 | AppGetHistPowerReq | [AppGetHistPower](AppGetHistPower.proto) |
| -23786 | 0xA316 | AppGetHistEDRes | 0xA216 | AppGetHistEDReq | [AppGetHistED](AppGetHistED.proto) |
| -23784 | 0xA318 | CommCmdResDTO | 0xA218 | CommCmdReqDTO | [CommCmd](CommCmd.proto) |
| -23784 | 0xA318 | CommCmdStatusResDTO | 0xA218 | CommCmdStatusReqDTO | [CommCmd](CommCmd.proto) |
| -23780 | 0xA31C | FWInfoResDTO | 0xA21C | FWInfoReqDTO | [AppFWOTA](AppFWOTA.proto) |
| -23779 | 0xA31D | FWOTAResDTO | 0xA21D | FWOTAReqDTO | [AppFWOTA](AppFWOTA.proto) |
| -23773 | 0xA323 | AppGetDevListRes | 0xA223 | AppGetDevListReq | [AppGetDevList](AppGetDevList.proto) |
|  -9471 | 0xDB01 | GWInfoResDTO | 0xDA01 | GWInfoReqDTO | [GWInfo](GWInfo.proto) |
|  -9471 | 0xDB01 | ReadHRegResDTO | 0xDA01 | ReadHRegReqDTO | [DevConfigSMLPE](DevConfigSMLPE.proto) |
|  -9471 | 0xDB01 | CmdSmlpeResDTO | 0xDA01 | CmdSmlpeReqDTO | [CmdSMLPE](CmdSMLPE.proto) |
|  -9471 | 0xDB01 | ESDataResDTO | 0xDA01 | ESDataReqDTO | [ESDataPB](ESDataPB.proto) |
|  -9471 | 0xDB01 | CommCmdStatusResDTO | 0xDA01 | CommCmdStatusReqDTO | [CommCmd](CommCmd.proto) |
|  -9471 | 0xDB01 | PVInvCurveResDTO | 0xDA01 | PVInvCurveReqDTO | [PV_Inv_Curve](PV_Inv_Curve.proto) |
|  -9471 | 0xDB01 | PVInvInfoResDTO | 0xDA01 | PVInvInfoReqDTO | [PV_Inv_Information](PV_Inv_Information.proto) |
|  -9471 | 0xDB01 | PVInvDataResDTO | 0xDA01 | PVInvDataReqDTO | [PV_Inv_RT_Data](PV_Inv_RT_Data.proto) |
|  -9471 | 0xDB01 | HPCSInfoResDTO | 0xDA01 | HPCSInfoReqDTO | [HPCS_Information](HPCS_Information.proto) |
|  -9470 | 0xDB02 | GWHBResDTO | 0xDA02 | GWHBReqDTO | [GWHeartbeat](GWHeartbeat.proto) |
|  -9469 | 0xDB03 | CommCmdResDTO | 0xDA03 | CommCmdReqDTO | [CommCmd](CommCmd.proto) |
|  -9468 | 0xDB04 | CommCmdStatusResDTO | 0xDA04 | CommCmdStatusReqDTO | [CommCmd](CommCmd.proto) |
|  -9466 | 0xDB06 | GWNetInfoRes | 0xDA06 | GWNetInfoReq | [GWNetInfo](GWNetInfo.proto) |
|  -9465 | 0xDB07 | SetConfigRes | 0xDA07 | SetConfigReq | [SetConfig](SetConfig.proto) |
|  -9465 | 0xDB07 | GWSetConfigRes | 0xDA07 | GWSetConfigReq | [GWSetConfig](GWSetConfig.proto) |
|  -9464 | 0xDB08 | GetConfigRes | 0xDA08 | GetConfigReq | [GetConfig](GetConfig.proto) |
|  -9464 | 0xDB08 | GWGetConfigRes | 0xDA08 | GWGetConfigReq | [GWGetConfig](GWGetConfig.proto) |
|  -9221 | 0xDBFB | MemReadResDTO | 0xDAFB | MemReadReqDTO | [GWMemRW](GWMemRW.proto) |
|  -9220 | 0xDBFC | DTLResDTO | 0xDAFC | DTLReqDTO | [SMLPERTData](SMLPERTData.proto) |
|  -9220 | 0xDBFC | MemWriteResDTO | 0xDAFC | MemWriteReqDTO | [GWMemRW](GWMemRW.proto) |
|  -9220 | 0xDBFC | WriteHRegResDTO | 0xDAFC | WriteHRegReqDTO | [DevConfigSMLPE](DevConfigSMLPE.proto) |
|  -9220 | 0xDBFC | DTLStateResDTO | 0xDAFC | DTLStateReqDTO | [SMLPEState](SMLPEState.proto) |
|  -9220 | 0xDBFC | InfoResDTO | 0xDAFC | InfoReqDTO | [SMLPEInfo](SMLPEInfo.proto) |
|  -9220 | 0xDBFC | GWSetConfigRes | 0xDAFC | GWSetConfigReq | [GWSetConfig](GWSetConfig.proto) |
|  -9218 | 0xDBFE | GWGetConfigRes | 0xDAFE | GWGetConfigReq | [GWGetConfig](GWGetConfig.proto) |
|  -9218 | 0xDBFE | CommDevCfgFetchResDTO | 0xDAFE | CommDevCfgFetchReqDTO | [CommDevCfg](CommDevCfg.proto) |
|  -9217 | 0xDBFF | CommDevCfgPutResDTO | 0xDAFF | CommDevCfgPutReqDTO | [CommDevCfg](CommDevCfg.proto) |
|  -9217 | 0xDBFF | GWSetConfigRes | 0xDAFF | GWSetConfigReq | [GWSetConfig](GWSetConfig.proto) |

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
             ┃  ┃  ┣━📄 ESEvent.proto
             ┃  ┃  ┣━📄 ESParaSet.proto
             ┃  ┃  ┣━📄 ESRegPB.proto
             ┃  ┃  ┣━📄 ESRegularSet.proto
             ┃  ┃  ┣━📄 ESSecData.proto
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
             ┃  ┃  ┣━📄 PV_Inv_Warn.proto
             ┃  ┃  ┗━📄 PV_Inv_Wave.proto
             ┃  ┣━📁 lr
             ┃  ┃  ┣━📄 HPCSLR_Information.proto
             ┃  ┃  ┣━📄 HPCSLR_RT_Data.proto
             ┃  ┃  ┣━📄 HPCSLR_UserSet.proto
             ┃  ┃  ┗━📄 HPCSLR_Warn.proto
             ┃  ┣━📁 power
             ┃  ┃  ┣━📄 AlarmData.proto
             ┃  ┃  ┣━📄 AppGetDevList.proto
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
                ┣━📄 CfgRuleConfigPBALL.proto
                ┣━📄 ChartPB.proto
                ┣━📄 ChartPBOldFloat.proto
                ┗━📄 PlaybackDataPB.proto
```
