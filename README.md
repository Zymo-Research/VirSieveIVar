# VirSieve iVar

## Summary

This container is part of the Environmental Viral Detection pipeline and covers the primer clipping portion of amplicon analysis.  This operation requires a BED file describing the loccation of the primers within the viral genome.  The output of this pipeline will be a BAM file with the primers clipped.

**SECURITY CONCERN**: This pipeline is currently using os.system to run commands and sanitization was causing runs to fail. If running files from untrusted sources, please be sure to sanitize file names to prevent potential command injections into the container.

### File naming and structure
Like other containers in the VirSieve Pipeline, this container is expected to run within a working folder.  Within that folder the expected input folder for this container is called **mergedBAM**.  It will output the resulting primer-clipped files to **primerTrimBAM** in the same working folder by default.  The default primer BED file is nCoV-2019.bed (ARTIC) in the internal reference folder, but this can be overridden by including a **primers.bed** file in the folder with the input data.  Alternatively, an environment variable can be passed explicitly giving the file to use as the primer BED file (see below for environment variables used by this container).

### Running the container
To run this container (presumed to be named _virsieveivar_ here), simply use the following command:
```bash
docker container run --rm -v /path/to/working/folder:/data virsieveivar
```

### Setting non-default options
Some options can be set to non-default values by passing them into the container as environmental variables using the standard Docker commandline technique for setting environmental variables as follows:

| Variable        | Type           | Default  | Description |
| --------------- |:--------------:|:--------:|-------------|
WORKINGFOLDER | string | /data | Working folder name within the container
INPUTFOLDER | string | /$WORKINGFOLDER/mergedBAM | The name of the incoming sequence folder within the working folder
PRIMERBED | string | /$WORKINGFOLDER/$INPUTFOLDER/adapters.fa | The BED file containing the primer locations for amplicon-based sequencing.  If this file is absent, the internal default will be used.
PROCESSEDREADFOLDER | string | /$WORKINGFOLDER/primerTrimBAM | The name of the output folder for this container


## Contributing

We welcome and encourage contributions to this project from the microbiomics community and will happily accept and acknowledge input (and possibly provide some free kits as a thank you).  We aim to provide a positive and inclusive environment for contributors that is free of any harassment or excessively harsh criticism. Our Golden Rule: *Treat others as you would like to be treated*.

## Versioning

We use a modification of [Semantic Versioning](https://semvar.org) to identify our releases.

Release identifiers will be *major.minor.patch*

Major release: Newly required parameter or other change that is not entirely backwards compatible
Minor release: New optional parameter
Patch release: No changes to parameters

## Authors

- **Michael M. Weinstein** - *Project Lead, Programming and Design* - [michael-weinstein](https://github.com/michael-weinstein)


See also the list of [contributors](https://github.com/Zymo-Research/figaro/contributors) who participated in this project.

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.
This license restricts the usage of this application for non-open sourced systems. Please contact the authors for questions related to relicensing of this software in non-open sourced systems.

## Acknowledgments

We would like to thank the following, without whom this would not have happened:
* The Python Foundation
* The staff at Zymo Research
* The scientific and public health COVID response community
* Our customers


