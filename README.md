<div align="center">
  <a href="https://nanonets.com/">
    <img src="https://nanonets.com/logo.png" alt="Invoice Processing with Python and Nanonets" width="100"/>
    </a>
</div>

<h1 align="center">Invoice Processing with Python and Nanonets</h1>

** **

## Reading Invoices

The Python + Nanonets Invoice Processing API uses Deep Learning to take an invoice and return the key values extracted from the Invoice.
** **

# Build a Invoice Processing API

>**Note:** Make sure you have python and pip installed on your system if you don't visit
[Python](https://www.python.org/downloads/release/python-2714/)
[pip](https://pip.pypa.io/en/stable/installing/)

<div align="center">
    <img src="https://github.com/NanoNets/invoice-processing-with-python-nanonets/blob/master/demo/results.gif" alt="number-plate-detection-gif" width = "600"/>
</div>

### Step 1: Clone the Repo, Install dependencies
```bash
git clone https://github.com/NanoNets/invoice-processing-with-python-nanonets.git
cd invoice-processing-with-python-nanonets
sudo pip install requests tqdm
```

### Step 2: Get your free API Key
Get your free API Key from http://app.nanonets.com/#/keys

### Step 3: Set the API key as an Environment Variable
```bash
export NANONETS_API_KEY=YOUR_API_KEY_GOES_HERE
```

### Step 4: Create a New Model
```bash
python ./code/create-model.py
```
 >_**Note:** This generates a MODEL_ID that you need for the next step

### Step 5: Add Model Id as Environment Variable
```bash
export NANONETS_MODEL_ID=YOUR_MODEL_ID
```
 >_**Note:** you will get YOUR_MODEL_ID from the previous step

### Step 6: Make Prediction
Once the model is trained. You can make predictions using the model
```bash
python ./code/prediction.py PATH_TO_YOUR_IMAGE.jpg
```

**Sample Usage:**
```bash
python ./code/prediction.py ./images/1.png
```