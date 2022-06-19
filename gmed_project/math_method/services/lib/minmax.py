class Minmax():
    name = 'minmax'

    slopeLowerJawMin = 65
    slopeLowerJawMax = 75
    slopeUpperJawMin = 90
    slopeUpperJawMax = 100
    slopeIncisorsMin = 104
    slopeIncisorsMax = 104
    interIncisorsAngleMin = 128.47  # В сменном прикусе 131,12 ±2,650 в постоянном - 134,81± 3,060
    interIncisorsAngleMax = 133.77
    interIncisorsAngleMinPerm = 137.87  # В сменном прикусе 131,12 ±2,650 в постоянном -134,81± 3,060
    interIncisorsAngleMaxPerm = 131.75
    posIncisorsUJMin = 2
    posIncisorsUJMax = 6
    posIncisorsLJMin = 1.5
    posIncisorsLJMax = 6.5
    posMolarsMin = 9  # В сменном прикусе равно 12±3 мм,в постоянном -16,7±3мм.
    posMolarsMax = 15
    posMolarsMinPerm = 13.7  # В сменном прикусе равно 12±3 мм,в постоянном -16,7±3мм.
    posMolarsMaxPerm = 19.7
    skullBase1Min = 65.53  # В сменном прикусе равно 66,29± 0,76 мм,в постоянном -70,29±1 мм.
    skullBase1Max = 67.05
    skullBase1MinPerm = 69.29  # В сменном прикусе равно 66,29± 0,76 мм,в постоянном -70,29±1 мм.
    skullBase1MaxPerm = 71.29
    skullBase2Min = 124.3
    skullBase2Max = 134.3
    skullBase3Min = 117
    skullBase3Max = 128
    lengthBaseUJMin = 44.69  # В сменном прикусе 45,46 ±0,77мм,в постоянном -47,46± 2,14 мм. В норме составляет 70% от длины переднего основания черепа N-S
    lengthBaseUJMax = 46.23
    lengthBaseUJMinPerm = 45.32  # В сменном прикусе 45,46 ±0,77мм,в постоянном -47,46± 2,14 мм. В норме составляет 70% от длины переднего основания черепа N-S
    lengthBaseUJMaxPerm = 49.70
    lengthBodyUJMin = 65.12  # В сменном прикусе 66,33 ±1,21мм,в постоянном -73,74± 1,67 мм, в нормесоставляя N-S+3 мм.
    lengthBodyUJMax = 67.54
    lengthBodyUJMinPerm = 72.07  # В сменном прикусе 66,33 ±1,21мм,в постоянном -73,74± 1,67 мм, в нормесоставляя N-S+3 мм.
    lengthBodyUJMaxPerm = 75.41
    sizeUJMin = 0  # MacNamara
    sizeUJMax = 0  # MacNamara
    sizeLJMin = 0  # MacNamara
    sizeLJMax = 0  # MacNamara
    sizeBranchLJMin = 47.45  # В сменном прикусе 48,85 ±1,4мм,в постоянном -54,87±1,41 мм
    sizeBranchLJMax = 50.25
    sizeBranchLJMinPerm = 53.46  # В сменном прикусе 48,85 ±1,4мм,в постоянном -54,87±1,41 мм
    sizeBranchLJMaxPerm = 56.28
    frontHeightUJMin = 26.5
    frontHeightUJMax = 30.5
    frontHeightLJMin = 36  # В сменном прикусе 38 ±2 мм,в постоянном -44±3мм
    frontHeightLJMax = 40
    frontHeightLJMinPerm = 41  # В сменном прикусе 38 ±2 мм,в постоянном -44±3мм
    frontHeightLJMaxPerm = 47
    backHeightUJMin = 17  # В сменном прикусе 19 ±2 мм,в постоянном - 25± 3мм
    backHeightUJMax = 21
    backHeightUJMinPerm = 22  # В сменном прикусе 19 ±2 мм,в постоянном - 25± 3мм
    backHeightUJMaxPerm = 28
    backHeightLJMin = 27  # В сменном прикусе 29 ±2 мм,в постоянном -34 ± 3мм
    backHeightLJMax = 31
    backHeightLJMinPerm = 31  # В сменном прикусе 29 ±2 мм,в постоянном -34 ± 3мм
    backHeightLJMaxPerm = 37
    posBaseUJMin = 79
    posBaseUJMax = 85
    posBaseLJ1Min = 77
    posBaseLJ1Max = 83
    posBaseLJ2Min = 78
    posBaseLJ2Max = 84
    LJAngleMin = 123
    LJAngleMax = 137
    posUJFromSkullBaseMin = 5.5
    posUJFromSkullBaseMax = 13.5
    posLJFromSkullBase1Min = 28
    posLJFromSkullBase1Max = 36
    posLJFromSkullBase2Min = 14.8
    posLJFromSkullBase2Max = 20.8
    sagittalJawBaseMin = 27
    sagittalJawBaseMax = 35
    posJawBaseMin = 0  # В постоянномприкусе -1,6 ± 1,50
    posJawBaseMax = 0
    witsMin = 0  # При гармоничном развитии составляет 0-1±2,5 мм.
    witsMax = 0
    backHeightSkullMin = 65.7
    backHeightSkullMax = 71.7
    growAngleMin = 62
    growAngleMax = 65
    frontHeightSkullMin = 103.2  # В сменном прикусе 105,2 ±2 мм,в постоянном -113,3 ±0,4 мм
    frontHeightSkullMax = 107.2
    frontHeightSkullMinPerm = 112.9  # В сменном прикусе 105,2 ±2 мм,в постоянном -113,3 ±0,4 мм
    frontHeightSkullMaxPerm = 113.7
    frontUpperHeightMin = 45.58  # В сменном прикусе 46,7 ±1,12 мм,в постоянном -51,8 ±0,4 мм
    frontUpperHeightMax = 47.82
    frontUpperHeightMinPerm = 51.4  # В сменном прикусе 46,7 ±1,12 мм,в постоянном -51,8 ±0,4 мм
    frontUpperHeightMaxPerm = 52.2
    lowerThirdPartFaceHeightMin = 0 #MacNamara
    lowerThirdPartFaceHeightMax = 0
    frontLowerHeightMin = 52.89 #В сменном прикусе 54,2 ±1,31 мм,в постоянн
    frontLowerHeightMax = 55.51
    frontLowerHeightMinPerm = 0 #В сменном прикусе 54,2 ±1,31 мм,в постоянн
    frontLowerHeightMaxPerm = 0
    backUpperHeightMin = 39.9
    backUpperHeightMax = 41.9
    backLowerHeightMin = 44.5
    backLowerHeightMax = 49.5
    jawAngleMin = 23
    jawAngleMax = 28
    faceProfileAngleMin = 164
    faceProfileAngleMax = 172
    upperLipsHeightMin = 30
    upperLipsHeightMax = 40
    lowerLipsAndChinHeightMin = 30
    lowerLipsAndChinHeightMax = 40
    upperLipsPosMin = 35
    upperLipsPosMax = 35
    lowerLipsPosMin = 0
    lowerLipsPosMax = 4
    noseLipsAngleMin = 94
    noseLipsAngleMax = 110