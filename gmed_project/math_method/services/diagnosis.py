from .lib.mcnamara import Mcnamara
from .lib.minmax import Minmax
from ..models import FullParameters, FullCalcResult, DiagnosisResult


class Diagnosis():
    mcNamara = Mcnamara()
    name = 'diagnosis'

    @staticmethod
    def calculateValues(params: FullParameters):
        result = FullCalcResult()

        # наклон резцов ВЧ относительно базиса ВЧ	U1/NL (наружный) град.
        result.slopeLowerJaw = params.paramU1 / params.paramNL
        # наклон резцов НЧ относительно базиса НЧ	L1/ML (внутренний) град.
        result.slopeUpperJaw = params.paramL1 / params.paramML
        # наклон резцов ВЧ относительно основания черепа	I\SN град.
        result.slopeIncisors = params.paramI / params.paramSN
        # межрезцовый угол	1/1 “alfa” град.
        result.interIncisorsAngle = params.paramAlfa
        # положение резцов ВЧ	U1-NA мм
        result.posIncisorsUJ = params.paramU1 - params.paramNA
        # положение резцов НЧ	 L1-NB мм
        result.posIncisorsLJ = params.paramL1 - params.paramNB
        # положение моляров	U6-PtV мм
        result.posMolars = params.paramU6 - params.paramPtV
        # основание черепа	N-Se мм
        result.skullBase1 = params.paramN - params.paramSe
        # N/S/Ba град.
        result.skullBase2 = params.paramN / params.paramS / params.paramBa
        # N/S/Ar град.
        result.skullBase3 = params.paramN / params.paramS / params.paramAr
        # Длина основания в/ч  	A’-PNS мм
        result.lengthBaseUJ = params.paramA - params.paramPNS
        # Длина тела н/ч      	Pg’-Go мм
        result.lengthBodyUJ = params.paramPg - params.paramGo
        # размер средней зоны лица (верхней челюсти)	A-Co мм
        result.sizeUJ = params.paramA - params.paramCo
        # размер нижней челюсти	Gn-Co мм
        result.sizeLJ = params.paramGn - params.paramCo
        # Длина ветви н/ч     	Co-Go мм
        result.sizeBranchLJ = params.paramCo - params.paramGo
        # Передняя высота в/ч  	U1-NL мм
        result.frontHeightUJ = params.paramU1 - params.paramNL
        # Передняя высота н/ч  	L1-ML мм
        result.frontHeightLJ = params.paramL1 - params.paramML
        # Задняя высота в/ч    	U6-NL мм
        result.backHeightUJ = params.paramU6 - params.paramNL
        # Задняя высота н/ч    	L6-ML мм
        result.backHeightLJ = params.paramL6 - params.paramML
        # положение базиса верхней челюсти	< S/N/A град.
        result.posBaseUJ = params.paramS / params.paramN / params.paramA
        # положение базиса нижней челюсти	< S/N/B град.
        result.posBaseLJ1 = params.paramS / params.paramN / params.paramB
        # < S/N/Pg град.
        result.posBaseLJ2 = params.paramS / params.paramN / params.paramPg
        # Нижнечелюстной угол	< Ar/Go/Me “Go” град.
        result.LJAngle = params.paramAr / params.paramGo / params.paramMe
        # положение верхней челюсти относительно основания черепа	< NL/NSL град.
        result.posUJFromSkullBase = params.paramNL / params.paramNSL
        # положение НЧ относительно основания черепа	< ML/NSL град.
        result.posLJFromSkullBase1 = params.paramML / params.paramNSL
        # < ML/OcL град.
        result.posLJFromSkullBase2 = params.paramML / params.paramUcL
        # Соотношение челюстных костей по сагиттали и вертикали Beta
        result.sagittalJawBase = params.paramBeta
        # Положение базисов челюстей относительно друг друга	< А/N/B град.
        result.posJawBase = params.paramA / params.paramN / params.paramB
        # Wits-число  мм
        result.wits = params.paramWits
        # Задняя высота черепа  	S-Go мм
        result.backHeightSkull = params.paramS - params.paramGo
        # направление роста	SGo\NGn %
        result.growAngle = params.paramSGo / params.paramNGn
        # Передняя высота черепа  	N-Gn мм
        result.frontHeightSkull = params.paramN - params.paramGn
        # Передняя верхняя высота  	N-Sna мм
        result.frontUpperHeight = params.paramN - params.paramSna
        # Высота нижней трети лица	SNA-Me мм
        result.lowerThirdPartFaceHeight = params.paramSNA - params.paramMe
        # Передняя нижняя высота  	Sna-Gn мм
        result.frontLowerHeight = params.paramSna - params.paramGn
        # Задняя верхняя высота  	Snp-NSL мм
        result.backUpperHeight = params.paramSnp - params.paramNSL
        # Задняя нижняя высота  	Ar-Go мм
        result.backLowerHeight = params.paramAr - params.paramGo
        # межчелюстной угол	< NL/ML град.
        result.jawAngle = params.paramNL / params.paramML
        # Угол профиля лица	<gl-sn-pg град.
        result.faceProfileAngle = params.paramgl - params.paramsn - params.paramPg
        # высота верхней губы	sn-st мм
        result.upperLipsHeight = params.paramsn - params.paramSt
        # высота нижней губы с подбородком	st-me мм
        result.lowerLipsAndChinHeight = params.paramSt - params.paramMe
        # положение верхней губы относительно эстетической плоскости Е	pn-pog мм
        result.upperLipsPos = params.parampn - params.parampog
        # положение нижней губы относительно эстетической плоскости Е	pn-pg мм
        result.lowerLipsPos = params.parampn - params.paramPg
        # носогубный угол	col-sn-UL мм
        result.noseLipsAngle = params.paramCol - params.paramsn - params.paramUL

        return result

    @staticmethod
    def makediagnosis(permbite: bool, params: FullCalcResult):
        result = DiagnosisResult()
        minmax = Minmax()
        if params.slopeLowerJaw < minmax.slopeLowerJawMin:
            result.slopeLowerJawDiag = "протрузия резцов ВЧ"
        if params.slopeLowerJaw > minmax.slopeLowerJawMax:
            result.slopeLowerJawDiag = "ретрузия резцов ВЧ"

        if params.slopeUpperJaw < minmax.slopeUpperJawMin:
            result.slopeUpperJawDiag = "ретрузия резцов НЧ"
        if params.slopeUpperJaw > minmax.slopeUpperJawMax:
            result.slopeUpperJawDiag = "протрузия резцов НЧ"

        if params.slopeIncisors < minmax.slopeIncisorsMin:
            result.slopeIncisorsDiag = "ретрузия резцов ВЧ"
        if params.slopeIncisors > minmax.slopeIncisorsMax:
            result.slopeIncisorsDiag = "протрузия резцов ВЧ"

        if permbite:
            if params.interIncisorsAngle < minmax.interIncisorsAngleMinPerm:
                result.interIncisorsAngleDiag = "бипротрузия соотношения резцов"
            if params.interIncisorsAngle > minmax.interIncisorsAngleMaxPerm:
                result.interIncisorsAngleDiag = "опистогн. Соотношение резцов"
        else:
            if params.interIncisorsAngle < minmax.interIncisorsAngleMin:
                result.interIncisorsAngleDiag = "бипротрузия соотношения резцов"
            if params.interIncisorsAngle > minmax.interIncisorsAngleMax:
                result.interIncisorsAngleDiag = "опистогн. Соотношение резцов"

        if params.posIncisorsUJ < minmax.posIncisorsUJMin:
            result.posIncisorsUJDiag = "ретрузия резцов ВЧ"
        if params.posIncisorsUJ > minmax.posIncisorsUJMax:
            result.posIncisorsUJDiag = "протрузия резцов ВЧ"

        if params.posIncisorsLJ < minmax.posIncisorsLJMin:
            result.posIncisorsLJDiag = "ретрузия резцов НЧ"
        if params.posIncisorsLJ > minmax.posIncisorsLJMax:
            result.posIncisorsLJDiag = "протрузия резцов НЧ"

        if permbite:
            if params.posMolars < minmax.posMolarsMinPerm:
                result.posMolarsDiag = "мезиальное положение моляров"
            if params.posMolars > minmax.posMolarsMaxPerm:
                result.posMolarsDiag = "дистальное положение моляров"
        else:
            if params.posMolars < minmax.posMolarsMin:
                result.posMolarsDiag = "мезиальное положение моляров"
            if params.posMolars > minmax.posMolarsMax:
                result.posMolarsDiag = "дистальное положение моляров"

        if permbite:
            if params.skullBase1 < minmax.skullBase1MinPerm:
                result.skullBase1Diag = "уменьшение размеров основания черепа"
            if params.skullBase1 > minmax.skullBase1MaxPerm:
                result.skullBase1Diag = "увеличение размеров основания черепа"
        else:
            if params.skullBase1 < minmax.skullBase1Min:
                result.skullBase1Diag = "уменьшение размеров основания черепа"
            if params.skullBase1 > minmax.skullBase1Max:
                result.skullBase1Diag = "увеличение размеров основания черепа"

        if params.skullBase2 < minmax.skullBase2Min:
            result.skullBase2Diag = "уменьшение угла наклона основания черепа: прогнатический тип профиля"
        if params.skullBase2 > minmax.skullBase2Max:
            result.skullBase2Diag = "увеличение - ретрогнатический тип профиля"

        if params.skullBase3 < minmax.skullBase3Min:
            result.skullBase3Diag = "малое значение - передняя позиция ямки - прогнатия"
        if params.skullBase3 > minmax.skullBase3Max:
            result.skullBase3Diag = "большое значение угла - задняя позиция суставной ямки - ретрогнатия"

        if permbite:
            if params.lengthBaseUJ < minmax.lengthBaseUJMinPerm:
                result.lengthBaseUJDiag = "микрогнатия ВЧ"
            if params.lengthBaseUJ > minmax.lengthBaseUJMaxPerm:
                result.lengthBaseUJDiag = "макрогнатия ВЧ"
        else:
            if params.lengthBaseUJ < minmax.lengthBaseUJMin:
                result.lengthBaseUJDiag = "микрогнатия ВЧ"
            if params.lengthBaseUJ > minmax.lengthBaseUJMax:
                result.lengthBaseUJDiag = "макрогнатия ВЧ"

        if permbite:
            if params.lengthBodyUJ < minmax.lengthBodyUJMinPerm:
                result.lengthBodyUJDiag = "микрогнатия ВЧ"
            if params.lengthBodyUJ > minmax.lengthBodyUJMaxPerm:
                result.lengthBodyUJDiag = "макрогнатия ВЧ"
        else:
            if params.lengthBodyUJ < minmax.lengthBodyUJMin:
                result.lengthBodyUJDiag = "микрогнатия НЧ"
            if params.lengthBodyUJ > minmax.lengthBodyUJMax:
                result.lengthBodyUJDiag = "макрогнатия НЧ"

        if params.sizeUJ < minmax.sizeUJMin:
            result.sizeUJDiag = "верхняя микрогнатия"
        if params.sizeUJ > minmax.sizeUJMax:
            result.sizeUJDiag = "верхняя макрогнатия"

        if params.sizeLJ < minmax.sizeLJMin:
            result.sizeLJDiag = "нижняя микрогнатия"
        if params.sizeLJ > minmax.sizeLJMax:
            result.sizeLJDiag = "нижняя макрогнатия"

        if permbite:
            if params.sizeBranchLJ < minmax.sizeBranchLJMinPerm:
                result.sizeBranchLJDiag = "уменьшение размера ветви НЧ"
            if params.sizeBranchLJ > minmax.sizeBranchLJMaxPerm:
                result.sizeBranchLJDiag = "увеличение размера ветви НЧ"
        else:
            if params.sizeBranchLJ < minmax.sizeBranchLJMin:
                result.sizeBranchLJDiag = "уменьшение размера ветви НЧ"
            if params.sizeBranchLJ > minmax.sizeBranchLJMax:
                result.sizeBranchLJDiag = "увеличение размера ветви НЧ"

        if permbite:
            if params.frontHeightUJ < minmax.frontHeightUJMin:
                result.frontHeightUJDiag = "Снижение высоты переднего отдела ВЧ"
            if params.frontHeightUJ > minmax.frontHeightUJMax:
                result.frontHeightUJDiag = "Повышение высоты переднего отдела ВЧ"

        if permbite:
            if params.frontHeightLJ < minmax.frontHeightLJMinPerm:
                result.frontHeightLJDiag = "Снижение высоты переднего отдела НЧ"
            if params.frontHeightLJ > minmax.frontHeightLJMaxPerm:
                result.frontHeightLJDiag = "Повышение высоты переднего отдела НЧ"
        else:
            if params.frontHeightLJ < minmax.frontHeightLJMin:
                result.frontHeightLJDiag = "Снижение высоты переднего отдела НЧ"
            if params.frontHeightLJ > minmax.frontHeightLJMax:
                result.frontHeightLJDiag = "Повышение высоты переднего отдела НЧ"

        if permbite:
            if params.backHeightUJ < minmax.backHeightUJMinPerm:
                result.backHeightUJDiag = "Снижение высоты заднего отдела ВЧ"
            if params.backHeightUJ > minmax.backHeightUJMaxPerm:
                result.backHeightUJDiag = "Повышение высоты заднего отдела ВЧ"
        else:
            if params.backHeightUJ < minmax.backHeightUJMin:
                result.backHeightUJDiag = "Снижение высоты заднего отдела ВЧ"
            if params.backHeightUJ > minmax.backHeightUJMax:
                result.backHeightUJDiag = "Повышение высоты заднего отдела ВЧ"

        if permbite:
            if params.backHeightLJ < minmax.backHeightLJMinPerm:
                result.backHeightLJDiag = "Снижение высоты заднего отдела НЧ"
            if params.backHeightLJ > minmax.backHeightLJMaxPerm:
                result.backHeightLJDiag = "Повышение высоты заднего отдела НЧ"
        else:
            if params.backHeightLJ < minmax.backHeightLJMin:
                result.backHeightLJDiag = "Снижение высоты заднего отдела НЧ"
            if params.backHeightLJ > minmax.backHeightLJMax:
                result.backHeightLJDiag = "Повышение высоты заднего отдела НЧ"

        if params.posBaseUJ < minmax.posBaseUJMin:
            result.posBaseUJDiag = "верхняя ретрогнатия, ретропозиция"
        if params.posBaseUJ > minmax.posBaseUJMax:
            result.posBaseUJDiag = "верхняя прогнатия, антеропозиция"

        if params.posBaseLJ1 < minmax.posBaseLJ1Min:
            result.posBaseLJ1Diag = "нижняя ретрогнатия, ретропозиция"
        if params.posBaseLJ1 > minmax.posBaseLJ1Max:
            result.posBaseLJ1Diag = "нижняя прогнатия, антеропозиция"

        if params.posBaseLJ2 < minmax.posBaseLJ2Min:
            result.posBaseLJ2Diag = "нижняя ретрогнатия, ретропозиция"
        if params.posBaseLJ2 > minmax.posBaseLJ2Max:
            result.posBaseLJ2Diag = "нижняя прогнатия, антеропозиция"

        if params.LJAngle < minmax.LJAngleMin:
            result.LJAngleDiag = "гипердивергентный, или вертикальный тип развития"
        if params.LJAngle > minmax.LJAngleMax:
            result.LJAngleDiag = "гиподивергентный, или горизонтальный тип развития"

        if params.posUJFromSkullBase < minmax.posUJFromSkullBaseMin:
            result.posUJFromSkullBaseDiag = "антеинкпинация ВЧ"
        if params.posUJFromSkullBase > minmax.posUJFromSkullBaseMax:
            result.posUJFromSkullBaseDiag = "ретроинклинация ВЧ"

        if params.posLJFromSkullBase1 < minmax.posLJFromSkullBase1Min:
            result.posLJFromSkullBase1Diag = "гиподивергентный, или горизонтальный тип развития"
        if params.posLJFromSkullBase1 > minmax.posLJFromSkullBase1Max:
            result.posLJFromSkullBase1Diag = "гипердивергентный тип строения лицевого скелета или вертикальный тип развития"

        if params.posLJFromSkullBase2 < minmax.posLJFromSkullBase2Min:
            result.posLJFromSkullBase2Diag = "гиподивергентный, или горизонтальный тип развития"
        if params.posLJFromSkullBase2 > minmax.posLJFromSkullBase2Max:
            result.posLJFromSkullBase2Diag = "гипердивергентный тип строения лицевого скелета или вертикальный тип развития"

        if params.sagittalJawBase < minmax.sagittalJawBaseMin:
            result.sagittalJawBaseDiag = "скелетный класс II"
        if params.sagittalJawBase > minmax.sagittalJawBaseMax:
            result.sagittalJawBaseDiag = "скелетный класс III"

        if params.posJawBase < minmax.posJawBaseMin:
            result.posJawBase = "скелетный класс III"
        if params.posJawBase > minmax.posJawBaseMax:
            result.posJawBase = "скелетный класс II"

        if params.wits < minmax.witsMin:
            result.witsDiag = "скелетный класс II"
        if params.wits > minmax.witsMax:
            result.witsDiag = "скелетный класс III"

        if params.backHeightSkull < minmax.backHeightSkullMin:
            result.backHeightSkullDiag = "скелетный класс II"
        if params.backHeightSkull > minmax.backHeightSkullMax:
            result.backHeightSkullDiag = "скелетный класс III"

        if params.growAngle < minmax.growAngleMin:
            result.growAngleDiag = "горизонтальный тип роста"
        if params.growAngle > minmax.growAngleMax:
            result.growAngleDiag = "вертикальный тип роста"

        if permbite:
            if params.frontHeightSkull < minmax.frontHeightSkullMinPerm:
                result.frontHeightSkullDiag = "снижение высоты переднего отдела лица"
            if params.frontHeightSkull > minmax.frontHeightSkullMaxPerm:
                result.frontHeightSkullDiag = "повышение высоты переднего отдела лица"
        else:
            if params.frontHeightSkull < minmax.frontHeightSkullMin:
                result.frontHeightSkullDiag = "снижение высоты переднего отдела лица"
            if params.frontHeightSkull > minmax.frontHeightSkullMax:
                result.frontHeightSkullDiag = "повышение высоты переднего отдела лица"

        if permbite:
            if params.frontUpperHeight < minmax.frontUpperHeightMinPerm:
                result.frontUpperHeightDiag = "снижение высоты среднего отдела лица"
            if params.frontUpperHeight > minmax.frontUpperHeightMaxPerm:
                result.frontUpperHeightDiag = "повышение высоты среднего отдела лица"
        else:
            if params.frontUpperHeight < minmax.frontUpperHeightMin:
                result.frontUpperHeightDiag = "снижение высоты среднего отдела лица"
            if params.frontUpperHeight > minmax.frontUpperHeightMax:
                result.frontUpperHeightDiag = "повышение высоты среднего отдела лица"

        if params.lowerThirdPartFaceHeight < minmax.lowerThirdPartFaceHeightMin:
            result.lowerThirdPartFaceHeightDiag = "прогнатия нижней челюсти"
        if params.lowerThirdPartFaceHeight > minmax.lowerThirdPartFaceHeightMax:
            result.lowerThirdPartFaceHeightDiag = "ретрогнатия нижней челюсти"

        if permbite:
            if params.frontLowerHeight < minmax.frontLowerHeightMinPerm:
                result.frontLowerHeightDiag = "снижение размеров нижней трети лица"
            if params.frontLowerHeight > minmax.frontLowerHeightMaxPerm:
                result.frontLowerHeightDiag = "увеличение размеров нижней трети лица"
        else:
            if params.frontLowerHeight < minmax.frontLowerHeightMin:
                result.frontLowerHeightDiag = "снижение размеров нижней трети лица"
            if params.frontLowerHeight > minmax.frontLowerHeightMax:
                result.frontLowerHeightDiag = "увеличение размеров нижней трети лица"

        if params.backUpperHeight < minmax.backUpperHeightMin:
            result.backUpperHeightDiag = "Снижение задней верхней высоты"
        if params.backUpperHeight > minmax.backUpperHeightMax:
            result.backUpperHeightDiag = "Увеличение задней верхней высоты"

        if params.backLowerHeight < minmax.backLowerHeightMin:
            result.backLowerHeightDiag = "Снижение задней нижней высоты"
        if params.backLowerHeight > minmax.backLowerHeightMax:
            result.backLowerHeightDiag = "Увеличение задней нижней высоты"

        if params.jawAngle < minmax.jawAngleMin:
            result.jawAngleDiag = "гиподивергентный, или горизонтальный тип развития"
        if params.jawAngle > minmax.jawAngleMax:
            result.jawAngleDiag = "гипердивергентный тип строения лицевого скелета или вертикальный тип развития"

        if params.faceProfileAngle < minmax.faceProfileAngleMin:
            result.faceProfileAngleDiag = "вогнутый профиль лица"
        if params.faceProfileAngle > minmax.faceProfileAngleMax:
            result.faceProfileAngleDiag = "выпуклый профиль лица"

        if params.upperLipsHeight < minmax.upperLipsHeightMin:
            result.upperLipsHeightDiag = ""
        if params.upperLipsHeight > minmax.upperLipsHeightMax:
            result.upperLipsHeightDiag = ""

        if params.lowerLipsAndChinHeight < minmax.lowerLipsAndChinHeightMin:
            result.lowerLipsAndChinHeightDiag = ""
        if params.lowerLipsAndChinHeight > minmax.lowerLipsAndChinHeightMax:
            result.lowerLipsAndChinHeightDiag = ""

        if params.upperLipsPos < minmax.upperLipsPosMin:
            result.upperLipsPosDiag = "положение губы ВЧ кзади"
        if params.upperLipsPos > minmax.upperLipsPosMax:
            result.upperLipsPosDiag = "положение губы ВЧ кпереди"

        if params.lowerLipsPos < minmax.lowerLipsPosMin:
            result.lowerLipsPosDiag = "положение губы НЧ кзади"
        if params.lowerLipsPos > minmax.lowerLipsPosMax:
            result.lowerLipsPosDiag = "положение губы НЧ кпереди"

        if params.noseLipsAngle < minmax.noseLipsAngleMin:
            result.noseLipsAngleDiag = ""
        if params.noseLipsAngle > minmax.noseLipsAngleMax:
            result.noseLipsAngleDiag = ""

