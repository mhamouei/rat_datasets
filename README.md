## SQLi and XSS datasets that are used in RAT: Reinforcement-Learning-Driven and Adaptive Testing for Vulnerability Discovery in Web Application Firewalls [[1]](#1)

### Download guide
This repository uses Git Large File Storage (LFS). Thus, cloning this repository requires an extra step.

In order to clone this repository, please first install the LFS extension by simply running the following command:

```
git lfs install
```

Then, it can be cloned by the command below:
```
git lfs clone https://github.com/mhamouei/rat_datasets.git
```
**If you experienced any issues cloning the repository using LFS, please use the following link to download the files:**
https://drive.google.com/file/d/1q-xQWhIsdJ-liFa_tApvBXbQNZI316nP/view?usp=sharing

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

## References
<a id="1">[1]</a> 
[M. Amouei, M. Rezvani and M. Fateh, "RAT: Reinforcement-Learning-Driven and Adaptive Testing for Vulnerability Discovery in Web Application Firewalls," in IEEE Transactions on Dependable and Secure Computing, doi: 10.1109/TDSC.2021.3095417.](https://doi.org/10.1109/TDSC.2021.3095417)
