from django.db import models


class ParametersList(models.Model):
    name = models.TextField(blank=True, null=False)
    description = models.TextField(blank=True, null=True)
    measure = models.TextField(blank=True, null=True)
    normal_value = models.IntegerField(blank=True, null=True)
    delta = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Diagnoses(models.Model):
    name = models.TextField(blank=True, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Parameters(models.Model):
    parameter = models.ForeignKey(ParametersList, models.DO_NOTHING)
    research = models.ForeignKey('visor.Research', models.DO_NOTHING)
    diagnoses = models.ForeignKey(Diagnoses, models.DO_NOTHING)
    value = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.value}'


class Point():
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class FullParameters():
    def __init__(self):
        pass

    paramU1 = 0
    paramNL = 0
    paramI = 0
    paramNA = 0
    paramL1 = 0
    paramNB = 0
    paramU6 = 0
    paramPtV = 0
    paramN = 0
    paramSe = 0
    paramS = 0
    paramBa = 0
    paramAr = 0
    paramA = 0
    paramPNS = 0
    paramPg = 0
    paramGo = 0
    paramCo = 0
    paramGn = 0
    paramML = 0
    paramMe = 0
    paramNSL = 0
    paramOcL = 0
    paramAlfa = 0
    paramBeta = 0
    paramWits = 0
    paramSGo = 0
    paramNGn = 0
    paramSna = 0
    paramSNA = 0
    paramSn = 0
    paramSt = 0
    paramCol = 0
    paramUL = 0
    paramgl = 0
    paramsn = 0
    parampn = 0
    parampog = 0


class FullCalcResult():
    def __init__(self):
        pass

    slopeLowerJaw = 0
    slopeUpperJaw = 0
    slopeIncisors = 0
    interIncisorsAngle = 0
    posIncisorsUJ = 0
    posIncisorsLJ = 0
    posMolars = 0
    skullBase1 = 0
    skullBase2 = 0
    skullBase3 = 0
    lengthBaseUJ = 0
    lengthBodyUJ = 0
    sizeUJ = 0
    sizeLJ = 0
    sizeBranchLJ = 0
    frontHeightUJ = 0
    frontHeightLJ = 0
    backHeightUJ = 0
    backHeightLJ = 0
    posBaseUJ = 0
    posBaseLJ1 = 0
    posBaseLJ2 = 0
    LJAngle = 0
    posUJFromSkullBase = 0
    posLJFromSkullBase1 = 0
    posLJFromSkullBase2 = 0
    sagittalJawBase = 0
    posJawBase = 0
    wits = 0
    backHeightSkull = 0
    growAngle = 0
    frontHeightSkull = 0
    frontUpperHeight = 0
    lowerThirdPartFaceHeight = 0
    frontLowerHeight = 0
    backUpperHeight = 0
    backLowerHeight = 0
    jawAngle = 0
    faceProfileAngle = 0
    upperLipsHeight = 0
    lowerLipsAndChinHeight = 0
    upperLipsPos = 0
    lowerLipsPos = 0
    noseLipsAngle = 0


class DiagnosisResult():
    def __init__(self):
        pass

    slopeLowerJawDiag = ""
    slopeUpperJawDiag = ""
    slopeIncisorsDiag = ""
    interIncisorsAngleDiag = ""
    posIncisorsUJDiag = ""
    posIncisorsLJDiag = ""
    posMolarsDiag = ""
    skullBase1Diag = ""
    skullBase2Diag = ""
    skullBase3Diag = ""
    lengthBaseUJDiag = ""
    lengthBodyUJDiag = ""
    sizeUJDiag = ""
    sizeLJDiag = ""
    sizeBranchLJDiag = ""
    frontHeightUJDiag = ""
    frontHeightLJDiag = ""
    backHeightUJDiag = ""
    backHeightLJDiag = ""
    posBaseUJDiag = ""
    posBaseLJ1Diag = ""
    posBaseLJ2Diag = ""
    LJAngleDiag = ""
    posUJFromSkullBaseDiag = ""
    posLJFromSkullBase1Diag = ""
    posLJFromSkullBase2Diag = ""
    sagittalJawBaseDiag = ""
    posJawBaseDiag = ""
    witsDiag = ""
    backHeightSkullDiag = ""
    growAngleDiag = ""
    frontHeightSkullDiag = ""
    frontUpperHeightDiag = ""
    lowerThirdPartFaceHeightDiag = ""
    frontLowerHeightDiag = ""
    backUpperHeightDiag = ""
    backLowerHeightDiag = ""
    jawAngleDiag = ""
    faceProfileAngleDiag = ""
    upperLipsHeightDiag = ""
    lowerLipsAndChinHeightDiag = ""
    upperLipsPosDiag = ""
    lowerLipsPosDiag = ""
    noseLipsAngleDiag = ""
