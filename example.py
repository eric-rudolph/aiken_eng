import aiken_eng
import aiken_eng.plotting as plotting


print(aiken_eng.hello())

x=[3,4,5,6]
y=[12,23,34,45]
plotting.plot(x,y,x_label="my x", title="Sample Plot")