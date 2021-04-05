import ivarSupport
import os


workingFolderEnv = os.environ.setdefault("WORKINGFOLDER", "/data")
if not os.path.isdir(workingFolderEnv):
    raise NotADirectoryError("Unable to find working directory at %s" %workingFolderEnv)
inputFolderEnv = os.environ.setdefault("INPUTFOLDER", os.path.join(workingFolderEnv, "mergedBAM"))
if not os.path.isdir(inputFolderEnv):
    raise NotADirectoryError("Unable to find input folder at %s" %inputFolderEnv)
primerBedFileEnv = os.environ.setdefault("PRIMERBED", os.path.join(inputFolderEnv, "primers.bed"))
if not os.path.isfile(primerBedFileEnv):
    primerBedFileEnv = None
processedReadsFolderEnv = os.environ.setdefault("PROCESSEDREADFOLDER", os.path.join(workingFolderEnv, "primerTrimBAM"))
if not os.path.isdir(processedReadsFolderEnv):
    os.mkdir(processedReadsFolderEnv)


def performAdapterTrimming(inputFolder:str=inputFolderEnv, outputFolder:str=processedReadsFolderEnv, primerBedFile:str=primerBedFileEnv):
    if not os.path.isdir(inputFolder):
        raise NotADirectoryError("Unable to find input directory at %s" %inputFolder)
    rawFiles = os.listdir(inputFolder)
    filteredFiles = []
    outputFiles = []
    for file in rawFiles:
        if not os.path.isfile(os.path.join(inputFolder, file)):
            continue
        if not file.endswith(".bam"):
            continue
        filteredFiles.append(os.path.join(inputFolder, file))
    for file in filteredFiles:
        print("Primer trimming %s with iVar" %(file))
        outputFile = ivarSupport.ivarTrimmer.runIVarTrim(file, outputFolder, primerBedFile)
        outputFiles.append(outputFile)
        print("Trimming complete")
    return outputFiles


if __name__ == "__main__":
    performAdapterTrimming()

