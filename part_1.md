# Part 1: Project setup and version control

### Question 1.1

Fork or clone this repository and host it on a personal GitHub account or an equivalent site that can be publicly accessed (eg. Bitbucket, Gitlab, personal host, etc). Please include a link to your copy of the repository as a part of your submission.

**PLEASE COMMIT YOUR ANSWERS INTO THAT COPY OF THE REPOSITORY**

### Question 1.2

Add a file called "os.txt" in the root of this repository and write the name of the operating system that you are using to do this test in the file (eg. "Ubuntu", "Windows").

### Answer

1. Create new file named os.txt

```powershell
New-Item -Path . -Name "os.txt" -ItemType "file"
```

2. fecth OS information and add it to file

```powershell
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, ServicePackMajorVersion, OSArchitecture, CSName, WindowsDirectory | Out-File -FilePath .\os.txt
```

### Question 1.3

Write a bash or PowerShell script in this repo root called `setup.sh` or `setup.ps1` to automatically:

- create a virtual environment named "env"
- activate that environment
- install the Python dependencies in requirements.txt into that virtual environment

Someone else should be able to run the script after git cloning this project, assuming they have virtualenv and pip available. Your script does not need to be idempotent.

### Answer

setup.psl

```powershell

    function create-venv {
    & python '-m' 'venv' 'env'
    & '.\env\Scripts\activate'
    }
     
    function activate-venv {
    & '.\env\Scripts\activate'
    }

    function install-dep {
        & pip install -r requirements.txt
        }

    create-venv
    activate-venv
    install-dep

```
