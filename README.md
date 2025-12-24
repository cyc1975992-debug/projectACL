## 우분투에서 실행하기
+ 가상환경 생성
```bash
    sudo apt update
    sudo apt install -y python3.10-venv python3-pip
    python3 -m venv py310
    source py310/bin/activate
```

+ scapy 패키지설치
```bash
    sudo python3 -m pip install scapy
```

+ 프로젝트 디렉토리설치
```bash
    mkdir /opt/projectACL
```

+ 메인 오플리케이션
```bash
    sudo vi /opt/projectACL/main.py
```

+ 메인 어플리케이션 실행
```bash
    sudo python3 main.py
```



### 우분투에 미니콘다 설치하기
+ 우분투에 파이썬을 설치하는 것은 다소 번거로움
+ 왜냐하면 소스를 내려받아 컴파일해야 하기 때문
+ 따라서, 미니콘다 배포파일을 다운로드해서 설치할 것을 추천!!
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-py311_25.11.1-1-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh

```


```bash
ubu@ubu:~$ mkdir -p ~/miniconda3
ubu@ubu:~$ wget https://repo.anaconda.com/miniconda/Miniconda3-py311_25.11.1-1-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
--2025-12-23 06:14:25--  https://repo.anaconda.com/miniconda/Miniconda3-py311_25.11.1-1-Linux-x86_64.sh
Resolving repo.anaconda.com (repo.anaconda.com)... 104.16.32.241, 104.16.191.158, 2606:4700::6810:bf9e, ...
Connecting to repo.anaconda.com (repo.anaconda.com)|104.16.32.241|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 155144821 (148M) [application/octet-stream]
Saving to: ‘/home/ubu/miniconda3/miniconda.sh’

/home/ubu/miniconda3/miniconda.sh          100%[=====================================================================================>] 147.96M  10.4MB/s    in 14s     

2025-12-23 06:14:38 (10.8 MB/s) - ‘/home/ubu/miniconda3/miniconda.sh’ saved [155144821/155144821]

ubu@ubu:~$ bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
PREFIX=/home/ubu/miniconda3
Unpacking bootstrapper...
Unpacking payload...

Installing base environment...

Preparing transaction: ...working... done
Executing transaction: ...working... done
installation finished.
ubu@ubu:~$ rm ~/miniconda3/miniconda.sh
```

### 설치확인
```bash
# 쉘 설정파일을 편집기로열고
vi ~/.bashrc

# 맨마지막줄에 다음내용추가
export PATH="$HOME/miniconda3/bin:$PATH"

# 변경사항 시스템적용
source ~/.bashrc

# 콘다 버젼확인 
conda --version

# 콘다 자동 base 환경 비활성화하고 확인 -> false
conda config --set auto_activate_base false
conda config --show auto_activate
```

### conda로 가상환경 생성 및 활성화
```bash
# 아래 2친구는 처음한번만실행
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

# 그다음 실행활성화
conda create -y -n py311 python=3.11
source activate py311
```

```bash
pip install --upgrade pip
pip install scapy

mkdir ~/projectACL
cd ~/projectACL
vi main.py
sudo ~/miniconda3/envs/py311/bin/python main.py
sudo python main.py
```

```bash
#py311 가상환경에서나가기
conda deactivate
```

