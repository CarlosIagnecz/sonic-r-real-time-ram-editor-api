import ctypes
from ctypes import wintypes
import pymem

#SONIC R
#(https://info.sonicretro.org/Sonic_R/Technical_information/Windows_PC)
ramOff = -0x400000

#Player Struct
pX = 0x0
pY = 0x4
pZ = 0x8
pYZ = 0xC
pXZ = 0x10
pXY = 0x14
pRingCount = 0x18
pAnimFrame = 0x1C
pXmirror = 0x20
pYmirror = 0x24
pZmirror = 0x28
pXspeed = 0x2C
pYspeed = 0x30
pZspeed = 0x34
pGroundHeight = 0x38
pInWater = 0x40
pSinkTime = 0x42
pMomentum = 0x44
pTrackDist = 0x4C
pLapTime1 = 0x50
pLapTime2 = 0x50
pLapTime3 = 0x58
pPlace = 0x5C
pLap = 0x5E
pItemIcon = 0x64
pItemCooldown = 0x66
pWaterSplashTimer = 0x68
pWaterDepth = 0x6A
pPressFoward = 0x6C
pCamXZ = 0x70
pGrndFlag = 0x72
pFlightMode = 0x74
pMidAirTime = 0x96
pAnim = 0x98
pAniFrame = 0x9C
pLoopMode = 0xA0
pColideLayer = 0xA4
pAboveGeometry = 0xB0
pAboveGeometryMirror = 0xB2
pSlopeRX = 0xB4
pSlopeMagnitude = 0xB6
pSlopeRZ = 0xB8
pLoop = 0xBC #?
pLoopXZPos = 0xC0
pLoopXZDist = 0xC4
pLoop2 = 0xC8 #?
pLoopXZMom = 0xCC
pLoopMom = 0xD0 #mom is momentum btw
pDriftDir = 0xD4
pSfx = 0xEA
pUnknown = 0xF0 #Not sure what this is for.
pId = 0xF2 #Plater identity
pAI = 0x11c
pModel = 0x1E0
pRunAnim = 0x1EC
pBaloons = 0x1F4
pLastBalTim = 0x204

plrStruct = {
    pX : 'dw',
    pY : 'dw',
    pZ : 'dw',
    pYZ : 'dw',
    pXZ : 'dw',
    pXY : 'dw',
    pRingCount : 'dw',
    pAnimFrame : 'dw',
    pXmirror : 'dw',
    pYmirror : 'dw',
    pZmirror : 'dw',
    pXspeed : 'dw',
    pYspeed : 'dw',
    pZspeed : 'dw',
    pGroundHeight : 'dw',
    pInWater : 'w',
    pSinkTime : 'w',
    pMomentum : 'dw',
    pTrackDist : 'dw',
    pLapTime1 : 'w',
    pLapTime2 : 'w',
    pLapTime3 : 'w',
    pPlace : 'w',
    pLap : 'w',
    pItemIcon : 'w',
    pItemCooldown : 'w',
    pWaterSplashTimer : 'w',
    pWaterDepth : 'w',
    pPressFoward : 'w',
    pCamXZ : 'w',
    pGrndFlag : 'w',
    pFlightMode : 'w',
    pMidAirTime : 'w',
    pAnim : 'w',
    pAniFrame : 'dw',
    pLoopMode : 'dw',
    pColideLayer : 'dw',
    pAboveGeometry : 'w',
    pAboveGeometryMirror : 'w',
    pSlopeRX : 'w',
    pSlopeMagnitude : 'w',
    pSlopeRZ : 'w',
    pLoop : 'dw',
    pLoopXZPos : 'dw',
    pLoopXZDist : 'dw',
    pLoop2 : 'dw',
    pLoopXZMom : 'dw',
    pLoopMom : 'dw',
    pDriftDir : 'w',
    pSfx : 'w',
    pUnknown : 'w',
    pId : 'w',
    pAI : 'b',
    pModel : 'dw',
    pRunAnim : 'dw',
    pBaloons : 'w',
    pLastBalTim : 'dw'
    }
    
#CONFIGURE HOOK
while True:
    try:
        process = pymem.Pymem('SonicR.exe')
        print(f"Locked On to Sonic R! (pid={process.base_address})")
        break
    except:
        pass

