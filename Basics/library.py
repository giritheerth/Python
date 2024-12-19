# matplot lib
'''
1. various data visualization task, exploratory data analysis, scientific plotting and creating publication-quality plots.
2. good for scenario where we need fine grained controls over plot customization and creat specialized visualizations.
3. cross platform and easy integration with numpy.

cons: limited 3D plotting, dependencies on external libraries

Apps: scientific research, finance, data analysis and education.

Layers:
1. scripting layer- top level - simple plots to mimic MATLAB plotting commands.
2. artist layer- full control and appearance of the plot.
3. background layer- lowest level - how to render and how to use different GUI ex: pyQT
'''
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,10])

# draw a line in a diagram from position (1,3) to (8,10)
plt.plot(xpoints, ypoints,'o')
plt.show()

# draw a line in a diagram 
xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints, ypoints)
plt.show()

# line style dotted / dashed
plt.plot(xpoints,ypoints,linestyle='dotted')
plt.plot(xpoints,ypoints,ls='--')
# multiple lines with different styles
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.xlabel('X-axis-Giri')
plt.ylabel('Y-axis-saraniyaa')
plt.show()
# histogram
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 




'''
matplot Grid -grid() function
matplot subplot
matplot scatter - scatter plot
matplot bars
matplot histogram - frequency distribution
matplot pie
matplot savefig
matplot show
matplot Legend
matplot title
'''
