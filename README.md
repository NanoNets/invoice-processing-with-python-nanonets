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
    <img src="https://github.com/NanoNets/invoice-processing-with-python-nanonets/blob/master/demo/results.gif" width = "600"/>
</div>

### Step 1: Clone the Repo, Install dependencies
```bash
git clone https://github.com/NanoNets/invoice-processing-with-python-nanonets.git
cd invoice-processing-with-python-nanonets
```

### Step 2: Create a New Invoice Model
Get to app.nanonets.com and click `Invoices` you will be redirected to your Invoices model. 
<div align="center">
    <img src="https://github.com/NanoNets/invoice-processing-with-python-nanonets/blob/master/demo/SelectInvoices.png" alt="Click Invoices" width = "800"/>
</div>


### Step 3: Create a New Invoice Model
Once you are on the new model page click on the integrate tab in the sidebar
<div align="center">
    <img src="https://github.com/NanoNets/invoice-processing-with-python-nanonets/blob/master/demo/Integrate.png" alt="Click Integrate" width = "800"/>
</div>

### Step 4: Copy the code into a new file
Select the language of your choice and if you wish to send it a file url or local file on your computer
<div align="center">
    <img src="https://github.com/NanoNets/invoice-processing-with-python-nanonets/blob/master/demo/Copy.png" alt="Click Copy" width = "800"/>
</div>

### Step 5: Create a new file with the copied code
paste the copied code into a new file using your favorite text editor (if you chose python then copy and paste it into a file called `example.py`)

Inside the file replace the file path with the file path of the file you want to process.

**Sample Usage:**
```bash
python example.py
```