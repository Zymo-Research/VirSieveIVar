import os

defaultPrimerBed = "/home/ivar/references/nCoV-2019.bed"
ivarExecutable = "/usr/local/bin/ivar"

def runIVarTrim(inputFilePath:str, outputFolder:str=None, primerBedFilePath:str=None):
    if not os.path.isfile(inputFilePath):
        raise FileNotFoundError("Unable to find input file for primer trimming at %s" % inputFilePath)
    if not primerBedFilePath:
        primerBedFilePath = defaultPrimerBed
    if not os.path.isfile(primerBedFilePath):
        raise FileNotFoundError("Unable to find primer bed file at %s" %primerBedFilePath)
    outputFileName = os.path.split(inputFilePath)[1][:-4] + ".primertrim.bam"
    outputFilePath = os.path.join(outputFolder, outputFileName)
    ivarCommand = "%s trim -i %s -b %s -e -p %s" %(ivarExecutable, inputFilePath, primerBedFilePath, outputFilePath[:-4])
    print("RUN: %s" %ivarCommand)
    exitStatus = os.system(ivarCommand)
    if exitStatus != 0:
        raise RuntimeError("iVar command failed with non-zero exit status of %s" %exitStatus)
    return outputFilePath