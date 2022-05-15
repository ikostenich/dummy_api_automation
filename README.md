# dummy_api_automation

INTRODUCTION
------------

The repository contains the codebase for automated test of Dummy API.



INSTALLATION
------------
 
 ## 1. Running tests using docker
 
 ### Preconditions:
 * linux-based or mac_os operation system
 * docker installed
 
 ### Steps:
####  1. Clone the repository
  ```linux
git clone https://github.com/ikostenich/dummy_api_automation.git
```
####  2. Go to the project root directory
 
 ```linux
cd dummy_api_automation
```

#### 3. Build the docker image from Dockerfile
 ```linux
bash build_docker_image.sh
```

or 

 ```linux
docker build -t dummy_api_automation .
```
As the result "dummy_api_automation" docker image will be created and set up

#### 4. Run the automated tests via "run_in_docker.sh" bash script which automates container launch
 ```linux
bash run_in_docker.sh
```
You'll see tests running and bhief results of particular test cases
![test_launch_01](https://user-images.githubusercontent.com/18323106/168469883-53dd198b-48f8-40dc-9772-63a1ed417c17.png)

 
 ## 2. Running manually (without docker)
 
 ### Preconditions:
 * linux-based or mac_os operation system. Recommend using Ubuntu 20.04 desktop.
 * sudo rights to install packages
 
 ### Steps:
####  1. Clone the repository
  ```linux
git clone https://github.com/ikostenich/dummy_api_automation.git
```

####  2. Go to the project root directory
 
 ```linux
cd dummy_api_automation
```

#### 3. Check if python installed. 3.8+ version is required.    
```linux
python3 -V
```
If not installed: 
```linux
sudo apt-get update
sudo apt-get install python3.8
```

#### 4. Install python venv package. For 3.8 python:
```linux
sudo apt install python3.8-venv
```

### 5. Export environment variables

Api key is stored\used as environment variable

```linux
source .env
```

#### 6. Create python virtual environment

```linux
python3 -m venv ./venv
```


#### 7. Activate the virtual environment

```linux
source venv/bin/activate
```

#### 8. Install the required python packages
```linux
python3 setup.py install
```

#### 9. Go to test execution directory
```linux
cd dummy_api
```

#### 10. Run tests
```linux
python3 -m pytest
```

![image](https://user-images.githubusercontent.com/18323106/168470203-19541abe-4531-47e9-984f-b4a8c499db06.png)

