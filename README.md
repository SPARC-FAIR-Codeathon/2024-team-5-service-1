# 2024-team-5- Service 1: File Format Converter

![License Badge](https://img.shields.io/badge/license-MIT-blue.svg) ![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg) ![Version](https://img.shields.io/badge/version-0.1.0-blue) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13308896.svg)](https://doi.org/10.5281/zenodo.13308896)

This module is part of:
<br/><br/>
<a href="https://github.com/SPARC-FAIR-Codeathon/2024-team-5">
<image src="https://github.com/appukuttan-shailesh/testData/blob/master/SPARC2024/oSPARCHub_logo.png?raw=true" height="200px" /></a>
<br/><br/>

This oSPARC service allows conversion of files between various formats such as CSV, JSON, YAML, XLS, XLSX, NWB (Neurodata Without Borders) and many others.

## Team #5 Repo

The team's main repo is located at:
https://github.com/SPARC-FAIR-Codeathon/2024-team-5

## Base Package

This oSPARC service was creating using [cookiecutter-osparc-service](
https://github.com/ITISFoundation/cookiecutter-osparc-service).


## Deployment Status

This service is awaiting deployment to oSPARC production. The GitHub actions fail, as we do not have the required permissions for the `build` stage:

> /home/scu/.venv/bin/python3: can't open file '/home/scu/.venv/bin/ooil': [Errno 13] Permission denied

Service has been deployed and tested locally via:
```
make publish-local
```

## Citation

Appukuttan, S., Benaribi, H., & Rievers, F. (2024). oSPARC Service #1: File Format Converter. Zenodo. https://doi.org/10.5281/zenodo.13308896


## Have an issue or question?
Please open an issue [here](https://github.com/SPARC-FAIR-Codeathon/2024-team-5-service-1/issues).
