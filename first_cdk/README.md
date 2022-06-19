In my first _.cdk_ application, I will create a lambda function doing a simple `x+y` function

### Step 1: initiate CDK with python
```
cd hello_world
cdk init app --language python
```

### Step 2: install the environment
```
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Step 3: deplpy
```
cdk deploy
```
Note that sometimes we may need to run `cdk bootstrap --verbose`