# Getting Started

### Installation

1. `python 3.8` 버전과 `VScode` 또는 `PyCharm` 을 설치합니다.
2. 본 repo 의 `develop` 브랜치를 clone 합니다. (git clone -b develop https://github.com/isaac105/instant_coding.git)
3. 터미널을 열어 프로젝트의 루트 경로에서 `python -m venv venv` 명령어를 통해 새로운 virtualenv를 생성합니다.
4. `cd venv` -> `Scripts\activate.bat` -> (가상환경진입)`pip install -r .requirements.txt` 명령을 순차적으로 실행하여 dependency package를 설치합니다.  # 윈도우 기준

### Git Guideline

- 프로젝트의 버전 관리는 `Github` 의 본 repository 를 통해 진행합니다. 
- remote repository 는 `master`, `develop` 이렇게 2개의 branch 를 가집니다.
- `master` branch 는 최종 확정된 코드이고, direct push 는 허가되지 않으며, 오직 Merge Request 를 통해서만 변경이 이루어 질 수 있습니다.
- `develop` branch 는 실질적으로 개발용 branch 이며 작업 시 본 branch 의 feature branch 를 checkout 후 작업한 후 merge request 를 생성하시면 됩니다.

### Coding Convention

- 모든 코드는 `Python 3.8` 을 기준으로 작성합니다.
- 코드 스타일은 [PEP8 Style Guide](https://peps.python.org/pep-0008/) 을 준수하는 것이 원칙이나 문서 참고하여 크게 벗어나지 않도록 작성합니다. 


### Etc.

1. branch change 시, 오류 해결법 
- 해당 에러 발생 시, 진행 [Git: invalid path 'stanford.edu/~cpiech/karel/ace/index.html?C=D;O=A']

> git reset  
> git config core.protectNTFS false  
> git origin/develop  
