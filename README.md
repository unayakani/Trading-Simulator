# Progress tracker
---
`12/11/24`

Created basic boilerplate code. Was able to simulate random chart. (considered modules like `plotly` and `uncertainties` but settled on `matplotlib` and `numpy`)(could have used `random` instead of `numpy`)

```python
import random
# import tkinter as tk
# import pygame
import matplotlib.pyplot as plt
import numpy

xplot = [0.0]
yplot = [0.0]

for i in range(100):
    xplot.append(xplot[-1] + 1)
    plus_minus = random.randrange(0, 2)
    if plus_minus == 0:
        yplot.append(yplot[-1] + float(numpy.random.random()))
    else:
        yplot.append(yplot[-1] - float(numpy.random.random()))

plt.plot(xplot, yplot)
plt.show()
```

![fig](./figures/12nov.png)

---
`13/11/24`

Decided to ditch the racing part and just do a trading sim. Decided to use streamlit for gui. Created a virtual environment for `pip install`ing modules.
See ac40536
---