#Sonic R RAM Constants
locs = {
        "windowed":0x5EDD24,
        "renderMode":0x75349C,
        "xResolution":0x461520,
        "yResolution":0x461524,
        "gameWindows":0x7AF280,
        "2pHudSplitStyle":0x7344EC,
        "modelCount":0x753504,
        "modelLimbCount":0x753678,
        "modelVertexCount":0x7BCB70,
        "modelPolyCount":0x7AF07C,
        "modelFrameCount":0x7535DC,
        "course":0x7AF13C,
        "gamemode":0x769F24,
        "emeraldSum":0x769F28,
        "timeAttMode":0x7BCB80,
        "musicVolume":0x7AF1B4,
        "gamePause":0x7C1BC0,
        "ScrTransSpd":0x5F388C,
        "ScrTransCover":0x7BCB28,
        "controlBitfieldP1":0x4A3608,
        "controlBitfieldP2":0x4A360A,
        "controlBitfieldP3":0x4A360C,
        "controlBitfieldP4":0x4A360E,
        "verticalOption":0x752828,
        "horizOption":0x7B7D48,
        "horizOptionDest":0x752858,
        "weather":0x8607BC,
        "timeOfDay":0x85EB78,
        "textureBufferPtrs":0x5D359C,
        "charUnlockArray":0x752BE0,
        "p1Data":0x7B7388,
        "p2Data":0x7B7388+0x71C,
        "p3Data":0x7B7388+(0x71C*2),
        "p4Data":0x7B7388+(0x71C*3),
        "p5Data":0x7B7388+(0x71C*3)}

form = {
        "windowed":'dw',
        "renderMode":'dw',
        "xResolution":'dw',
        "yResolution":'w',
        "gameWindows":'dw',
        "2pHudSplitStyle":'dw',
        "modelCount":'dw',
        "modelLimbCount":'dw',
        "modelVertexCount":'dw',
        "modelPolyCount":'dw',
        "modelFrameCount":'dw',
        "course":'w',
        "gamemode":'dw',
        "emeraldSum":'w',
        "timeAttMode":'dw',
        "musicVolume":'dw',
        "gamePause":'b',
        "ScrTransSpd":'dw',
        "ScrTransCover":'dw',
        "controlBitfieldP1":'w',
        "controlBitfieldP2":'w',
        "controlBitfieldP3":'w',
        "controlBitfieldP4":'w',
        "verticalOption":'dw',
        "horizOption":'dw',
        "horizOptionDest":'dw',
        "weather":'dw',
        "timeOfDay":'dw',
        "textureBufferPtrs":'dw', #51 32 bit pointers
        "charUnlockArray":'dw',#10 dwords
        "p1Data":plrStruct,
        "p2Data":plrStruct,
        "p3Data":plrStruct,
        "p4Data":plrStruct,
        "p5Data":plrStruct} 

#8 bytes (2 bytes * 4 players)
"""3 - LBrake
6 - Camera
7 - RBrake
8 - Spindash/Accelerate
A - Jump
B - Start
C - Up
D - Down
E - Left
F - Right"""

def setType(typ,val):
    if typ == 'b':
        return ctypes.wintypes.BYTE(val)
    elif typ == 'w':
        return ctypes.wintypes.WORD(val)
    elif typ == 'dw':
        return ctypes.wintypes.DWORD(val)
    else:
        print(f"Failed to asign {val} as {typ}")
        return -1

def write(name,off,val):
    global process,form,locs,ramOff
    add = process.base_address+off+locs[name]+ramOff
    if str(type(form[name])) == "<class 'dict'>":
        v = setType(form[name][off],val)
    else:
        v = setType(form[name],val)
    if v!=-1:
        process.write_ctype(add,v)

def read(name,off,pv):
    global process,form,locs,ramOff
    add = process.base_address+off+locs[name]+ramOff
    if str(type(form[name])) == "<class 'dict'>":
        v = setType(form[name][off],0)
    else:
        v = setType(form[name],None)
    if v!=-1:
        return process.read_ctype(address=add,ctype=v,get_py_value=pv)
