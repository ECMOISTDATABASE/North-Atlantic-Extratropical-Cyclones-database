### Reproducing the Figure in Example Records (Case 029, 2002)

**Ensure Python Dependencies:**
First, ensure that you have installed the necessary Python dependencies. If not, create the Conda environment by executing the following commands:

```bash
conda env create -f ECdatasetenv.yml
conda activate ECdatasetenv
```

Clone the Repository:
Clone the repository to your local machine. Open your terminal or command prompt and execute the following command:

```bash
git clone https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database.git
```

Access the Example Case Directory:
Navigate to the Example_case_029_2002 directory within the cloned repository.

Update Path in Example Script:
Open the example_case.py script and locate line 176. Update the path direction to the content of the Moisture uptake .zip file according to your local directory structure.

Execute the Python Code:
Run the Python code within example_case.py to reproduce the figure.

Loop the Script (Optional):
Optionally, you can loop the script to reproduce the results for other cases or types of masks.
