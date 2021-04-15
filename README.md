## SQLi and XSS datasets that are used in RAT: Reinforcement-Learning-Driven and Adaptive Testing for Vulnerability Discovery in Web Application Firewalls

### Download guide
This repository uses Git Large File Storage (LFS). Thus, cloning this repository requires an extra step.

In order to clone this repository, please first install the LFS extension by simply running the following command:

```
git lfs install
```

Then, it can be cloned like any other repositories:
```
git clone https://github.com/mhamouei/rat_datasets.git
```
### Decompression guide

These datasets are huge, so we compressed them using NumPy.
If your ram is below 64GB, we highly advise you to use the provided **extract.py** file. 
To do so, first install the following packages using pip:
```
pip install numpy
pip install tqdm
```
Finally, run the **extract.py** file:
```
python extract.py
```
